# Telegram Scraping

This script scrapes messages and media from specified Telegram channels and stores them in CSV files.

## Setup

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Set your Telegram API credentials in `telegram_scraper.py`.

3. Run the scraper:
    ```bash
    python telegram_scraper.py
    ```

## Channels Scraped

### Messages:
- https://t.me/DoctorsET
- https://t.me/lobelia4cosmetics
- https://t.me/yetenaweg
- https://t.me/EAHCI
- [Medicine Channels](https://et.tgstat.com/medicine)

### Images:
- https://t.me/Chemed
- https://t.me/lobelia4cosmetics

## Logs

Logs are stored in `logs/telegram_scraper.log`.

## Data

Scraped data is stored in the `data/raw/` directory.
