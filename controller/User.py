from sqlalchemy import insert, literal_column, select, or_
from connection.connections import db_connection
from helper.enqueue_job import enqueue_job
from helper.send_email import send_email
from model.DbTable import DbTable
from logs.custom_logger import custom_logging

class User:
    
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
    
    
    def update_db(self):
        
        try:
            # checking if entry already exists
            query = select(literal_column('1')).where(or_(DbTable.name == self._name, 
                DbTable.email == self._email))
                
            is_duplicate_user = db_connection.execute_query(query)
            
            if is_duplicate_user:
                custom_logging.error("This username or email already exists in database")
                return False
            
            query = insert(DbTable).values(name=self._name, email=self._email, password=self._password)

            is_successful = db_connection.execute_query(query)
            
            # if successful, shoot email
            if is_successful is True:
                custom_logging.info("Added data to database successfully")
                
                EMAIL_BODY = f"Name: {self._name} | Email: {self._email} | Password: {self._password}"
                
                enqueue_job(send_email, self._email, EMAIL_BODY)
                
                return True
                
            else:
                custom_logging.error("Data insertion in database failed")
                return False
            
        except Exception as e:
            custom_logging.error(f"Error while updating database: {e}", exc_info=True)
            return False
        
    
    