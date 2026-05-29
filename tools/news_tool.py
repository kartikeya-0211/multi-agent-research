from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta

load_dotenv()

thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

def news_search(topic):
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": topic,
            "from": thirty_days_ago,
            "sortBy":"relevancy",
            "pageSize":5,
            "apiKey": os.getenv("NEWS_API_KEY")
        }

        response = requests.get(url,params=params)
        data = response.json()

        results = []
        for news in data["articles"]:
            results.append({
                "source": news["source"]["name"],
                "url": news["url"],
                "title": news["title"],
                "description": news["description"]
            })
        return results
    except Exception as e:
        return []
    