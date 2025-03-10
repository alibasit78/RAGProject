from abc import ABC
import pickle
import os
import uuid
from pydantic import UUID4, BaseModel, Field
from loguru import logger
from utils import save_pickle, load_pickle
from rag_engineering.constants import VECTOR_DB_DIR_NAME
from ..exceptions import IncorrectConfigured

class VectorBaseDocument(BaseModel, ABC):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    
    @classmethod
    def save(cls, model, **kwargs):
        id = model.id
        # platform = model.platform
        collection_name = cls.get_collection_name()
        user_full_name = model.author_full_name
        save_dir_path = os.path.join(VECTOR_DB_DIR_NAME, user_full_name)
        os.makedirs(save_dir_path, exist_ok=True)
        save_pickle(model, os.path.join(save_dir_path, collection_name+"_"+str(id)+".pkl"))

    @classmethod
    def get_object_(cls, id_, **kwargs):
        # platform = kwargs['platform']
        collection_name = cls.get_collection_name()
        user_dir_path = os.path.join(VECTOR_DB_DIR_NAME, kwargs['author_full_name'])
        os.makedirs(user_dir_path, exist_ok=True)
        return load_pickle(os.path.join(user_dir_path, collection_name+"_"+str(id_)+".pkl"))
    
    @classmethod
    def find_one(cls, **kwargs):
        # prefix_filename = kwargs['collection_name']+"_"+kwargs["first_name"]+"_"+kwargs['last_name']
        prefix_filename = kwargs['collection_name']
        dir_path = os.path.join(VECTOR_DB_DIR_NAME, kwargs["first_name"]+" "+kwargs['last_name'])
        if not os.path.exists(dir_path):
            return None
        for filename in os.listdir(dir_path):
            if filename.startswith(prefix_filename):
                return load_pickle(os.path.join(dir_path, filename))
        return None

    @classmethod
    def get_collection_name(cls):
        if not hasattr(cls, "Config") or not hasattr(cls.Config, "name"):
            raise IncorrectConfigured("Document should define the setting configuration with the attribute name (collection name)")
        return cls.Config.name