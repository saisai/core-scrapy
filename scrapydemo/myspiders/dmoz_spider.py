#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""
from scrapydemo.items import *
from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.exceptions import DropItem


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('text()').re(r'-\s([^\n]*?)\n')
            items.append(MyItem(title=title, link=link, desc=desc))

        return items


class BaiduSpider(Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://www.baidu.com/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        self.log('parse.... %s' % (response.url,), log.INFO)
        title = response.xpath(u'//a[text()="关于百度"]/text()').extract()[0]
        self.log('========title=%s' % title.encode('gb2312'), log.INFO)
        link = 'dddd'
        desc = 'ccccc'
        return MyItem(title=title, link=link, desc=desc)


