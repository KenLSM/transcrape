import scrapy

class CSSpider(scrapy.Spider):
    name = "club_house_spider"
    allowed_domains = ["clubhouse.com"]
    start_urls = [
	"clubhouse.com/forums"  
	# not properly set. 
	# Will supply the initial links using another scraper.
        # this scraper will search within thread?
	# some other scraper will supply links + handle paignation
	# "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
