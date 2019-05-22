from abc import ABCMeta, abstractmethod
 
# abstrct for the repository 
class AbstractDAO(object):
    __metaclass__ = ABCMeta
     
    @abstractmethod
    def save(self):
        pass
    
    

#concrete class implementing AbractDAO 
class FileDAO(AbstractDAO):
    def save(self):
        print("Saving on File")
        

#concrete class implementing AbractDAO 
class DatabaseDAO(AbstractDAO):
    def save(self):
        print("Saving on Database")
        
        

fileDAO = FileDAO()
fileDAO.save()

databaseDAO = DatabaseDAO()
databaseDAO.save()