#!/usr/bin/python3
"""Instantiates a storage object.

If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
instantiates a database storage engine (DBStorage).
Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


"""This checks the envirn var to determine storage method"""
if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    """The file storage selected"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
