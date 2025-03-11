import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Tools.scrape_tool import scrape_tool
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="deepseek-r1-distill-llama-70b")


Scraper = create_react_agent(
    model=model,
    tools=[scrape_tool],
    name="scraper",
    prompt="أنت مُجمع الأخبار، المسؤول عن استخراج آخر مقالات أخبار كرة القدم التونسية من MosaiqueFM باستخدام أداة التجميع (Scraping). "
           "هدفك هو جمع بيانات إخبارية منظمة وعالية الجودة وذات صلة مع التأكد من أن المحتوى مُنسق بشكل صحيح للمعالجة اللاحقة."
)




res = Scraper.invoke({"messages": [("human", "do your job")]})
print(res["messages"][-1].pretty_print())