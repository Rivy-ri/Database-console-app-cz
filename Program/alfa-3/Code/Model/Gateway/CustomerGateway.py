import mysql.connector.errors
from Code.Interfaces.IGateway import IGateway
from Code.Model.DatabaseConnection import DatabaseConnection
from Code.Model.DatabaseObjects.Customer import Customer


class CustomerGateway(IGateway):
    """

    Class is gateway between user and _database, contain all methods for controling db

    """
    def __init__(self):
        self._database = DatabaseConnection()

    def __str__(self):
        return ('customer','find by email')

    def find_by_email(self, customer):
        """

        Method find customer by his email address and return an full object of customer class.

        :param customer: data type of customer with only one parametr email
        :return: customer object
        """
        if isinstance(customer, Customer) == True:
            try:
                sql = "Select Jmeno,Prijmeni,Email,Telefon,Pohlavi from Zakaznik where Email=%s"
                tuple = (customer.email,)
                cursor = self._database.connection.cursor()
                cursor.execute(sql, tuple)
                result = cursor.fetchone()
                self._database.connection.commit()
                return Customer(result[0], result[1], result[2], result[3], result[4])
            except mysql.connector.errors.InternalError as e:
                print(f'customer with this e-mail {tuple[0]} wasnt found \n {e}')

        else:
            raise ValueError


    def insert(self, customer):
        """

        Method will insert in to _database a new instance of customer entity

        :param customer: data type of customer with only one parametr email
        :return: True if the creating of instance was succesfull
                 False if not
        """
        if isinstance(customer, Customer) == True:
            try:
                sql = 'Insert into zakaznik(Jmeno,Prijmeni,Email,Telefon,Pohlavi) values (%s,%s,%s,%s,%s)'
                data = (customer.name, customer.lastname, customer.email, customer.phone, customer.gender)
                self._database.cursor.execute(sql, data)
                if self._database.cursor.rowcount>0:
                    self._database.connection.commit()
                    return True
                else:
                    self._database.connection.rollback()
                    return False

            except mysql.connector.errors.IntegrityError:
                print('E-mail is already used')
                return

        else:
            raise ValueError

    def delete(self, customer):
        """

        Method will delete instance in customer table in _database by email.

        :param customer:

        :return: True if it was deleted successfully
                ,False if not
        """
        if isinstance(customer, Customer):
            sql_customer = 'Delete from zakaznik where Email=%s'
            sql_get_all_orders='Select objednavka.id from objednavka inner join zakaznik z on objednavka.FK_zakaznik = z.ID where z.Email=%s'
            sql_delete_connected_items='delete from vazba_objednavka_zbozi where FK_objednavka=%s'
            sql_delete_connected_orders="delete from objednavka where id=%s "

            data = (customer.email,)
            self._database.connection.start_transaction()
            self._database.cursor.execute(sql_get_all_orders, data)
            all_id=self._database.cursor.fetchall()
            for id in all_id:
                self._database.cursor.execute(sql_delete_connected_items, (id[0],))
                self._database.cursor.execute(sql_delete_connected_orders, (id[0],))
                
            self._database.cursor.execute(sql_customer, data)
            if self._database.cursor.rowcount>0:
                self._database.connection.commit()
                return True
            else:
                self._database.connection.rollback()
                return False
        else:
            raise ValueError

    def update(self, customer_old,customer_new):
        """

        Method will update instance in Entity Zakaznik

        :param customer_old:
        :param customer_new:
        :return:
        """
        if isinstance(customer_old,Customer)==True and isinstance(customer_new,Customer)==True:
            try:
                sql = 'Update zakaznik set Telefon=%s, Email=%s where Jmeno=%s and Prijmeni=%s and Email=%s'
                tuple = (customer_new.phone,customer_new.email,customer_old.name,customer_old.lastname,customer_old.email)
                self._database.cursor.execute(sql, tuple)
                if self._database.cursor.rowcount>0:
                    self._database.connection.commit()
                    return True
                else:
                    self._database.connection.rollback()
                    return False
            except:
                print("data wasnt updated")
        else:
            raise ValueError

    def get_id(self,email:str):
        """

        Method will get id of customer with email adress and return it

        :param email: Email 
        :return:
        """
        sql='Select zakaznik.id from zakaznik where zakaznik.email =%s'
        data=(email,)
        self._database.cursor.execute(sql, data)
        id= self._database.cursor.fetchone()
        self._database.connection.commit()
        return id

