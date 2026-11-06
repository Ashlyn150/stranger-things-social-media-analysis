# 🎬 Stranger Things Social Media Analysis

## 📌 Overview

This project analyses audience sentiment, discussion themes, and engagement patterns across different seasons of *Stranger Things* using Reddit and IMDb data.

The project was completed as part of the **Social Media Analysis** module in the MSc Business Analytics programme at Trinity College Dublin.

Beyond measuring audience sentiment, the project explores how social media analytics can reduce creative and commercial **“guesswork”** by connecting audience reactions with content decisions, promotional opportunities, and character-level commercial potential.

The analysis combines sentiment analysis, keyword analysis, LDA topic modelling, audience engagement analysis, character-level analysis, and brand matchmaking.

---

## 🎯 Objectives

The project focuses on questions such as:

- How did audience sentiment change across different seasons?
- Which seasons generated the strongest audience buzz and engagement?
- What topics and keywords appeared most frequently in audience discussions?
- Which characters attracted the most attention?
- What recurring themes emerged from Reddit and IMDb text data?
- How can audience insights support content, promotion, and commercial decision-making?

---

## 🎥 Two Analytical Lenses

### 1. Content Creation

The analysis examines which narratives, characters, and themes resonate most strongly with audiences and whether audience discussion can help identify potential creative risks or opportunities.

### 2. Marketing & Commercial Value

The project also explores which characters and moments generate disproportionate social buzz, and whether sentiment and discussion patterns can help inform promotional focus and potential brand partnerships.

---

## 📊 Data Sources

- **Reddit** — audience discussions and comments related to *Stranger Things*
- **IMDb** — audience reviews, ratings, and related review information

The repository includes data collection scripts as well as processed datasets used in the analysis.

> Note: Data files are included for academic and portfolio demonstration purposes. Any platform-specific usage requirements should be respected when reusing the data.

---

## 🧠 Analytical Methods

- Data cleaning and preprocessing
- Data merging and transformation
- Exploratory data analysis
- Rating vs. social buzz comparison
- Sentiment polarity analysis
- Keyword and frequency analysis
- LDA topic modelling
- Character-level analysis
- Brand matchmaking and business interpretation
- Data visualisation
- Cross-season comparison

---

## 🔍 Analysis Workflow

### 1. Data Collection

IMDb and Reddit data were collected using dedicated scraping / extraction scripts.

Files:
- `data_collection/imdb_scraper.py`
- `data_collection/reddit_scraper.ipynb`

### 2. Data Cleaning and Integration

Raw and intermediate datasets were cleaned and merged into a combined analysis dataset.

File:
- `analysis/01_data_cleaning_merge.py`

### 3. Rating vs. Social Buzz

IMDb ratings were compared with a composite **Social Buzz Index** based on review volume and engagement. The analysis explored whether highly rated seasons necessarily generated the strongest audience discussion.

File:
- `analysis/02_rating_vs_buzz.ipynb`

### 4. Sentiment Analysis

Audience text was analysed to identify positive, negative, and neutral sentiment patterns and compare reactions across seasons.

File:
- `analysis/03_sentiment_polarity.ipynb`

### 5. Topic Modelling

LDA topic modelling was used to identify recurring themes within audience discussions and interpret the main subjects driving conversation.

File:
- `analysis/04_lda_topic_modeling.ipynb`

### 6. Keyword Analysis

Frequently occurring words and terms were analysed to identify prominent discussion themes, season-specific signals, and audience interests.

File:
- `analysis/05_keywords.ipynb`

### 7. Character Analysis

Character-related discussion patterns were explored to understand which characters attracted the most attention and how character-level engagement changed over time.

File:
- `analysis/06_character_analysis.ipynb`

### 8. Brand Matchmaking

Audience and character insights were extended into a brand-matching exercise to demonstrate how social media analytics can support marketing and commercial interpretation.

File:
- `analysis/07_brand_matchmaking.ipynb`

---

## 💡 Key Takeaways

The project shows how unstructured social media and review data can be transformed into structured audience insights.

Rather than relying only on overall ratings, the analysis examines **why** audience reactions differ by looking at sentiment, discussion volume, recurring topics, keywords, and character-level engagement.

The findings demonstrate how audience analytics can support:

- **Creative risk mitigation** — identifying narrative elements, character arcs, and themes that resonate with audiences.
- **Promotional prioritisation** — using social buzz and discussion signals to identify high-interest characters, scenes, or themes for campaign focus.
- **Strategic IP development** — using long-term engagement patterns to assess which elements of an entertainment franchise may have sustained audience value.
- **Commercial and brand opportunities** — using character- and topic-level signals as a starting point for potential brand partnership evaluation.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Natural Language Processing (NLP)
- Sentiment Analysis
- LDA Topic Modelling
- Exploratory Data Analysis
- Data Visualisation
- Reddit data
- IMDb data
- Git / GitHub

---

## 📁 Repository Structure

```text
stranger-things-social-media-analysis/
│
├── README.md
│
├── data/
│   ├── combined_data.csv
│   ├── stranger_things_reddit.csv
│   └── stranger_things_reviews.csv
│
├── data_collection/
│   ├── imdb_scraper.py
│   └── reddit_scraper.ipynb
│
├── analysis/
│   ├── 01_data_cleaning_merge.py
│   ├── 02_rating_vs_buzz.ipynb
│   ├── 03_sentiment_polarity.ipynb
│   ├── 04_lda_topic_modeling.ipynb
│   ├── 05_keywords.ipynb
│   ├── 06_character_analysis.ipynb
│   └── 07_brand_matchmaking.ipynb
│
├── presentation/
│   └── Stranger_Things_Social_Media_Analysis.pdf
│
└── requirements.txt
```

---

## 🎓 Academic Context

This project was completed as a **group project** for the Social Media Analysis module within the MSc Business Analytics programme at Trinity College Dublin.

The project brief required teams to:

- define a problem statement,
- apply text or image analytics techniques,
- explain the data and analytical approach,
- interpret results critically,
- and translate findings into business implications.

The final deliverable was presented as a group presentation.

---

## 👤 My Contribution

This was completed as a university group project.

My contribution included participation in the analytical workflow, interpretation of social media data, development of insights, and presentation of findings.

---

## ⚠️ Limitations

- Social media users may not represent the full *Stranger Things* audience.
- Reddit discussions may be influenced by highly active communities or specific events.
- Sentiment models may not fully capture sarcasm, humour, or context.
- Topic modelling requires human interpretation when assigning meaning to generated topics.
- IMDb ratings and Reddit discussions represent different forms of audience engagement and should not be treated as directly equivalent measures.

---

## 📎 Presentation

A PDF version of the final project presentation is included in the `presentation/` folder for a concise overview of the project story, analysis, findings, and business implications.

---

## 👩‍💻 Author

**Bingbing (Ashlyn) Lin**  
MSc Business Analytics, Trinity College Dublin  
GitHub: [Ashlyn150](https://github.com/Ashlyn150)
