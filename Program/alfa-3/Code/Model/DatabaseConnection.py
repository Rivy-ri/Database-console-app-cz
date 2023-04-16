import mysql.connector
from Code.Model.Workers.ConfigurationWorker import ConfigurationWorker
class DatabaseConnection:
    """

    Database connection is singleton that work as connection to _database

    """
    _instance=None

    def __new__(cls):
        if cls._instance==None:
            cls._instance=super().__new__(cls)
            return cls._instance
        else:
            return cls._instance

    def __init__(self):
        worker=ConfigurationWorker()
        if worker.check_existence_of_configuration_file()==True:
            self.connection=mysql.connector.connect(
            host =worker.get_data_from_cofiguration_file('host'),
            user = worker.get_data_from_cofiguration_file('user'),
            password = worker.get_data_from_cofiguration_file('password'),
            database = worker.get_data_from_cofiguration_file('database'),
            buffered= False
            )
            self.cursor=self.connection.cursor()

        else:
            input("configuration file is empty! program shutting dow hit any key...")
            exit()






