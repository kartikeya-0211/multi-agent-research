import requests

def search_repos(topic):
    try:
        url = "https://api.github.com/search/repositories"
        params = {
            "q": topic,
            "sort" : "stars",
            "per_page" : 5
        } 

        response = requests.get(url,params=params)
        data = response.json()
        results = []
        for repo in data["items"]:
            results.append({
                "name": repo["name"],
                "url": repo["html_url"],
                "stars": repo["stargazers_count"],
                "description": repo["description"]
            })
        return results
    except Exception as e:
        return []
