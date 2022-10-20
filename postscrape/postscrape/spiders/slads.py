from turtle import delay
import scrapy
from scrapy.crawler import CrawlerProcess
import time
import json

class CoalNewsFromOilPrice(scrapy.Spider):
    name = 'sla'
    start_urls = ['https://sl-ads.com/index.php?action=1&page='+str(x)+'&category=&location=&search=' for x in range(1,3)]
    download_delay = 1.5

    def parse(self, response):
        for link in response.xpath('//*[@class="normalAdHeadingDiv"]/a/@href'):
            yield scrapy.Request(
                url='https://sl-ads.com/'+link.get(),
                callback=self.parse_item        
            )
  

    def parse_item(self, response):
   
        yield {
           
            # 'datetime': response.xpath('//*[@class="article_byline"]/text()[2]').get(),
            # 'category': response.xpath('(//*[@itemprop="name"])[3]/text()').get(),
            'title': response.xpath('//*[@id="desctiptionTxt"]/text()').get()
            # 'text':''.join([x.get().strip() for x in response.xpath('//*[@id="article-content"]//p//text()')])
            }
       


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(CoalNewsFromOilPrice)
    process.start()