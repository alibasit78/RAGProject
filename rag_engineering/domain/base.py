from abc import ABC
import pickle
import os
import uuid
from pydantic import UUID4, BaseModel, Field
from loguru import logger
from utils import save_pickle, load_pickle
from rag_engineering.constants import MONGO_DB_DIR_NAME
from .exceptions import IncorrectConfigured

class NoSQLBaseDocument(BaseModel, ABC):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    
    @classmethod
    def save(cls, model, **kwargs):
        id = model.id
        # platform = model.platform
        collection_name = cls.get_collection_name()
        user_full_name = model.author_full_name
        save_dir_path = os.path.join(MONGO_DB_DIR_NAME, user_full_name)
        os.makedirs(save_dir_path, exist_ok=True)
        save_pickle(model, os.path.join(save_dir_path, collection_name+"_"+str(id)+".pkl"))

    @classmethod
    def get_object_(cls, id_, **kwargs):
        # platform = kwargs['platform']
        collection_name = cls.get_collection_name()
        user_dir_path = os.path.join(MONGO_DB_DIR_NAME, kwargs['author_full_name'])
        os.makedirs(user_dir_path, exist_ok=True)
        return load_pickle(os.path.join(user_dir_path, collection_name+"_"+str(id_)+".pkl"))
        
    @classmethod
    def save_to_db(model):
        pass
    
    @classmethod
    def get_or_create(cls, **kwargs):
        collection_name = cls.get_collection_name()
        # print(kwargs)
        kwargs['collection_name'] = collection_name
        try:
            instance = cls.find_one(**kwargs)
            if instance:
                return instance
            instance = cls(**dict(kwargs))
            user_dir_path = os.path.join(MONGO_DB_DIR_NAME, kwargs['first_name']+' '+kwargs['last_name'])
            os.makedirs(user_dir_path, exist_ok=True)
            save_pickle(instance, os.path.join(user_dir_path, collection_name+'_'+str(instance.id)+".pkl"))
            return instance
        except Exception as e:
            logger.error(f"Exception in saving or finding pickle file - {e}")
            raise IncorrectConfigured("Exception in saving or finding pickle file")
        
    @classmethod
    def find_one(cls, **kwargs):
        # prefix_filename = kwargs['collection_name']+"_"+kwargs["first_name"]+"_"+kwargs['last_name']
        prefix_filename = kwargs['collection_name']
        dir_path = os.path.join(MONGO_DB_DIR_NAME, kwargs["first_name"]+" "+kwargs['last_name'])
        if not os.path.exists(dir_path):
            return None
        for filename in os.listdir(dir_path):
            if filename.startswith(prefix_filename):
                return load_pickle(os.path.join(dir_path, filename))
        return None
        # raise IncorrectConfigured(f"Errors in finding the saved pickle file of {kwargs['collection_name']} collection_name")
        
    
    @classmethod
    def get_collection_name(cls):
        if not hasattr(cls, "Settings") or not hasattr(cls.Settings, "name"):
            raise IncorrectConfigured("Document should define the setting configuration with the attribute name (collection name)")
        return cls.Settings.name
        
        