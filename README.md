# Smart Web Scraper Platform 🚀

A production-style multi-source web scraping platform built using Python, FastAPI, BeautifulSoup, Playwright, SQLite, and APScheduler.

## Features

- Multi-source scraping
- Indian news website scraping
- Dynamic website scraping using Playwright
- FastAPI dashboard
- SQLite database integration
- Duplicate prevention
- Automated scheduler
- Retry handling
- Logging & monitoring
- Change detection

## Integrated Sources

- Hacker News
- Reddit
- The Hindu
- Economic Times
- YourStory

## Tech Stack

- Python
- FastAPI
- BeautifulSoup
- Playwright
- SQLite
- APScheduler
- Pandas
- Tenacity

## Project Structure

```text
web-scraper-system/
│
├── app.py
├── main.py
├── scheduler.py
├── database.py
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