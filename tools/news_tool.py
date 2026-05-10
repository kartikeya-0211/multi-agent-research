from dotenv import load_dotenv
import os
import requests

load_dotenv()

def news_search(topic):
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": topic,
            "from": "2026-04-09",
            "sortBy":"popularity",
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
    