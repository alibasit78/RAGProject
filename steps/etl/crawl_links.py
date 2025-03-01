from rag_engineering.domain.documents import UserDocument
from rag_engineering.application.crawlers.dispatcher import CrawlerDispatcher
from loguru import logger
from urllib.parse import urlparse
from tqdm import tqdm


def crawl_links(user: UserDocument, links):
    dispatcher = CrawlerDispatcher.build().register_linkedin().register_medium().register_github()
    logger.info(f"Starting to crawl {len(links)} links.")
    successful_crawls = 0
    metadata = {}
    for link in tqdm(links):
        successful_crawl, domain = _crawl_link(dispatcher, link, user)
        successful_crawls += successful_crawl
        metadata = _add_to_metadata(metadata, domain, successful_crawl)
        logger.info(f"metadata: {metadata}")
    logger.info(f"Successfully crawled {successful_crawls} / {len(links)} links.")

def _add_to_metadata(metadata:dict, domain:str, successfull_crawl:bool)->dict:
    if domain not in metadata:
        metadata[domain] = {}
    metadata[domain]["successful"] = metadata.get(domain, {}).get("successful", 0) + successfull_crawl
    metadata[domain]["total"] = metadata.get(domain, {}).get("total", 0) + 1
    return metadata

def _crawl_link(dispatcher: CrawlerDispatcher, link:str, user: UserDocument):
    crawler = dispatcher.get_crawler(link)
    crawler_domain = urlparse(link).netloc
    try:
        crawler.extract(link=link, user=user)
        return (True, crawler_domain)
    except Exception as e:
        logger.error(f'An error occured while crawling: {e}')
        return (False, crawler_domain)
    
if __name__ == "__main__":
    user = UserDocument(first_name="author", last_name = "1")
    links = ["https://linkedin.com/AI-Trends-2025", "https://medium.com/Understanding-Large-Language-Models", "https://github.com/Financial-Market-Analysis-Tool"]
    crawl_links(user=user, links = links)
        
