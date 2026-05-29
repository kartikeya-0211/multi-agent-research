from tools.arxiv_tool import search_papers
from tools.news_tool import news_search
from tools.github_tool import search_repos


def search_tools(topic,user_input):
    results = {
        "papers": [],
        "repos": [],
        "news": []
    }
    if "news" in user_input:
        results["news"] = news_search(topic)
    elif "repos" in user_input:
        results["repos"] = search_repos(topic)
    elif "papers" in user_input:
        results["papers"] = search_papers(topic)
    else:
        results['news'] = news_search(topic)
        results['papers'] = search_papers(topic)
        results['repos'] = search_repos(topic)

    return results

def format_results(results):
    papers = 'PAPERS:\n'
    for paper in results["papers"]:
        papers += f"- Title: {paper.get('Title', '')}\n"
        papers += f"  Links: {paper.get('Links', '')}\n\n"

    repos = "REPOS:\n"
    for repo in results["repos"]:
        repos += f"- Name: {repo.get('name', '')}\n"
        repos += f"- Stars: {str(repo.get('stars', ''))}\n"
        repos += f"- Description: {(repo.get('description') or '')}\n"
        repos += f"- URL: {repo.get('url', '')}\n\n"

    news = "NEWS:\n"
    for article in results["news"]:
        news += f"- Title: {article['title']}\n"
        news += f"- Description: {article.get('description') or 'N/A'}\n"
        news += f"- Source: {article['source']}\n\n"
        
    final_text = papers + news + repos

    return final_text