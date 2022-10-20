import scrapy
from scrapy.crawler import CrawlerProcess

class CoalNewsFromOilPrice(scrapy.Spider):
    name = 'coalnews'
    start_urls = ['https://oilprice.com/Energy/Coal/Page-'+str(x)+'.html' for x in range(1,18)]

    def parse(self, response):
        for link in response.xpath('//*[@class="categoryArticle__content"]/a/@href'):
            yield scrapy.Request(
                url=link.get(),
                callback=self.parse_item
            )

    def parse_item(self, response):
        yield {
            'datetime': response.xpath('//*[@class="article_byline"]/text()[2]').get(),
            'category': response.xpath('(//*[@itemprop="name"])[3]/text()').get(),
            'title': response.xpath('//*[@class="singleArticle__content"]/h1/text()').get(),
            'text':''.join([x.get().strip() for x in response.xpath('//*[@id="article-content"]//p//text()')])
            }
       


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(CoalNewsFromOilPrice)
    process.start()