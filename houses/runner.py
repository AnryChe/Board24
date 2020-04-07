from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from houses import settings
from houses.spiders.rub_houses import RubHousesSpider



if __name__ =='__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(RubHousesSpider)
    # process.crawl(SjruSpider)
    process.start()
