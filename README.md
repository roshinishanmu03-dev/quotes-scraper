# Quotes Scraper — learning project

## Goal

Build a respectful web scraper that visits every page of the practice website
`quotes.toscrape.com`, extracts quote data, and exports it into reusable files.

## What you will learn

- Set up an isolated Python environment
- Identify HTML elements with CSS selectors
- Write a Scrapy spider
- Follow pagination without manually listing URLs
- Export results as JSON and CSV
- Add basic safety settings: robots.txt, delay, and a descriptive user agent

## Step 1: Set up

Open a terminal in this folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate with `.venv\\Scripts\\activate` instead.

## Step 2: Test selectors interactively

```bash
scrapy shell "https://quotes.toscrape.com/"
```

Then try these commands:

```python
response.css("div.quote").getall()[:1]
response.css("div.quote span.text::text").getall()[:3]
response.css("li.next a::attr(href)").get()
```

The key idea is **CSS selector → attribute/text to extract**. For example,
`div.quote span.text::text` means “text inside an element with class `text`,
inside a quote card.”

## Step 3: Run the provided spider

```bash
scrapy runspider quotes_spider.py -O quotes.json
scrapy runspider quotes_spider.py -O quotes.csv
```

Open either output file and confirm that every record contains `text`, `author`,
`tags`, and `source_url`.

## Step 4: Read the spider

The spider has three jobs:

1. `start_urls` supplies the first page.
2. `parse()` extracts one record for every `div.quote` card.
3. It finds the next-page link and uses `response.follow()` to continue until
   the link no longer exists.

`yield` hands each extracted dictionary (or next request) back to Scrapy.

## Step 5: Your exercises

Do these one at a time:

1. Add an `author_url` field by extracting the author link from each card.
2. Add `page_number`, derived from `response.url`.
3. Change `start_urls` to a tag page such as
   `https://quotes.toscrape.com/tag/love/`, then export `love_quotes.json`.
4. Stop after three pages using `DEPTH_LIMIT` in `custom_settings`.
5. Create an author spider: visit author links and collect the author’s birth
   date and birthplace.

## How Beautiful Soup fits in

Use Beautiful Soup when you want to parse one downloaded HTML document. Scrapy
is better when the task needs many requests, pagination, retrying, throttling,
and exporting. You can use Beautiful Soup inside a Scrapy callback, but Scrapy’s
built-in CSS/XPath selectors are usually enough.

## Responsible scraping checklist

- Read the site’s terms and `robots.txt` before scraping a real site.
- Prefer the official API when one exists.
- Use a delay; do not send high request volumes.
- Do not bypass logins, paywalls, CAPTCHAs, access controls, or collect private
  data.
- Save only data you have a legitimate reason to use.

## What to do next

When the basic spider works, tell me which exercise you reached. I can review
your changes or guide you through the author-detail spider next.