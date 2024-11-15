from controller.User import User
from logs.custom_logger import custom_logging
from connection.connections import db_connection
from helper.email_verification import email_verification

if __name__ == "__main__":
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        
        if email_verification(email):
            user = User(name, email, password)
            
            user.update_db()
            
        else:
            custom_logging.error("Invalid email")
        
    except KeyboardInterrupt as e:
        custom_logging.info('Exitting ......')
        
    except Exception as e:
        custom_logging.error(f"Oops Something went wrong! {e}", exc_info=True)
        
    finally:
        db_connection.disconnect()