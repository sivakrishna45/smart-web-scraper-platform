from .base_scraper import BaseScraper
import pandas as pd


class HinduScraper(BaseScraper):

    def scrape(self):

        self.logger.info(
            "Starting The Hindu scrape..."
        )

        url = "https://www.thehindu.com/news/"

        html = self.fetch(url)

        soup = self.parse(html)

        articles = []

        items = soup.select("h3.title a")

        for item in items[:20]:

            title = item.get_text(strip=True)

            link = item.get("href")

            if title and link:

                articles.append({
                    "title": title,
                    "link": link,
                    "source": "The Hindu"
                })

        df = pd.DataFrame(articles)

        self.logger.info(
            f"Extracted {len(df)} Hindu articles"
        )

        return df