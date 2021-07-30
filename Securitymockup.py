import mysql.connector
from mysql.connector import Error
import pandas as pd
from cryptography.fernet import Fernet
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def register(Tele_id, username, password):
    f = Fernet(Tele_id)
    token_id = f.encrypt(Tele_id)
    token_username = f.encrypt(username)
    token_password = f.encrypt(password)
    new_user = """INSERT INTO users VALUES({token_id}, {token_username}, {token_password}""".format(token_id=token_id,
                                                                                                    token_username= token_username,
                                                                                                    token_password= token_password)
