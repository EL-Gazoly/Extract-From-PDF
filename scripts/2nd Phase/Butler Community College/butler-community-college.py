from scrapy.crawler import CrawlerProcess
import scrapy
import logging
import re


class ButlerCommunityCollegeScraper(scrapy.Spider):
    name = 'butler-community-college'

    def start_requests(self):
        url = 'https://catalog.butlercc.edu/content.php?catoid=10&navoid=485'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for uri in response.xpath("//a[contains(@href, 'preview_course')]/@href").getall():
            yield response.follow(uri, callback=self.parse_course)

        next_page_url = response.xpath("//td[text()='Page: ']/span[@aria-current]/following-sibling::a/@href").get()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_course(self, response):
        item = {}
        item['code'] = response.xpath("//h1[@id='course_preview_title']/text()").re_first(r'(\b[A-Z]+\s+\d{2,4})')



        title_text = response.xpath("//h1[@id='course_preview_title']/text()").get()
        import re

        title_match = re.search(r'\b[A-Z]+\s+\d{2,4}\.\s*(.*)', title_text)
        if title_match:
            item['title'] = title_match.group(1)
        else:
            item['title'] = None

        
        # Extracting description
        text_items = response.css("td[class='block_content']::text")

        possible_desc = []
        

        for text_item in text_items:
            text = text_item.get().strip()  # Get the text content and remove leading/trailing spaces
            
            # Check if the text contains a numeric value (assuming course credits are numeric)
            if text.isdigit():
                item['credits'] = int(text)  # Convert the numeric text to an integer
            elif len(text) >= 100:
                desc = self.normalize_spaces_and_line_breaks(text)
                length = len(text)
                possible_desc.append((length, desc))
                possible_desc.sort()
        if len(possible_desc) >= 1:
            item['description'] = possible_desc[-1][1]
        else:
            item['description'] = ''

        yield item

    @staticmethod
    def normalize_spaces_and_line_breaks(text):
        # Replace line breaks with space
        text = text.replace('\n', ' ')

        # Replace multiple spaces with a single space
        text = ' '.join(text.split())

        return text


crawler = CrawlerProcess(settings={
    "FEEDS": {"butler-community-college.csv": {"encoding": "utf8", "format": "csv", "overwrite": True}},
    "LOG_LEVEL": logging.DEBUG
})
crawler.crawl(ButlerCommunityCollegeScraper)
crawler.start(stop_after_crawl=True)