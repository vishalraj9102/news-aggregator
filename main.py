from fastapi import FastAPI, HTTPException
import csv

app = FastAPI()

# Load articles from CSV
def load_articles(filename="news_articles.csv"):
    articles = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            articles.append(row)
    return articles

articles = load_articles()

# Get all articles
@app.get("/articles")
def get_articles(category: str = None):
    if category:
        return [article for article in articles if article["Category"] == category]
    return articles

# Get article by id
@app.get("/articles/{id}")
def get_article(id: int):
    if id < 0 or id >= len(articles):
        raise HTTPException(status_code=404, detail="Article not found")
    return articles[id]

# Search for articles by keyword
@app.get("/search")
def search_articles(keyword: str):
    return [article for article in articles if keyword.lower() in article["Title"].lower()]
