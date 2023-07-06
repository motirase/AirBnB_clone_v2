#!/usr/bin/python3
<<<<<<< HEAD
"""
Este módulo crea una instancia de un objeto de clase FileStorage
"""
# from models.base_model import BaseModel, Base
from os import getenv


is_type = getenv("HBNB_TYPE_STORAGE")

if is_type == 'db':
=======
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD

storage.reload()

=======
storage.reload()
>>>>>>> 8c5dbeed60929e24fc56e598218afe8c5214768b
