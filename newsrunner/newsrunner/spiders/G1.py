# -*- coding: utf-8 -*-
import scrapy


class G1Spider(scrapy.Spider):
    name = 'G1'
    allowed_domains = ['g1.globo.com.br']
    start_urls = ['http://g1.globo.com/politica']

    def parse(self, response):
        print response         
        for brickset in response.css('.feed-post-link'):
           print(brickset.css('.feed-post-link ::text').extract_first())
            
       
        pass
