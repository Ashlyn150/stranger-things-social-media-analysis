# Stranger Things Social Media Analysis

## Overview

This project analyses audience sentiment and discussion themes across different seasons of *Stranger Things* using social media and review data from Reddit and IMDb.

The aim was to understand how audience perception changed over time, identify the topics viewers discussed most frequently, and compare sentiment patterns across seasons. The project combines text analytics, sentiment analysis, keyword extraction, topic modelling, and data visualisation to turn unstructured audience feedback into clear insights.

## Objectives

The analysis focused on questions such as:

- How did audience sentiment change across different seasons of *Stranger Things*?
- Which topics and themes appeared most frequently in online discussions?
- Which seasons received the strongest or weakest audience reactions?
- How did audience discussions evolve as the series progressed?
- What insights can be extracted from large volumes of unstructured social media text?

## Data Sources

- **Reddit** — audience discussions and comments related to *Stranger Things*
- **IMDb** — audience ratings and review-related information

> Note: Raw data may not be included in this repository due to platform terms, privacy considerations, or file-size limitations.

## Methods

The project applied a range of text analytics and NLP techniques, including:

- Data cleaning and text preprocessing
- Sentiment analysis
- Keyword and frequency analysis
- Season-level comparison
- LDA topic modelling
- Topic interpretation
- Data visualisation
- Audience insight generation

## Analytical Approach

### 1. Data Preparation

Text data was cleaned and prepared for analysis by removing irrelevant content and standardising text for downstream NLP tasks.

### 2. Sentiment Analysis

Audience comments and reviews were analysed to identify positive, negative, and neutral sentiment patterns.

The results were compared across seasons to understand changes in audience perception over time.

### 3. Keyword Analysis

Frequently occurring words and discussion terms were examined to identify the subjects receiving the most audience attention.

### 4. Topic Modelling

Latent Dirichlet Allocation (LDA) was used to identify recurring topics within audience discussions.

The resulting topics were interpreted in the context of the series to understand the main themes driving online conversation.

### 5. Cross-Season Comparison

Sentiment, topics, and audience reactions were compared across seasons to identify changes in reputation and discussion patterns.

## Key Takeaway

The project demonstrates how unstructured social media and review data can be transformed into structured audience insights using NLP and statistical text analysis.

Rather than relying only on overall ratings, the analysis explores *why* audience reactions differ by examining sentiment and recurring discussion themes.

## Tech Stack

- Python
- Pandas
- NumPy
- Natural Language Processing (NLP)
- Sentiment Analysis
- LDA Topic Modelling
- Data Visualisation
- Reddit data
- IMDb data

## Repository Structure

```text
stranger-things-social-media-analysis/
│
├── README.md
├── data/
│   └── README.md
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_sentiment_analysis.ipynb
│   └── 03_topic_modelling.ipynb
├── visuals/
│   └── project_visualisations/
└── requirements.txt
```

The exact structure may vary depending on the final version of the project files.

## My Contribution

This was completed as part of a university group project for Social Media Analysis.

My work contributed to the analytical workflow, interpretation of audience data, and development of insights from social media analysis.

> Update this section before publishing if you want to describe your individual contribution in more detail.

## Skills Demonstrated

- NLP and text analytics
- Sentiment analysis
- Topic modelling
- Working with unstructured data
- Exploratory data analysis
- Data visualisation
- Translating analytical results into business-style insights
- Communicating findings to non-technical audiences

## Limitations

- Social media users may not represent the full *Stranger Things* audience.
- Online sentiment can be influenced by highly active users or specific events.
- Topic modelling requires human interpretation when assigning meaning to topics.
- Sentiment models may not always capture sarcasm, humour, or context accurately.

## Academic Context

This project was completed as part of the MSc Business Analytics programme at Trinity College Dublin.

## Author

**Bingbing (Ashlyn) Lin**  
MSc Business Analytics, Trinity College Dublin  
[LinkedIn](#) | [GitHub](#)
