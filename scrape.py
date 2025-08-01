from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup


def scrape_website(website, SBR_WEBDRIVER):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # Clean content
    for tag in soup.find_all(['header', 'footer']):
        tag.decompose()
    for tag in soup.find_all(attrs={"class": lambda x: x and ("header" in x or "footer" in x)}):
        tag.decompose()
    for tag in soup.find_all(attrs={"id": lambda x: x and ("header" in x or "footer" in x)}):
        tag.decompose()

    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    
    for tag in soup.find_all(lambda tag: tag.has_attr('src') or tag.has_attr('data-src')):
        alt = tag.get("alt") or tag.get("aria-label") or tag.get_text(strip=True)
        src = tag.get("src") or tag.get("data-src")
        if alt and src:
            replacement = f"[IMAGE: {alt} | {src}]"
        elif src:
            replacement = f"[IMAGE: {src}]"
        else:
            replacement = "[IMAGE]"
        tag.replace_with(replacement)

    
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href")
        if href:
            replacement = f"{text} ({href})"
        else:
            replacement = text
        a.replace_with(replacement)

    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=60000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]