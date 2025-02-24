
from loguru import logger
from rag_engineering.application import utils
def get_or_create_user(user_full_name: str):
    logger.info(f"Getting or creating user: {user_full_name}")
    
    first_name, last_name = utils.split_user_full_name(user_full_name)
    