from concurrent.futures import ThreadPoolExecutor, as_completed
from loguru import logger
from rag_engineering.constants import MONGO_DB_DIR_NAME
from rag_engineering.domain.documents import UserDocument, PostDocument, RepositoryDocument, ArticleDocument
from rag_engineering.application.utils import split_user_full_name
from loguru import logger
import os

def query_data_warehouse(author_file_name: list[str]):
    authors = []
    documents = []
    for author_full_name in author_file_name:
        first_name, last_name = split_user_full_name(author_full_name)
        author = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
        authors.append(author)
        # logger.info(f"Getting the author: {author_full_name}")
        # logger.info(f"Author : {author}")
        results = fetch_all_data(author)
        # logger.info(f"Results: {results}")
        documents.extend(results)
    logger.info(f"Completed the query_data_warehouse step: {documents}")
    return documents

def fetch_all_data(author):
    # author_dir_path = os.path.join(MONGO_DB_DIR_NAME, author.full_name)
    user_full_name = author.full_name
    with ThreadPoolExecutor() as executor:
        future_to_query = {
            executor.submit(__fetch_articles, user_full_name): "articles",
            executor.submit(__fetch_repositories, user_full_name): "repositories",
            executor.submit(__fetch_posts, user_full_name): "posts",
        }
        results = {}
        for future in as_completed(future_to_query):
            query_name = future_to_query[future]
            try:
                results[query_name] = future.result()
            except Exception as e:
                logger.error(f"An error occured while fetching {query_name}: {e}")
                results[query_name] = []
        return results

def __fetch_articles(user_full_name):
    return __fetch_data(user_full_name, "articles", ArticleDocument)

def __fetch_repositories(user_full_name):
    return __fetch_data(user_full_name, "repositories", RepositoryDocument)

def __fetch_posts(user_full_name):
    return __fetch_data(user_full_name, "posts", PostDocument)

def __fetch_data(user_full_name, data_type, document_type):
    user_dir_path = os.path.join(MONGO_DB_DIR_NAME, user_full_name)
    if not os.path.exists(user_dir_path):
        return []
    data = []
    for filename in os.listdir(user_dir_path):
        if filename.startswith(data_type):
            data.append(document_type.get_object_(filename.split("_")[-1].split(".")[0], author_full_name=user_full_name))
    logger.info(f"Found {len(data)} {data_type} for {user_full_name}")
    return data
if __name__ == "__main__":
    query_data_warehouse(["author 1", "author 2"])
           
        

        