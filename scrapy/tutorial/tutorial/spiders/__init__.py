import scrapy


class QuotesSpider(scrapy.Spider):
    # identifies the spider name. Called to execute crawler in terminal: "scrapy crawl quotes"
    name = "quotes"

    # generator function or list. This function just has to return at iterable object/list
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # get the last piece in the URL
        # page = list(filter(None,response.url.split("/")))[-1]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
            # f.write(response.body)

        for quote in response.css("div.quote"):
            # print(dict(text=text, author=author, tags=tags))
            yield {
                'text' : quote.css("span.text::text").extract_first().encode("utf-8"),
                'author' : quote.css("small.author::text").extract_first().encode("utf-8"),
                'tags' : quote.css("div.tags a.tag::text").extract()
            }

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)


                # f.write(text)
                # f.write(author)
                # f.write(', '.join(tags)+'\n\n')

        # self.log('Saved file %s' % filename)