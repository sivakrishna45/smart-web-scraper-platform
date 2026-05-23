import logging

from database import Database

from scrapers.hackernews_scraper import HackerNewsScraper
from scrapers.reddit_scraper import RedditScraper
from scrapers.hindu_scraper import HinduScraper
from scrapers.economictimes_scraper import EconomicTimesScraper
from scrapers.yourstory_scraper import YourStoryScraper


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/scraper.log"),
        logging.StreamHandler()
    ]
)


def main():

    print("🚀 Starting Smart Web Scraper System\n")

    db = Database()

    scrapers = [

    HackerNewsScraper(),

    RedditScraper(),

    HinduScraper(),

    EconomicTimesScraper(),

    YourStoryScraper()
]

    for scraper in scrapers:

        try:

            print(
                f"\n🔍 Running "
                f"{scraper.__class__.__name__}"
            )

            df = scraper.scrape()

            if not df.empty:

                db.save(df)

                print(
                    f"✅ Successfully scraped and saved "
                    f"{len(df)} records from "
                    f"{scraper.__class__.__name__}"
                )

            else:

                print(
                    f"⚠️ No data scraped from "
                    f"{scraper.__class__.__name__}"
                )

        except Exception as e:

            print(
                f"❌ Error in "
                f"{scraper.__class__.__name__}: {e}"
            )


if __name__ == "__main__":
    main()