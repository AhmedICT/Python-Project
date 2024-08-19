import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_absolute(url):
    """Check if a URL is absolute."""
    return bool(urlparse(url).netloc)

def get_links(url, html):
    """Extract all links from the HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            href = href.strip()
            if is_absolute(href):
                links.append(href)
            else:
                links.append(urljoin(url, href))
    return links

def crawl(url, max_depth=3, current_depth=0, visited=None):
    """Recursively crawl a webpage and its linked pages."""
    if visited is None:
        visited = set()

    if current_depth > max_depth:
        return

    if url in visited:
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    visited.add(url)
    print(f"Crawling: {url}")

    links = get_links(url, html)
    for link in links:
        crawl(link, max_depth, current_depth + 1, visited)

if __name__ == "__main__":
    start_url = input("Enter the starting URL: ")
    max_depth = int(input("Enter the maximum depth to crawl: "))
    crawl(start_url, max_depth)

   