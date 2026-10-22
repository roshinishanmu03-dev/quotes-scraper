import unittest

from scrapy.http import TextResponse

from quotes_spider import QuotesSpider


class QuotesSpiderTests(unittest.TestCase):
    def test_extracts_a_quote_and_follows_pagination(self):
        html = """
        <div class="quote">
          <span class="text"> A quote </span>
          <small class="author">Ada</small>
          <div class="tags"><a class="tag">science</a></div>
        </div>
        <li class="next"><a href="/page/2/">next</a></li>
        """
        response = TextResponse(
            "https://quotes.toscrape.com/", body=html.encode(), encoding="utf-8"
        )

        results = list(QuotesSpider().parse(response))

        self.assertEqual(
            results[0],
            {
                "text": "A quote",
                "author": "Ada",
                "tags": ["science"],
                "source_url": "https://quotes.toscrape.com/",
            },
        )
        self.assertEqual(results[1].url, "https://quotes.toscrape.com/page/2/")