import configparser
import os
import sys


class ConfigurationWorker:
    """
    Class serv as reader of configuration file.

    Parameters:
        self._path= predefined value of path to configuration file
        self._configuration_name= predefined name of value in configuration file

    Methods:
        check_existence_of_configuration_file: method on call check if the path exists
        _create_new_configuration_file: will create new configuration file the check find that doesnt exist
        get_data_from_cofiguration_file: will return value for key


    """

    def __init__(self):
        self._path = 'Configuration\Configuration_file.ini'
        self._configuration_name = 'database connection string'

    def check_existence_of_configuration_file(self):
        """

        Method will check existenc of Configuration file if the file doesn't exist it will create
        new with _create_new_configuration_file method

        :return: False if the new has to be created True if it exist
        """
        try:
            if os.path.exists(self._path) == True:
                return True
            else:
                raise ConfigurationError("configuration file doesnt exist")
        except ConfigurationError as exeption:
            print(exeption, end=' ')
            print('I will create new configuration file for you')
            self._create_new_configuration_file()
            return False

    def _create_new_configuration_file(self):
        """

        Will create a new configuration fille if there wasnt any found

        :return:void
        """

        configuration_parser = configparser.ConfigParser()
        configuration_parser[self._configuration_name] = \
            {

                'host': '',
                'user': '',
                'password': '',
                'database': ''

            }
        while True:
            try:
                with open(self._path, 'w') as file:
                    configuration_parser.write(file)
                    print('New configuration file was successfully created, please fill it')
                    sys.exit()
                    return
            except FileNotFoundError:
                os.mkdir('Configuration')
                continue

    def get_data_from_cofiguration_file(self, key: str):
        """

        This method read configuration file that shuth be locaded in
        Configuration folder under name onfiguration_file

        :param key: for which part i wan to get data from configuration file
        :return: value for _database or None if there is no data for key
        """
        try:
            if os.path.exists(self._path) == True:
                configuration_parser = configparser.ConfigParser()
                configuration_parser.read(self._path)
                value = configuration_parser[self._configuration_name][key]
                if len(value) > 0:
                    return value
                else:
                    raise ConfigurationError(f'key:{key} has no information given, please fil it')
            else:
                self._create_new_configuration_file()

        except ConnectionError as exeption:
            print(exeption)
            return


class ConfigurationError(Exception):
    """
    an Error Class that raise new error that make shure that the configuration file is filed
    """

    def __init__(self, message: str):
        self.message = message
