from tools.arxiv_tool import search_papers
from tools.news_tool import news_search
from tools.github_tool import search_repos


def search_tools(topic):
    research_papers = search_papers(topic)
    repo_papers = search_repos(topic)
    news_papers = news_search(topic)
    results = {
        "papers": research_papers,
        "repos": repo_papers,
        "news": news_papers
    }
    return results

def format_results(results):
    papers = "PAPERS:\n"
    for paper in results["papers"]:
        papers += paper.get("Title", "") + "\n"
        papers += paper.get("Links", "") + "\n\n"

    repos = "REPOS:\n"
    for repo in results["repos"]:
        repos += repo.get("name", "") + "\n"
        repos += str(repo.get("stars", "")) + "\n"
        repos += (repo.get("description") or "") + "\n"
        repos += repo.get("url", "") + "\n\n"

    news = "NEWS:\n"
    for article in results["news"]:
        news += article.get("title", "") + "\n"
        news += (article.get("description") or "") + "\n"
        news += article.get("source", "") + "\n\n"
        
    final_text = papers + news + repos

    return final_text

results = search_tools("Quantum Computing")
print(format_results(results))