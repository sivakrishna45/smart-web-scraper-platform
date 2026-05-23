import sqlite3
import pandas as pd
from datetime import datetime
import logging
import os


class Database:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        self.db_path = "data/scraped_data.db"

        self.conn = sqlite3.connect(
            self.db_path,
            check_same_thread=False
        )

        self.logger = logging.getLogger(
            "Database"
        )

        self.create_table()

    def create_table(self):

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS articles (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            link TEXT UNIQUE,

            source TEXT,

            scraped_at TEXT
        )
    ''')

        self.conn.commit()

        self.logger.info(
            "Database table ready"
        )

    def save(self, df):

        if df.empty:

            self.logger.warning(
                "Empty dataframe received"
            )

            return

        df['scraped_at'] = (
            datetime.now().isoformat()
        )

        try:

            df.to_sql(
                'articles',
                self.conn,
                if_exists='append',
                index=False,
                method='multi'
            )

            self.logger.info(
                f"💾 Saved {len(df)} "
                f"new records to database"
            )

            print(
                f"✅ Saved {len(df)} "
                f"records successfully!"
            )

        except Exception as e:

            self.logger.warning(
                f"Duplicate insert skipped: {e}"
            )

    def fetch_latest(self, limit=100):

        query = f'''
            SELECT
                title,
                link,
                source,
                scraped_at
            FROM articles
            ORDER BY scraped_at DESC
            LIMIT {limit}
        '''

        return pd.read_sql(
            query,
            self.conn
        )

    def close(self):

        self.conn.close()

        self.logger.info(
            "Database connection closed"
        )