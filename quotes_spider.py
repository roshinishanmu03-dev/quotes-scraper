import scrapy


class QuotesSpider(scrapy.Spider):
    """Collect quotes and their authors from a public practice website."""

    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "ROBOTSTXT_OBEY": True,
        "USER_AGENT": "LearningQuotesScraper/1.0 (educational project)",
    }

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(default="").strip(),
                "author": quote.css("small.author::text").get(default="").strip(),
                "tags": quote.css("div.tags a.tag::text").getall(),
                "source_url": response.url,
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)