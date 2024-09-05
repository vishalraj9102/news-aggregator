import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape articles from BBC (example)
def scrape_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    article_id = 0  # Initialize article ID

    for article in soup.find_all("a", class_="gs-c-promo-heading"):
        title = article.text
        link = "https://www.bbc.com" + article['href']
        pub_date = time.strftime("%Y-%m-%d")  # Use current date for simplicity
        articles.append([article_id, title, "", pub_date, "BBC", link])
        article_id += 1  # Increment article ID

    return articles

# Function to save articles to CSV
def save_to_csv(articles, filename="news_articles.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Summary", "Publication Date", "Source", "URL"])
        writer.writerows(articles)

if __name__ == "__main__":
    bbc_articles = scrape_bbc()
    save_to_csv(bbc_articles)
    print("Articles scraped and saved.")
