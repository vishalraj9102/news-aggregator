# 📚 Personalized News Aggregator

Welcome to the Personalized News Aggregator! This project scrapes news articles from multiple sources, categorizes them, and provides access via a REST API and a simple front-end interface.

## 🚀 Getting Started

These instructions will help you set up and run the project locally.

### 🛠️ Prerequisites

Make sure you have the following installed:

- [Python 3.12+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

### 📦 Installing

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/news-aggregator.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd news-aggregator
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

### 🧩 Usage

1. **Run the scraper:**

   This will scrape articles and save them to `news_articles.csv`.

   ```bash
   python scraper.py
   ```

2. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API:**

   - **Get all articles:** `http://127.0.0.1:8000/articles`
   - **Get article by ID:** `http://127.0.0.1:8000/articles/{id}`
   - **Search articles:** `http://127.0.0.1:8000/search?keyword={keyword}`

### 🌐 Front-End

Visit `http://127.0.0.1:8000` to see the front-end interface (if applicable).

## 🔍 API Endpoints

### `/articles`

- **GET**: Retrieve all articles.
- **Query Parameters**: `category` (optional) - Filter by article category.

### `/articles/{id}`

- **GET**: Retrieve a specific article by its ID.

### `/search`

- **GET**: Search for articles by keyword.
- **Query Parameters**: `keyword` - Keyword to search in article titles.

## 📝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**
3. **Commit your changes**
4. **Push to the branch**
5. **Open a pull request**

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [FastAPI](https://fastapi.tiangolo.com/)

## 📧 Contact

For questions, please reach out to (vishalrajmehra95@gmail.com).

---

Thank you for checking out the Personalized News Aggregator! 🚀
