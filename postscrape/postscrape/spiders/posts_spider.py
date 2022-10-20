from turtle import title
import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://www.zyte.com/blog/'
    ]

    def parse(self, response):
        for post in response.css('div.oxy-post'):
            yield{
                'title':post.css('.oxy-post-wrap a::text')[0].get()
            }
            next_page = response.css('div.oxy-easy-posts-pages a.next::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page,callback=self.parse)

        # page = response.url.split('/')[-1]
        # print(page)
        # filename = 'posts-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)