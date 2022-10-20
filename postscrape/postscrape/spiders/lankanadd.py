from turtle import title
import scrapy

class PostsSpider(scrapy.Spider):
    name = "lanka"

    start_urls = [
        'https://lankanad.com/all'
    ]

    def parse(self, response):
        for post in response.css('post_post__1F3_x'):
            yield{
                'title':post.css('.post_card_title__1sNeD::text')[0].get()
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