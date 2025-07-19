import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_groq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="AI Web Scraper", layout='centered')
st.title('AI Web Scraper ✨')
st.sidebar.title('Scraper settings')

groq_api_key = st.sidebar.text_input("Enter GROQ API Key", type="password")
sbr_webdriver = st.sidebar.text_input("Enter SBR WebDriver URL", type="password")

# Fallback to .env if not provided
if not groq_api_key:
    groq_api_key = os.getenv("GROQ_API_KEY")
if not sbr_webdriver:
    sbr_webdriver = os.getenv("SBR_WEBDRIVER")

# Error if missing
if not groq_api_key:
    st.sidebar.error("Please provide the GROQ API Key in the sidebar or set it in the .env file.")
if not sbr_webdriver:
    st.sidebar.error("Please provide the SBR WebDriver URL in the sidebar or set it in the .env file.")


if groq_api_key and sbr_webdriver:
    url = st.sidebar.text_input("Enter Website URL")

    #Scrape the Website
    if st.sidebar.button("Scrape Website"):
        if url:
            st.sidebar.write("Scraping the website...")
            st.spinner(text="Hangon website is begin scraped...")

            try:
                # Scrape the website (pass sbr_webdriver)
                web_content = scrape_website(url, sbr_webdriver)
                body_content = extract_body_content(web_content)
                cleaned_content = clean_body_content(body_content)

                # Store the Web content in Streamlit session state
                st.session_state.web_content = cleaned_content

                # Display the Web content in an expandable text box
                with st.expander("View Content"):
                    st.text_area("Extracted Content", cleaned_content, height=300)
            except Exception as e:
                st.error(f"Failed to scrape website. Please check your SBR WebDriver URL and try again. Error: {e}")

    #Describe Scraping content and structure
    if "web_content" in st.session_state:
        parse_description = st.sidebar.text_area("Describe what you want to parse")
        parse_structure = st.sidebar.text_area("Your json structure here...")

        if st.sidebar.button("Parse Content"):
            if parse_description:
                st.sidebar.write("Parsing the content...")
                st.spinner(text="Parsing your request...")

                try:
                    # Parse the content with Groq (pass groq_api_key)
                    dom_chunks = split_dom_content(st.session_state.web_content)
                    parsed_result = parse_with_groq(dom_chunks, parse_description, parse_structure, groq_api_key)
                    st.session_state.parsed_result = parsed_result
                    import json
                    try:
                        data = json.loads(parsed_result)
                        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                            st.dataframe(data)
                        elif isinstance(data, dict):
                            st.dataframe([data])
                        else:
                            st.write(data)
                        
                        download_key = "download_json_clicked"
                        def on_download():
                            st.session_state[download_key] = True

                        st.download_button(
                            label="Download JSON",
                            data=json.dumps(data, ensure_ascii=False, indent=2),
                            file_name="parsed_result.json",
                            mime="application/json",
                            on_click=on_download
                        )
                        if st.session_state.get(download_key):
                            st.success("JSON file downloaded successfully!")
                    except Exception:
                        st.write(parsed_result)
                except Exception as e:
                    st.error(f"Failed to parse content. Please check your GROQ API Key and try again. Error: {e}")