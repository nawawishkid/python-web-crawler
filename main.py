import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

def can_fetch(url, user_agent='*'):
    # Parse the robots.txt file for the domain
    rp = RobotFileParser()
    rp.set_url(f"{url.scheme}://{url.netloc}/robots.txt")
    rp.read()
    # Check if the user agent is allowed to fetch this URL
    return rp.can_fetch(user_agent, url.geturl())

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    urls = []
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):
            urls.append(href)

    return urls

def crawl(start_url, max_depth=1, user_agent='*'):
    visited = set()
    queue = [(start_url, 0)]

    while queue:
        current_url, depth = queue.pop(0)
        if depth > max_depth:
            break

        parsed_url = requests.utils.urlparse(current_url)
        if current_url not in visited and can_fetch(parsed_url, user_agent):
            visited.add(current_url)
            print(f"Visiting: {current_url}")

            try:
                for url in get_links(current_url):
                    if url not in visited:
                        queue.append((url, depth + 1))
            except requests.exceptions.RequestException:
                pass

    return visited

# Start crawling
crawled_urls = crawl('http://example.com', max_depth=2)
print(f"Crawled URLs: {crawled_urls}")

