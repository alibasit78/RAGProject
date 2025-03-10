
from loguru import logger
from rag_engineering.application import utils
from rag_engineering.domain.documents import UserDocument

def get_or_create_user(user_full_name: str):
    logger.info(f"Getting or creating user: {user_full_name}")
    first_name, last_name = utils.split_user_full_name(user_full_name)
    user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
    logger.info(_get_metadata(user_full_name, user))
    logger.info("Completed the get_or_create_user step")
    return user

def _get_metadata(user_full_name: str, user: UserDocument):
    return {
        'query': {"user_full_name":user_full_name},
        'retrieved': {'user_id':user.id, 'first_name':user.first_name, 'last_name': user.last_name}
    }

if __name__ == "__main__":
    get_or_create_user("Vivek kumar gupta")
    