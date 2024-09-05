import csv
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def categorize_article(title, summary):
    # Simplified categorization logic based on keywords
    doc = nlp(title + summary)
    if "technology" in doc.text.lower():
        return "Technology"
    elif "politics" in doc.text.lower():
        return "Politics"
    else:
        return "General"

def categorize_articles(filename="news_articles.csv"):
    articles = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            title, summary, pub_date, source, url = row
            category = categorize_article(title, summary)
            articles.append([title, summary, pub_date, source, url, category])

    # Write updated articles with category to the same CSV file
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Summary", "Publication Date", "Source", "URL", "Category"])
        writer.writerows(articles)

if __name__ == "__main__":
    categorize_articles()
    print("Articles categorized and saved.")
