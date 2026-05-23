from .base_scraper import BaseScraper
import pandas as pd


class YourStoryScraper(BaseScraper):

    def scrape(self):

        self.logger.info(
            "Starting YourStory scrape..."
        )

        url = "https://yourstory.com"

        html = self.fetch(
            url,
            dynamic=True
        )

        soup = self.parse(html)

        articles = []

        for item in soup.find_all("a")[:300]:

            title = item.get_text(strip=True)

            link = item.get("href")

            if (
                title
                and link
                and len(title) > 25
            ):

                if not link.startswith("http"):

                    link = f"https://yourstory.com{link}"

                articles.append({
                    "title": title,
                    "link": link,
                    "source": "YourStory"
                })

        df = pd.DataFrame(articles)

        self.logger.info(
            f"Extracted {len(df)} YourStory articles"
        )

        return df