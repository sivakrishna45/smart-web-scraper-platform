from .base_scraper import BaseScraper
import pandas as pd


class RedditScraper(BaseScraper):

    def scrape(self):

        self.logger.info(
            "Starting Reddit scrape..."
        )

        url = "https://old.reddit.com/r/programming/"

        html = self.fetch(url)

        soup = self.parse(html)

        articles = []

        items = soup.select("a.title")

        for item in items[:20]:

            title = item.get_text(strip=True)

            link = item.get("href")

            if title and link:

                articles.append({
                    "title": title,
                    "link": link,
                    "source": "Reddit"
                })

        df = pd.DataFrame(articles)

        self.logger.info(
            f"Extracted {len(df)} Reddit posts"
        )

        return df