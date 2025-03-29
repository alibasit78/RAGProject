from concurrent.futures import ThreadPoolExecutor, as_completed
from loguru import logger
from rag_engineering.constants import MONGO_DB_DIR_NAME
from rag_engineering.domain.documents import UserDocument, PostDocument, RepositoryDocument, ArticleDocument
from rag_engineering.application.utils import split_user_full_name
from loguru import logger
import os

def query_data_warehouse(author_full_names: list[str]):
    authors = []
    documents = []
    for author_full_name in author_full_names:
        first_name, last_name = split_user_full_name(author_full_name)
        author = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
        authors.append(author)
        # logger.info(f"Getting the author: {author_full_name}")
        # logger.info(f"Author : {author}")
        results = fetch_all_data(author)
        documents.extend([doc for result in results.values() for doc in result])
        # for result in results.values():
        #     documents.extend(result)
    logger.info(f"Completed the query_data_warehouse step: {len(documents)}")
    logger.info(f"metadata: {_get_metadata(documents)}")
    logger.info(f"All documents: {documents}")
    return documents

def _get_metadata(documents):
    metadata = {"num_documents": len(documents)}
    for document in documents:
        collection_name = document.get_collection_name()
        print("collection_name: ", collection_name, type(collection_name))
        if collection_name not in metadata:
            metadata[collection_name] = {}
        if "authors" not in metadata[collection_name]:
            metadata[collection_name]["authors"] = []
        metadata[collection_name]["num_documents"] = metadata[collection_name].get("num_documents", 0) + 1
        # print("metadata: ", metadata[collection_name]["authors"])
        metadata[collection_name]["authors"].append(document.author_full_name)
    return metadata
        

# The below functions can be added in the utils.py file
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
        logger.info(f"User directory not found: {user_dir_path}")
        return []
    data = []
    for filename in os.listdir(user_dir_path):
        if filename.startswith(data_type):
            logger.info(f"Found {data_type} file: {filename}")
            data.append(document_type.get_object_(filename.split("_")[-1].split(".")[0], author_full_name=user_full_name))
    logger.info(f"Found {len(data)} {data_type} for {user_full_name}")
    return data

if __name__ == "__main__":
    query_data_warehouse(["author 1", "author 2"])