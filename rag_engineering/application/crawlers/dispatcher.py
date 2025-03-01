from loguru import logger
import re
from .linkedin import LinkedinCrawler
from .github import GithubCrawler
from .medium import MediumCrawler
from .base import BaseCrawler
from urllib.parse import urlparse
from .exceptions import NotValidUrlException

class CrawlerDispatcher:
    def __init__(self):
        self._crawlers = {}
    
    @classmethod
    def build(cls):
        dispatcher = cls()
        return dispatcher
    
    def register_linkedin(self):
        logger.info(f"linkedin crawler created")
        self.register("https://linkedin.com", LinkedinCrawler)
        return self
    
    def register_github(self):
        logger.info(f"github crawler created")
        self.register("https://github.com", GithubCrawler)
        return self
    
    def register_medium(self):
        logger.info(f"medium crawler created")
        self.register("https://medium.com", MediumCrawler)
        return self
    
    def register(self, link, crawler: BaseCrawler):
        parsed_domain = urlparse(link)
        domain = parsed_domain.netloc
        self._crawlers[r'https://(www\.)?{}/*'.format(domain)] = crawler
    def get_crawler(self, url) -> BaseCrawler:
        for pattern, crawler in self._crawlers.items():
            if re.search(pattern, url):
                return crawler()
        logger.warning(f"No crawler found for {url}")
        raise NotValidUrlException(f"No crawler is present for the {url}")
                
    
    