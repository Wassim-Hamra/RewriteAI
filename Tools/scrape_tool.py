from datetime import datetime, timedelta
from langchain_core.tools import tool
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from States.states import News

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




def get_news(xpath_template, div_num):
    wait = WebDriverWait(driver, 20)
    menu_item = wait.until(EC.element_to_be_clickable(
        (By.XPATH, xpath_template.format(div_num))))
    date_template = '//*[@id="__next"]/div[1]/main/section[2]/div/div/div[1]/div[1]/div[{}]/div/div/div[2]/time'
    date = wait.until(
        EC.presence_of_element_located((By.XPATH, date_template.format(div_num))))
    date = date.text.split(" ")[0]
    date_object = datetime.strptime(date, "%Y/%m/%d").date()
    two_days_from_today = datetime.today().date() - timedelta(days=5)
    is_match = date_object > two_days_from_today
    if is_match:
        driver.execute_script("arguments[0].click();", menu_item)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div[1]/main/section[2]/div/div/div[1]/div[1]/article/span')))
        news_title = driver.title.split(" | ")[0]
        sleep(1)
        p_tags = driver.find_elements(By.TAG_NAME, "p")
        content = ''
        for p in p_tags:
            content += p.text + "\n"
        newsClass = News(news_title, content)
        newsList.append(newsClass)
        print(newsClass)
    driver.back()
    wait.until(
        EC.presence_of_element_located((By.XPATH, xpath_template.format(div_num+1))))



newsList = []
def scrape_tool():
    """
    A tool that scrapes the latest Tunisian football news articles from the website mosaiqueFM.
    """

    url = "https://www.mosaiquefm.net/ar/actualites/%D8%A7%D9%84%D8%B1%D8%A7%D8%A8%D8%B7%D8%A9-%D8%A7%D9%84%D8%A3%D9%88%D9%84%D9%89-%D9%83%D8%B1%D8%A9-%D9%82%D8%AF%D9%85/17"
    driver.get(url)
    sleep(2)
    xpath_template = '//*[@id="__next"]/div[1]/main/section[2]/div/div/div[1]/div[1]/div[{}]/div/figure/a'
    global newsList
    for div_num in range(1, 7):
        get_news(xpath_template, div_num)
    driver.quit()
    return newsList



