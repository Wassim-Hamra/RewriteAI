from ..Tools.scrape_tool import scrape_tool

from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="deepseek-r1-distill-llama-70b")


math_agent = create_react_agent(
    model=model,
    tools=[scrape_tool],
    name="scraper",
    prompt="You are the News Scraper, responsible for extracting the latest Tunisian football news articles from specified sources using the scraping tool."
           "Your goal is to gather structured, high-quality, and relevant news data while ensuring that the content is properly formatted for further processing."
)