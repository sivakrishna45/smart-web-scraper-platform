from .base_scraper import BaseScraper
from .utils.change_detector import ChangeDetector
import pandas as pd
from bs4 import BeautifulSoup   # ← This was missing

class HackerNewsScraper(BaseScraper):
    def __init__(self):
        super().__init__()
        self.change_detector = ChangeDetector()

    def scrape(self):
        self.logger.info("Starting Hacker News scrape...")
        url = "https://news.ycombinator.com"
        
        try:
            html = self.fetch(url)
            
            # Check for website changes
            self.change_detector.detect_change("Hacker News", html)
            
            soup = self.parse(html)
            
            articles = []
            for item in soup.select('tr.athing'):
                title_tag = item.select_one('.titleline > a')
                if title_tag:
                    articles.append({
                        "title": title_tag.get_text(strip=True),
                        "link": title_tag.get('href'),
                        "source": "Hacker News"
                    })
            
            df = pd.DataFrame(articles)
            self.logger.info(f"Successfully extracted {len(df)} articles")
            return df
            
        except Exception as e:
            self.logger.error(f"Failed to scrape Hacker News: {e}")
            raise
