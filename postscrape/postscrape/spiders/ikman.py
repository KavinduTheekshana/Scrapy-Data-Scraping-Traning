import scrapy
from scrapy.crawler import CrawlerProcess

class CoalNewsFromOilPrice(scrapy.Spider):
    name = 'ikman'
    start_urls = ['https://ikman.lk/en/ads/sri-lanka?sort=date&order=desc&buy_now=0&urgent=0&page='+str(x) for x in range(1,3)]



    def parse(self, response):
        for link in response.xpath('//*[@class="normal--2QYVk"]/a/@href'):
            yield scrapy.Request(
                url='https://ikman.lk/'+link.get(),
                callback=self.parse_item
            )

    def parse_item(self, response):
        yield {
            # 'datetime': response.xpath('//*[@class="article_byline"]/text()[2]').get(),
            # 'category': response.xpath('(//*[@itemprop="name"])[3]/text()').get(),
            'title': response.xpath('//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div/h1/text()').extract(),
            # 'text':''.join([x.get().strip() for x in response.xpath('//*[@id="article-content"]//p//text()')])
            }
       


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(CoalNewsFromOilPrice)
    process.start()