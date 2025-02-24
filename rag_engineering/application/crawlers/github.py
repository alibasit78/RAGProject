from .base import BaseSeleniumCrawler
from loguru import logger
from data.sample_data import sample_dataset1, sample_dataset2
from rag_engineering.domain.documents import RepositoryDocument, UserDocument

class GithubCrawler(BaseSeleniumCrawler):
    model = RepositoryDocument
    def extract(self, link, **kwargs):
        logger.info(f"Extracting the page from github - {link}")
        topic = link.split("/")[-1].replace("-", " ")
        content = ""
        for sample_dataset in [sample_dataset1, sample_dataset2]:
            if topic in sample_dataset['GitHub']:
                content = sample_dataset['GitHub'][topic]
                break
        # print(content)
        # print(topic)
        self.scroll_page()
        user = kwargs["user"]
        instance = self.model(
            content={"content": content},
            name=topic,
            link=link,
            platform="github",
            # author_id=user.id,
            author_full_name=user.full_name,
        )
        self.model.save(instance)
        logger.info(f"Completed crawling of github - {link}")

if __name__ == "__main__":
    github_crawler = GithubCrawler()
    user_document = UserDocument(first_name="author", last_name = "1")
    github_crawler.extract(link=r"https://github.com/Open-Source-LLM-Chatbot", user = user_document)
    