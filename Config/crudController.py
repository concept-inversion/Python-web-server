import json
from Config.postgreModule import Postgre_db
#generate query from user input
class CRUD():
    '''
    Class to implement CRUD functionality:
    1. Create(self, each)
        Inserts data in the database.
        each -> Python dict input
    2. Update(self,param)
        Updates  columns 
    3. Read(self, param)
    
    4. Delete(self,param)
    
    5. View(self, param)

    6. Jsonloader(self, data)
    
    '''
    
    def __init__(self):
        # use without self
        self.db= Postgre_db()

    def Create(self,data):
        self.db.Create(data)
        

    def Update(self,each,Id):
        #statement = f'''
        #                    UPDATE People SET  Bio={each['Bio']},
        #                                    Name={each['Name']},
        #                                    Dob={each['Dob']}, 
        #                                    Gender={each['Gender']},
        #                                    Email={each['Email']}, 
        #                                    Longitude={each['Longitude']},
        #                                    Latitude={each['Latitude']},
        #                                    Phone={each['Phone']},
        #                                    Link={each['Link']},
        #                                    Image={each['Image']},
        #                                    Address={each['Address']} 
        #                    WHERE Id = {Id} '''
        
        data=self.db.Update(each,Id)
        
        return data 

    def Read(self, param):
        statement= ' SELECT * FROM PEOPLE WHERE (%s)'% (param)
        data=self.db.executeDB(statement,param)
        if data:
            return data.fetchall()
    
    def View(self,param=[]):
        statement= ' SELECT * FROM PEOPLE ' 
        data=self.db.executeDB(statement,param)
        if data:
            return data

    def Delete(self, param):
        statement= 'DELETE FROM PEOPLE WHERE (%s)'%(param)
        data=self.db.executeDB(statement,param)
        return data

    def JsonLoader(self,data):
        self.db.JsonLoader(data)
    
    def close(self):
        self.db.closeDB()
        


