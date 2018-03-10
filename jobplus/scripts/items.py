import scrapy

class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    descriptian = scrapy.Field()
    type = scrapy.Field()
    job_count = scrapy.Field)


