from kafka import KafkaConsumer

import psycopg2
import json

consumer = KafkaConsumer(

    'scraped_articles',

    bootstrap_servers='kafka:9092',

    auto_offset_reset='earliest',

    value_deserializer=lambda m:
        json.loads(m.decode('utf-8'))
)

conn = psycopg2.connect(

    host="postgres",

    database="scraperdb",

    user="admin",

    password="admin123"
)

cursor = conn.cursor()

for message in consumer:

    article = message.value

    try:

        cursor.execute(
            """
            INSERT INTO articles
            (
                title,
                link,
                source,
                scraped_at
            )
            VALUES (%s, %s, %s, %s)
            """,
            (
                article['title'],
                article['link'],
                article['source'],
                article['scraped_at']
            )
        )

        conn.commit()

        print(
            f"Saved: {article['title']}"
        )

    except Exception as e:

        conn.rollback()

        print(
            f"Error: {e}"
        )