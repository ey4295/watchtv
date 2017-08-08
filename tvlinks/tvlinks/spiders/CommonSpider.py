import scrapy


class CommonSpider:
    """common spider object"""
    start_urls = [
        'https://doc.scrapy.org/en/latest/intro/tutorial.html',

    ]

    target = ('//h2', 'xpath')

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.custom_parse)

    def custom_parse(self, response):
        return response.xpath(self.target[0]).extract() if self.target[1] == 'xpath' else response.css(
            self.target[0]).extract()

    def add_url(self, url):
        self.start_urls.append(url)

    def set_url(self, url):
        self.start_urls = [url]

    def set_target(self, target_path, path_type):
        self.target = (target_path, path_type)
