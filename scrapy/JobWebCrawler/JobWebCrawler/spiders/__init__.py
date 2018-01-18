# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# https://www.indeed.com/jobs?q=Kafka&l=94002
import scrapy
from JobWebCrawler.items import JobwebcrawlerItem

class JobPostingSpider(scrapy.Spider):
    # identifies the spider name. Called to execute crawler in terminal: "scrapy crawl quotes"
    name = "job_posting"

    # generator function or list. This function just has to return at iterable object/list
    def start_requests(self):
        urls = [
            # 'http://quotes.toscrape.com',
            'https://www.indeed.com/jobs?q=Kafka&l=94002' #&sort=date
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):


        jobPosts = response.css('.row') #a.turnstileLink')

        jobCounter = 0
        for jobPosting in jobPosts:


            if jobCounter == 8:
                continue

            print('--STARTING--------------------------------------------------------------------')
            print('jobCounter', jobCounter)
            print('--END-------------------------------------------------------------------------')

            item = JobwebcrawlerItem()

            jobCounter += 1
            allLinks = jobPosting.css('a.turnstileLink')
            site = ''
            title = ''
            companyName = jobPosting.css('span.company::text').extract_first().strip('\n ')
            counter = 0


            for linkSelector in allLinks:
                # print('\nlinkCounter', counter)
                # print('TXT', linkSelector.css('a::text').extract())
                # print('TTL', linkSelector.css('a::attr(title)').extract())
                # print('CMP', companyName == '', len(companyName), companyName)
                # print(linkSelector.css('a::attr(href)').extract())

                link = linkSelector.css('a::attr(href)').extract_first()

                if '/cmp' in link and len(companyName) == 0 :
                    companyName = linkSelector.css('a::text').extract_first().strip('\n ')
                    # print('new CMP', len(companyName) == 0, len(companyName), companyName)

                    if len(companyName) == 0:
                        companyName = linkSelector.css('a::attr(title)').extract_first().strip('reviews').strip(' ')
                        # print('newer CMP', len(companyName) == 0, len(companyName), companyName)

                elif '/pagead' in link or '/rc' in link:
                    # print('TTL', linkSelector.css('a::attr(title)').extract())
                    site = link
                    title = linkSelector.css('a::attr(title)').extract_first()

                counter += 1
                # print('\n')

            # .strip(' \t\n')
            location = jobPosting.css('span.location::text').extract_first()

            # print('POSTING:', ", ".join([title, companyName, location])) # site
            # print('companyName', companyName)
            # companyName = jobPosting.css('span.company::text').extract_first().strip(' \t\n')
            # print('New companyName', companyName)

            item['title'] = title
            item['company'] = companyName
            item['location'] = location

            print('-----ITEM:', item)
            yield response.follow(site, callback=self.parse_job_posting, meta = {'item' : item})



    def parse_job_posting(self, response):
        item = response.meta['item']

        self.logger.info("Visited %s", response.url)

        skills = response.css('li::text').extract()
        item['skills'] = skills

        summary = response.css('span#job_summary::text').extract()
        if len(summary) > 0:
            summary = [x.strip('\n') for x in response.css('span#job_summary::text').extract()]

        item['summary'] = summary

        yield item
