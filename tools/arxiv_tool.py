import arxiv 

client = arxiv.Client()
def search_papers(topic):
    try:
        search = arxiv.Search(
            query=topic,
            max_results=5
            )
        papers = []
        for result in client.results(search):
            paper={"Title": result.title, "Links": result.entry_id}
            papers.append(paper)
        return papers
    except Exception as e:
            return []