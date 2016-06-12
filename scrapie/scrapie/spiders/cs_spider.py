import scrapy
from urllib.parse import urljoin


class CSSpider(scrapy.Spider):
    name = "club_house_spider"
    allowed_domains = ["clubhouse.com"]
    start_urls = [
        "http://www.clubsnap.com/forums/forumdisplay.php?f=102",
        "http://www.clubsnap.com/forums/forumdisplay.php?f=104",
    ]

    thread_path = "//*[@class='threadtitle']/a[contains(@class, 'title')]"
    domain = "http://www.clubsnap.com/forums/"

    def parse(self, response):
        thread_urls = []
        for thread in response.xpath(self.thread_path):
            urls = [
                urljoin(self.domain, rel_link)
                for rel_link in thread.xpath("@href").extract()
            ]

            thread_urls.extend(urls)

        print(thread_urls)
