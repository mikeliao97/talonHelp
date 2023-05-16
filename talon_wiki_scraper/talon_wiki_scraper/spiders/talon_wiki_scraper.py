import scrapy

class TalonWikiSpider(scrapy.Spider):
    name = 'talon_wiki_spider'
    start_urls = ['https://talon.wiki/']

    def parse(self, response):
        for article in response.css('div.page'):
            yield {
                'title': article.css('h1.page-header::text').get(),
                'link': article.css('a.page-link::attr(href)').get(),
                'content': article.css('div.page-body::text').get()
            }

        next_page = response.css('div.pagination::attr(data-next)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
