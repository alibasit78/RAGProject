from abc import ABC
import pickle
import os
import uuid
from pydantic import UUID4, BaseModel, Field
from loguru import logger
from utils import save_pickle, load_pickle
from rag_engineering.constants import DIR_NAME

class NoSQLBaseDocument(BaseModel, ABC):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    
    def save(model, **kwargs):
        id = model.id
        platform = model.platform
        save_pickle(model, os.path.join(DIR_NAME, platform+"_"+str(id)+".pkl"))

    @classmethod
    def get_object_(cls, id_, **kwargs):
        platform = kwargs['platform']
        load_pickle(os.path.join(DIR_NAME, platform+"_"+str(id_)+".pkl"))
        
    @classmethod
    def save_to_db(model):
        pass
    
    @classmethod
    def get_or_create(cls, **kwargs):
        instance = cls(**dict(kwargs))
        save_pickle(instance, os.path.join(DIR_NAME, "user_"+str(instance.id)+".pkl"))
        return instance