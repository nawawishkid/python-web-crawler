# Python Web Crawler

## Overview

This Python web crawler is a simple tool designed to traverse the web by following links from a starting URL. It respects the rules set in the `robots.txt` file of each website, making it an ethical choice for basic web scraping and data collection tasks.

## Features

- **Robots.txt Compliance**: Automatically checks and respects the `robots.txt` file for each domain.
- **Depth Control**: Users can specify the depth of crawling.
- **Simple Link Extraction**: Extracts all hyperlinks from the web pages it visits.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python ^3.8 installed on your system.
- `requests` and `bs4` (BeautifulSoup) libraries installed. You can install these using pip:

  ```bash
  pip install requests bs4
  ```

````

### Installation & Usage
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/python-web-crawler.git
cd python-web-crawler
````

To run the web crawler, execute the script with Python:

```bash
python web_crawler.py
```

### Configuration

You can configure the following parameters in the script:

`start_url`: The URL where the crawler begins.  
`max_depth`: The maximum depth of crawling.  
`user_agent`: The user agent string used for crawling.

### Contact

If you want to contact me, you can reach me at [nawawishkid.dev@gmail.com](mailto:nawawishkid.dev@gmail.com)
