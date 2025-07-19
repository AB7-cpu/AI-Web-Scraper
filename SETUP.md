# Setup Guide for AI Web Scraper

Follow these steps to run the AI Web Scraper on your local machine.

---

## 1. Prerequisites
- **Python 3.8+** (Recommended: Python 3.10 or newer)
- **pip** (Python package manager)
- **Google Chrome** (for Selenium WebDriver)
- **Bright Data account** (for SBR WebDriver URL)
- **GROQ account** (for LLM API key)

---

## 2. Clone the Repository
```sh
git clone https://github.com/AB7-cpu/AI-Web-Scraper.git
cd AI-Web-Scraper
```

---

## 3. Create a Virtual Environment (Recommended)
```sh
#Create the environment:
#On Windows:
python -m venv .venv
#On Mac/Linux:
python3 venv .venv

# Activate the environment:
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

---

## 4. Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 5. Set Up Environment Variables
Create a `.env` file in the project root with the following content:

```
GROQ_API_KEY=your_groq_api_key_here
SBR_WEBDRIVER=your_bright_data_webdriver_url_here
```

- **GROQ_API_KEY:** Get this from your [GROQ dashboard](https://console.groq.com/).
- **SBR_WEBDRIVER:** Get this from your [Bright Data account](https://brightdata.com/), add browser api and copy the url for selenium.

> **Note:** You can also enter these values in the Streamlit sidebar UI at runtime if you prefer not to use a `.env` file.

---

## 6. Run the App
```sh
streamlit run main.py
```

- The app will open in your browser (usually at http://localhost:8501).
- Enter your credentials (if not set in `.env`), the website URL, and follow the UI.

---

## 7. Using the App
- **Scrape Website:** Enter a URL and click the button to fetch and clean the page content.
- **Parse Content:** Describe what you want to extract and provide a sample JSON structure.
- **View/Download:** See results in a table, download as CSV or JSON, or save to a folder.

---

## 8. Troubleshooting
- **Missing API Key or WebDriver URL:**
  - The app will show an error if these are not set.
  - Double-check your `.env` file or sidebar inputs.
- **Invalid Credentials:**
  - If you enter an invalid key or URL, the app will display a clear error message.
- **Selenium/Browser Issues:**
  - Make sure Google Chrome is installed and up to date.
  - The Bright Data WebDriver URL must be valid and active.
- **Other Errors:**
  - Check the terminal for error logs.
  - Ensure all dependencies are installed and your Python version is compatible.

---

## 9. Updating Dependencies
If you update `requirements.txt`, run:
```sh
pip install -r requirements.txt
```

---

## 10. Deactivating the Virtual Environment
When done, you can deactivate with:
```sh
deactivate
```

---

**You're all set! Enjoy scraping and parsing with AI Web Scraper.** 