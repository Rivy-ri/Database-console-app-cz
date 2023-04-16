import re


class Customer:
    """

    Clas represent databse Entity Zakaznik

    """
    def __init__(self, name=None, lastname=None, email=None, phone=None, gender='N'):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.gender = gender

    def __str__(self):
        return f"{self.name} \n {self.lastname} \n {self.email} \n {self.phone} \n {self.gender}"

    def valid_email_check(self,email):
        """

        Method check if the format of email is valid

        :param email: e-mail adress type of string
        :return: True if is the format is right False if not
        """
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        match = email_regex.match(email)
        if match:
            return True
        else:
            return False
    def valid_phone_number(self,number):
        """

        Method check if the format of phone number is valid

        :param number: phone number type of string
        :return: True if is the format is right False if not
        """
        phone_regex = re.compile(r"\d{9}")
        match=phone_regex.match(number)
        if match:
            return True
        else:
            return False

