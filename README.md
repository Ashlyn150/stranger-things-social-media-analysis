# 🎬 Stranger Things Social Media Analysis

## 📌 Overview

This project analyses audience sentiment, discussion themes, and engagement patterns across different seasons of *Stranger Things* using Reddit and IMDb data.

The project was completed as part of the **Social Media Analysis** module in the MSc Business Analytics programme at Trinity College Dublin. The coursework required the use of intensive text analytics or image analysis techniques to generate business-relevant insights from social media data.

The analysis combines sentiment analysis, keyword analysis, LDA topic modelling, audience engagement analysis, character-level analysis, and brand matchmaking to explore how audience perception and discussion evolved across seasons.

## 🎯 Objectives

- How did audience sentiment change across different seasons?
- Which seasons generated the strongest audience buzz and engagement?
- What topics and keywords appeared most frequently in audience discussions?
- Which characters attracted the most attention?
- What recurring themes emerged from Reddit and IMDb text data?
- How can audience insights be translated into potential brand or marketing opportunities?

## 📊 Data Sources

- **Reddit** — audience discussions and comments related to *Stranger Things*
- **IMDb** — audience reviews, ratings, and related review information

The repository includes data collection scripts as well as processed datasets used in the analysis.

> Note: Data files are included for academic and portfolio demonstration purposes. Any platform-specific usage requirements should be respected when reusing the data.

## 🧠 Analytical Methods

- Data cleaning and preprocessing
- Data merging and transformation
- Exploratory data analysis
- Rating vs. buzz comparison
- Sentiment polarity analysis
- Keyword and frequency analysis
- LDA topic modelling
- Character-level analysis
- Brand matchmaking and business interpretation
- Data visualisation
- Cross-season comparison

## 🔍 Analysis Workflow

### 1. Data Collection
Files:
- `data_collection/imdb_scraper.py`
- `data_collection/reddit_scraper.ipynb`

### 2. Data Cleaning and Integration
File:
- `analysis/01_data_cleaning_merge.py`

### 3. Rating vs. Buzz Analysis
File:
- `analysis/02_rating_vs_buzz.ipynb`

### 4. Sentiment Analysis
File:
- `analysis/03_sentiment_polarity.ipynb`

### 5. Topic Modelling
File:
- `analysis/04_lda_topic_modeling.ipynb`

### 6. Keyword Analysis
File:
- `analysis/05_keywords.ipynb`

### 7. Character Analysis
File:
- `analysis/06_character_analysis.ipynb`

### 8. Brand Matchmaking
File:
- `analysis/07_brand_matchmaking.ipynb`

## 💡 Key Takeaway

This project demonstrates how unstructured social media and review data can be transformed into structured audience insights.

Rather than relying only on ratings, the analysis explores **why** audience reactions differ by examining sentiment, discussion volume, recurring topics, keywords, and character-level engagement.

It also shows how social media analytics can move beyond descriptive analysis toward business interpretation and marketing applications.

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

## 🎓 Academic Context

This project was completed as a **group project** for the Social Media Analysis module within the MSc Business Analytics programme at Trinity College Dublin.

The project brief required teams to:
- define a problem statement,
- apply text or image analytics techniques,
- explain the data and analytical approach,
- interpret results critically,
- and translate findings into business implications.

The final deliverable was presented as a group presentation.

## 👤 My Contribution

This repository is used as a portfolio representation of the group project.

My contribution included participation in the analytical workflow, interpretation of social media data, development of insights, and presentation of findings.

> This section can be updated later with a more detailed breakdown of individual responsibilities.

## ⚠️ Limitations

- Social media users may not represent the full *Stranger Things* audience.
- Reddit discussions may be influenced by highly active communities or specific events.
- Sentiment models may not fully capture sarcasm, humour, or context.
- Topic modelling requires human interpretation when assigning meaning to generated topics.
- IMDb ratings and Reddit discussions represent different forms of audience engagement and should not be treated as directly equivalent measures.

## 📎 Presentation

A PDF version of the final project presentation is included in the `presentation/` folder for a concise overview of the project story, analysis, findings, and business implications.

## 👩‍💻 Author

**Bingbing (Ashlyn) Lin**  
MSc Business Analytics, Trinity College Dublin  
GitHub: [Ashlyn150](https://github.com/Ashlyn150)
