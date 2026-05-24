# Smart Web Scraper Platform 🚀

Production-style real-time web scraping platform built using Python, FastAPI, Kafka, Redis, PostgreSQL, BeautifulSoup, Playwright, and Docker.

The platform collects articles from multiple news and tech sources, processes them through an event-driven architecture, stores them in PostgreSQL, caches responses using Redis, and visualizes analytics through a modern FastAPI dashboard.

---

## Features

- Multi-source web scraping
- Real-time event-driven pipeline using Kafka
- FastAPI analytics dashboard
- PostgreSQL database integration
- Redis caching layer
- Dynamic website scraping using Playwright
- Duplicate prevention & idempotency handling
- CSV & Excel export support
- Search & filtering APIs
- Docker multi-container deployment
- Automated scheduling support
- Retry handling & resilience
- Logging & monitoring ready
- Source analytics visualization
- Responsive enterprise UI dashboard

---

## Integrated Sources

- Hacker News
- Reddit
- The Hindu
- Economic Times
- YourStory

---

## Tech Stack

### Backend
- Python
- FastAPI
- BeautifulSoup
- Playwright

### Streaming & Caching
- Apache Kafka
- Redis

### Database
- PostgreSQL
- SQLite (initial development)

### Data Processing
- Pandas

### Infrastructure
- Docker
- Docker Compose

### Reliability
- APScheduler
- Tenacity

---

## System Architecture

```text
Web Scrapers
      ↓
Kafka Producer
      ↓
Kafka Topic
      ↓
Kafka Consumer
      ↓
PostgreSQL Database
      ↓
Redis Cache
      ↓
FastAPI APIs
      ↓
Analytics Dashboard
```

---

## Project Structure

```text
web-scraper-system/
│
├── app.py
├── main.py
├── scheduler.py
├── database.py
├── kafka_producer.py
├── kafka_consumer.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
│
├── scrapers/
│   ├── base_scraper.py
│   ├── hackernews_scraper.py
│   ├── reddit_scraper.py
│   ├── hindu_scraper.py
│   ├── economictimes_scraper.py
│   ├── yourstory_scraper.py
│   └── utils/
│
├── templates/
├── logs/
├── data/
└── venv/
```

---

## Running the Project

### Start Containers

```bash
docker compose up --build
```

### Access Dashboard

```text
http://localhost:8000
```

### Kafka Topic Creation

```bash
docker exec -it scraper-kafka kafka-topics \
--create \
--topic scraped_articles \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```

---

## APIs

| Endpoint | Description |
|---|---|
| `/` | Dashboard UI |
| `/articles` | Latest articles |
| `/stats` | Analytics statistics |
| `/search` | Search articles |
| `/source/{source}` | Filter by source |
| `/health` | Health check |
| `/export/csv` | Export CSV |
| `/export/excel` | Export Excel |

---

## Future Enhancements

- Kubernetes deployment
- CI/CD pipeline
- Prometheus + Grafana monitoring
- Elasticsearch integration
- AI article summarization
- WebSocket real-time dashboard
- JWT authentication
- Microservices decomposition

---

## Screenshots

### Dashboard
Add your dashboard screenshot here.

### Analytics
Add your analytics screenshot here.

---

## Author

Sivakrishna Velpula

---

## License

MIT License