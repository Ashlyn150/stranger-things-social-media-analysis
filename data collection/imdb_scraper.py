"""
IMDb Stranger Things - Selenium Review Scraper with Amazon Login
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re

# ── Fill in your Amazone email & password here ──
AMAZON_EMAIL    = "YOUR EMAIL ADDRESS"
AMAZON_PASSWORD = "PASS CODE"
# ────────────────────────────────────────

URL    = "https://www.imdb.com/title/tt4574334/reviews"
TARGET = 5636


def build_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


def login(driver, wait):
    print("Navigating to IMDb login page...")
    driver.get("https://www.imdb.com/registration/signin")
    time.sleep(3)

    # Click "Sign in with Amazon"
    try:
        amazon_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='amazon'], button[data-testid*='amazon'], a[class*='amazon']")
        ))
        amazon_btn.click()
        print("Clicked 'Sign in with Amazon'")
        time.sleep(3)
    except TimeoutException:
        # Try finding by text
        try:
            btns = driver.find_elements(By.TAG_NAME, "a")
            for btn in btns:
                if "amazon" in btn.text.lower() or "amazon" in (btn.get_attribute("href") or "").lower():
                    btn.click()
                    print("Clicked Amazon login link")
                    time.sleep(3)
                    break
        except Exception as e:
            print(f"Could not find Amazon login button: {e}")
            print("Please log in manually in the Chrome window, then press Enter here...")
            input()
            return

    # Fill in Amazon email
    try:
        email_field = wait.until(EC.presence_of_element_located((By.ID, "ap_email")))
        email_field.clear()
        email_field.send_keys(AMAZON_EMAIL)
        time.sleep(1)

        # Click Continue
        try:
            continue_btn = driver.find_element(By.ID, "continue")
            continue_btn.click()
            time.sleep(2)
        except NoSuchElementException:
            pass

        # Fill in password
        password_field = wait.until(EC.presence_of_element_located((By.ID, "ap_password")))
        password_field.clear()
        password_field.send_keys(AMAZON_PASSWORD)
        time.sleep(1)

        # Click Sign in
        signin_btn = driver.find_element(By.ID, "signInSubmit")
        signin_btn.click()
        print("Submitted login form...")
        time.sleep(4)

    except TimeoutException:
        print("Could not find Amazon login fields automatically.")
        print("Please log in manually in the Chrome window, then press Enter here...")
        input()

    # Check if login succeeded
    if "imdb.com" in driver.current_url:
        print("Login successful!")
    else:
        print("Still on Amazon page - may need 2FA or CAPTCHA.")
        print("Please complete login manually in the Chrome window, then press Enter here...")
        input()


def parse_reviews(html):
    soup = BeautifulSoup(html, "html.parser")
    reviews = []

    containers = soup.find_all("div", class_="review-container")
    if not containers:
        containers = soup.find_all("article", class_=re.compile(r"review", re.I))
    if not containers:
        containers = soup.find_all(attrs={"data-testid": re.compile(r"review-card|user-review", re.I)})

    for item in containers:
        review = {}

        # Rating
        rating_tag = (item.find("span", class_="ipc-rating-star--rating")
                      or item.find("span", class_="rating-other-user-rating"))
        if rating_tag:
            nums = re.findall(r"\d+", rating_tag.get_text())
            review["rating"] = nums[0] if nums else None
        else:
            review["rating"] = None

        # Title
        title_tag = (item.find("a", class_="title")
                     or item.find(attrs={"data-testid": "review-summary"})
                     or item.find("h3"))
        review["title"] = title_tag.get_text(strip=True) if title_tag else None

        # Content
        content_tag = (item.find("div", class_="text show-more__control")
                       or item.find("div", class_="text")
                       or item.find(attrs={"data-testid": "review-overflow"}))
        review["content"] = content_tag.get_text(strip=True) if content_tag else None

        # Author
        author_tag = (item.find("span", class_="display-name-link")
                      or item.find(attrs={"data-testid": "author-link"}))
        review["author"] = author_tag.get_text(strip=True) if author_tag else None

        # Date
        date_tag = (item.find("li", class_="review-date")
                    or item.find("span", class_="review-date")
                    or item.find("time"))
        if date_tag:
            review["date"] = date_tag.get("datetime") or date_tag.get_text(strip=True)
        else:
            review["date"] = None

        # Helpful (thumbs up count)
        helpful_tag = item.find("span", class_="ipc-voting__label__count--up")
        review["helpful"] = helpful_tag.get_text(strip=True) if helpful_tag else None

        # Not helpful (thumbs down count)
        not_helpful_tag = item.find("span", class_="ipc-voting__label__count--down")
        review["not_helpful"] = not_helpful_tag.get_text(strip=True) if not_helpful_tag else None

        reviews.append(review)

    return soup, reviews


def click_load_more(driver):
    try:
        btn = WebDriverWait(driver, 6).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                "button.ipc-see-more__button"))
        )
        driver.execute_script("arguments[0].click();", btn)
        return True
    except TimeoutException:
        # Try finding by text content
        try:
            btns = driver.find_elements(By.TAG_NAME, "button")
            for btn in btns:
                if "see all" in btn.text.lower() or "load more" in btn.text.lower():
                    driver.execute_script("arguments[0].click();", btn)
                    return True
        except Exception:
            pass
        return False


def save_csv(data, filename):
    df = pd.DataFrame(data)
    df.insert(0, "no", range(1, len(df) + 1))
    # Set column order
    cols = ["no", "author", "date", "rating", "title", "content", "helpful", "not_helpful"]
    cols = [c for c in cols if c in df.columns]
    df = df[cols]
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"  Saved: {len(df)} reviews -> {filename}")


def main():
    print("=" * 55)
    print("  IMDb Stranger Things - Full Review Scraper")
    print(f"  Target: {TARGET} reviews")
    print("=" * 55)

    if AMAZON_PASSWORD == "YOUR_PASSWORD_HERE":
        print("\nERROR: Please open imdb_scraper.py and fill in your password.")
        print("Find this line:  AMAZON_PASSWORD = \"YOUR_PASSWORD_HERE\"")
        print("Replace YOUR_PASSWORD_HERE with your actual Amazon password.")
        return

    print("\nOpening Chrome... (do not close the window)\n")
    driver = build_driver()
    wait = WebDriverWait(driver, 15)
    all_reviews = []

    try:
        login(driver, wait)

        print(f"\nNavigating to reviews page...")
        driver.get(URL)
        time.sleep(3)

        no_new_count = 0

        while len(all_reviews) < TARGET:
            html = driver.page_source
            _, reviews = parse_reviews(html)

            prev_count = len(all_reviews)
            all_reviews = reviews
            new = len(all_reviews) - prev_count

            print(f"  Loaded: {len(all_reviews)} / {TARGET} reviews", end="\r")

            if len(all_reviews) % 500 < 25 and len(all_reviews) > 0:
                save_csv(all_reviews, "stranger_things_reviews_partial.csv")

            clicked = click_load_more(driver)
            if not clicked:
                print(f"\n  No more 'Load More' button.")
                break

            if new == 0:
                no_new_count += 1
                if no_new_count >= 3:
                    print("\n  No new reviews loading, stopping.")
                    break
            else:
                no_new_count = 0

            time.sleep(random.uniform(1.5, 3.0))

    finally:
        driver.quit()

    print(f"\nTotal scraped: {len(all_reviews)}")

    if not all_reviews:
        print("No reviews found.")
        return

    save_csv(all_reviews, "stranger_things_reviews.csv")

    df = pd.DataFrame(all_reviews)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    print("\n-- Rating distribution --")
    print(df["rating"].value_counts().sort_index().to_string())
    print("\nDone!")


if __name__ == "__main__":
    main()
