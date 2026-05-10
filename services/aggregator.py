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


results = search_tools("Quantum Computing")
print(format_results(results))