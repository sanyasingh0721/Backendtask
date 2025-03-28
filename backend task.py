import requests
import csv
import argparse
import sys
from typing import List, Dict

def fetch_pubmed_papers(query: str) -> List[Dict[str, str]]:
    """
    Fetch research papers from PubMed API based on the given query.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 50  # Limit results for testing
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    
    return fetch_paper_details(paper_ids) if paper_ids else []

def fetch_paper_details(paper_ids: List[str]) -> List[Dict[str, str]]:
    """
    Fetch detailed paper information using PubMed's ESummary API.
    """
    if not paper_ids:
        return []
    
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    data = response.json().get("result", {})
    papers = []
    
    for paper_id in paper_ids:
        paper = data.get(paper_id, {})
        papers.append({
            "PubmedID": paper.get("uid", "N/A"),
            "Title": paper.get("title", "N/A"),
            "Publication Date": paper.get("pubdate", "N/A"),
            "Non-academic Author(s)": "N/A",  # Placeholder
            "Company Affiliation(s)": "N/A",  # Placeholder
            "Corresponding Author Email": "N/A"  # Placeholder
        })
    
    return papers

def save_to_csv(papers: List[Dict[str, str]], filename: str) -> None:
    """
    Save paper details to a CSV file.
    """
    if not papers:
        print("No papers to save.")
        return
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=papers[0].keys())
        writer.writeheader()
        writer.writerows(papers)

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers based on a query.")
    parser.add_argument("query", type=str, nargs="?", help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    
    if args.query is None:
        args.query = "cancer treatment"  # Provide a default query instead of exiting
    
    papers = fetch_pubmed_papers(args.query)
    
    if args.debug:
        print("Fetched Papers:", papers)
    
    if args.file:
        save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        print(papers)

if __name__ == "__main__":
    main()
