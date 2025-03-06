from langchain_core.tools import tool
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to Brave browser binary
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Configure ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path  # Set Brave as the browser
chrome_options.add_argument("--headless")  # Optional: Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Use ChromeDriverManager without 'version' in the init
driver = webdriver.Chrome(service=Service(r"C:\Users\Public\Documents\RewriteAI\Extra\chromedriver-win32\chromedriver.exe"), options=chrome_options)

@tool
def scrape_tool():
    """
    A tool that scrapes the latest Tunisian football news articles from the website mosaiqueFM.
    """

    url = "https://www.mosaiquefm.net/ar/actualites/%D8%A7%D9%84%D8%B1%D8%A7%D8%A8%D8%B7%D8%A9-%D8%A7%D9%84%D8%A3%D9%88%D9%84%D9%89-%D9%83%D8%B1%D8%A9-%D9%82%D8%AF%D9%85/17"
    driver.get(url)


    title = driver.title
    driver.quit()
    return title







print(scrape_tool())