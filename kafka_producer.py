from kafka import KafkaProducer
import json

producer = KafkaProducer(

    bootstrap_servers='kafka:9092',

    value_serializer=lambda v:
        json.dumps(v).encode('utf-8')
)

def publish_article(article):

    producer.send(
        'scraped_articles',
        article
    )

    producer.flush()

    print(
        f"Published: {article['title']}"
    )