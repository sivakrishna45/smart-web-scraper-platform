from .base_scraper import BaseScraper
import pandas as pd


class EconomicTimesScraper(BaseScraper):

    def scrape(self):

        self.logger.info(
            "Starting Economic Times scrape..."
        )

        url = (
            "https://economictimes.indiatimes.com/"
            "news/newsblogs"
        )

        html = self.fetch(url)

        soup = self.parse(html)

        articles = []

        items = soup.find_all("a")

        for item in items[:150]:

            title = item.get_text(strip=True)

            link = item.get("href")

            if (
                title
                and link
                and len(title) > 25
            ):

                if not link.startswith("http"):

                    link = (
                        "https://economictimes.indiatimes.com"
                        + link
                    )

                articles.append({
                    "title": title,
                    "link": link,
                    "source": "Economic Times"
                })

        df = pd.DataFrame(articles)

        self.logger.info(
            f"Extracted {len(df)} Economic Times articles"
        )

        return df