# AI Web Scraper ✨

## Overview
AI Web Scraper is an intelligent, user-friendly web scraping tool that leverages LLMs (Large Language Models) to extract structured data from any website. With a simple Streamlit interface, users can scrape, parse, and download data in tabular or JSON format—no coding required.

## Features
- **No-Code Web Scraping:** Scrape any website by simply entering its URL.
- **AI-Powered Parsing:** Use natural language to describe what you want to extract, and define your desired JSON structure.
- **Flexible Output:** View results as a table, download as CSV (via Streamlit), or download as JSON.
- **Customizable Extraction:** Supports custom parsing instructions and output formats.
- **Credential Management:** Securely provide your API keys and WebDriver URL via the UI or environment variables.
- **Error Handling:** Friendly error messages for missing or invalid credentials.
- **Session State:** Keeps your data and results available throughout your session.

## Tech Stack
- **Python**
- **Streamlit** (UI)
- **Selenium** (Web scraping automation)
- **BeautifulSoup** (HTML parsing and cleaning)
- **LangChain** & **LangChain Groq** (LLM orchestration)
- **GROQ LLM API** (for AI-powered parsing)
- **Bright Data WebDriver** (for robust browser automation)
- **python-dotenv** (for environment variable management)

## How It Works
1. **Credential Input:**
   - Enter your GROQ API Key and SBR WebDriver URL in the sidebar, or set them as environment variables.
   - The app checks for these credentials before allowing scraping or parsing.

2. **Scraping:**
   - Enter the target website URL and click "Scrape Website".
   - The app uses Selenium (with Bright Data WebDriver) to fetch and render the page, handling captchas if present.
   - Extracts and cleans the main content using BeautifulSoup.

3. **Parsing:**
   - Describe what you want to extract (e.g., "List all product names and prices") and provide a sample JSON structure.
   - The app splits the content if needed and sends it to the GROQ LLM via LangChain for intelligent extraction.
   - The LLM returns structured data matching your instructions.

4. **Viewing & Downloading:**
   - Results are shown in a table (if possible) for easy review.
   - Download your data as JSON (custom button) or CSV (Streamlit's built-in feature).

5. **Saving Results:**
   - Optionally, select a folder and filename to save your parsed results as a JSON file.

## Main Files & Modules
- `main.py` — Streamlit UI, user flow, and session management.
- `scrape.py` — Web scraping logic (Selenium, BeautifulSoup, content cleaning).
- `parse.py` — LLM-powered parsing and formatting (LangChain, Groq API).

## Usage Scenarios
- **Market Research:** Extract product listings, prices, and images from e-commerce sites.
- **Movie/Media Data:** Scrape movie names, release dates, and thumbnails from review sites.
- **Custom Data Mining:** Use natural language to extract any structured data from arbitrary web pages.

## Why Use This Project?
- **No coding required:** Everything is handled via a simple web UI.
- **AI-powered:** Get structured data from even complex or messy web pages.
- **Flexible and secure:** Credentials are never hardcoded and can be managed securely.
- **Open and extensible:** Easily adapt or extend for your own scraping and parsing needs.

---

*For setup and installation instructions, see the separate `SETUP.md` file.* 