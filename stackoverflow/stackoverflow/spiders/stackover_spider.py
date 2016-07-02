
import scrapy

from stackoverflow.items import StackoverflowItem



class Stackover(scrapy.Spider):
    name = 'stackover'
    allowed_domains = ['http://stackoverflow.com/']
    start_urls = [
        'http://stackoverflow.com/search?page=951&tab=relevance&q=a'
    ]

    def parse(self, response):
        
        for url in response.xpath('//div[@class="result-link"]/span/a/@href').extract():
            url = response.urljoin(url)
            request = scrapy.Request(url, callback=self.parse_data,dont_filter=True)
            yield request

	next_page = response.xpath('//div[@class="pager fl"]/a[@rel="next"]/@href')
        print next_page
        if next_page:
            url = response.urljoin(next_page.extract_first())
            yield scrapy.Request(url, callback=self.parse,dont_filter=True)

    def parse_data(self, response):
        temp = StackoverflowItem()
        temp['question'] = response.xpath('//h1[@itemprop="name"]/a/text()').extract()[0]
        return temp
