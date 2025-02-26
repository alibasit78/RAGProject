from abc import ABC
import pickle
import os
import uuid
from pydantic import UUID4, BaseModel, Field
from loguru import logger
from utils import save_pickle, load_pickle
DIR_NAME:str = r'C:\Users\DELL\Downloads\projects\MyAssistant\RAGProject\data\domain'
class NoSQLBaseDocument(BaseModel, ABC):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    
    def save(model, **kwargs):
        id = model.id
        platform = model.platform
        # user_id = model.author_id
        # with open(os.path.join(DIR_NAME, platform+"_"+str(id)+".pkl"), "wb") as fw:
        #     pickle.dump(model, fw)
        save_pickle(model, os.path.join(DIR_NAME, platform+"_"+str(id)+".pkl"))
    # 
    @classmethod
    def get_object_(cls, id_, **kwargs):
        platform = kwargs['platform']
        # dir_name = kwargs['dir_name']
        with open(os.path.join(DIR_NAME, platform+"_"+str(id_)+".pkl"), "rb") as fr:
            return pickle.load(fr)
        
    @classmethod
    def save_to_db(model):
        pass
    
    @classmethod
    def get_or_create_obj(cls, **kwargs):
        logger.info(kwargs["first_name"], kwargs["last_name"])
        # return kwargs['first_name']+' '+kwargs['last_name']
        instance = cls(**dict(kwargs))
        save_pickle(instance, os.path.join(DIR_NAME, "user_"+str(instance.id)+".pkl"))
        return instance