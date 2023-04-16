import datetime
from Code.Interfaces.IGateway import IGateway
from Code.Model.DatabaseConnection import DatabaseConnection
from Code.Model.DatabaseObjects.Order import Order

class OrderGateway(IGateway):
    """
    Class represent comunication with _database
    """
    def __init__(self):
        self._database = DatabaseConnection()

    def __str__(self):
        return 'order'

    def insert(self,order):
        """

        Method will insert order object in to _database.

        :param order: object type of Order class that will be inserted
        :return: bool, True if it was inserted False if not
        """
        if isinstance(order,Order)==True:
            sql_order_insert='insert into objednavka ' \
                             '(Datum_tvorby, Zaplaceno,' \
                             ' Datum_uhrady, Stav,' \
                             ' FK_zakaznik,Trasovaci_cislo)' \
                             ' values (%s,%s,%s,%s,%s,%s)'

            sql_product_insert='Insert into vazba_objednavka_zbozi' \
                               '( Pocet_ks, FK_objednavka, FK_zbozi)' \
                               ' values (%s,%s,%s)'

            sql_get_product_id='select zbozi.ID from zbozi where Nazev=%s '

            data_order = (
            order.creation_date, order._payment_state,
            order.date_of_payment, order.state_of_order.name,
            order.owner[0],order._tracer_number)

            self._database.connection.start_transaction()
            self._database.cursor.execute(sql_order_insert, data_order)
            order_id=self.get_id(order.tracer_number)[0]
            for product in order.order_items:
                self._database.cursor.execute(sql_get_product_id, (product[0],))
                product_id=self._database.cursor.fetchone()[0]
                data=(product[1],order_id,product_id)
                self._database.cursor.execute(sql_product_insert, data)
            if self._database.cursor.rowcount>0:
                self._database.connection.commit()
                return True
            else:
                self._database.connection.rollback()
                return False

        else:
            raise ValueError


    def delete(self,order):
        """

        Method will delete order from _database and all items that beloget to it

        :param order: order that contains just Tracert number
        :return: bool, True if deleted or False if not
        """
        if isinstance(order, Order) == True:
            sql_delete_order = 'delete from objednavka where Trasovaci_cislo=%s'
            sql_delete_order_items='delete vazba_objednavka_zbozi ' \
                                   'from vazba_objednavka_zbozi ' \
                                   'inner join objednavka' \
                                   ' on vazba_objednavka_zbozi.FK_objednavka = objednavka.ID ' \
                                   'where Trasovaci_cislo=%s'

            data = (order._tracer_number,)
            self._database.connection.start_transaction()
            self._database.cursor.execute(sql_delete_order_items, data)
            self._database.cursor.execute(sql_delete_order, data)
            if self._database.cursor.rowcount>0:
                self._database.connection.commit()
                return True
            else:
                self._database.connection.rollback()
                return False
        else:
            raise ValueError

    def update(self,tracert_number,order_new):
        """

        Method will just update 'head' of order
        :param tracert_number: number by which  is order found
        :param order_new: new parametrs of order
        :return: boolean, true if updated false if not
        """
        if isinstance(order_new,Order):
            sql='update objednavka set Stav=%s, Zaplaceno=%s where  Trasovaci_cislo=%s'
            data=(order_new.state_of_order,order_new._payment_state,tracert_number)
            self._database.cursor.execute(sql, data)
            if self._database.cursor.rowcount>0:
                self._database.connection.commit()
                return True
            else:
                return False
        else:
            raise ValueError

    def update_items_in_order(self,order_old,order_new):
        """

        Method will update intems of an order

        :param order_old: the original order items
        :param order_new: the order with updated items
        :return: True if updated, False if not
        """
        if isinstance(order_old, Order) == True and isinstance(order_new, Order):
            delete_items=set(order_old.order_items)-set(order_new.order_items)
            insert_items=set(order_new.order_items)-set(order_old.order_items)
            id_of_order= self.get_id(order_old.tracer_number)
            self._database.connection.start_transaction()
            sql_delete='Delete vazba_objednavka_zbozi from vazba_objednavka_zbozi inner join zbozi on vazba_objednavka_zbozi.FK_zbozi = zbozi.ID where FK_objednavka=%s and zbozi.Nazev=%s'
            sql_insert ='Insert into vazba_objednavka_zbozi (pocet_ks, fk_objednavka, fk_zbozi)Select %s,%s,(Select ID as zbozi_ID from zbozi where zbozi.Nazev=%s)'
            for item_to_delete in delete_items:
                self._database.cursor.execute(sql_delete, (id_of_order, item_to_delete.name))
            for item_to_inser in insert_items:
                self._database.cursor.execute(sql_insert, (item_to_inser[1], id_of_order[0], item_to_inser[0]))
            if self._database.cursor.rowcount>0:
                self._database.connection.commit()
                return True
            else:
                self._database.connection.rollback()
                return False
        else:
            raise ValueError


    def get_id(self, tracer_number):
        """

        will get id of order by tracer number of order
        :param tracer_number: tracer number of order for which i want to get id
        :return: id
        """
        sql='SELECT objednavka.ID From objednavka where objednavka.Trasovaci_cislo=%s'
        data=(tracer_number,)
        self._database.cursor.execute(sql, data)
        id=self._database.cursor.fetchone()
        self._database.connection.commit()
        return id



    def find_by_tracer_number(self,tracert_number,user_ID):
        """

        Method will get full information about order from _database and return it

        :param order: order for which i want to get information
        :return: order object
        """
        sql='select objednavka.Trasovaci_cislo ' \
            ',objednavka.Datum_tvorby ' \
            ',objednavka.Datum_uhrady' \
            ',objednavka.Zaplaceno' \
            ' ,objednavka.Stav ' \
            'from objednavka' \
            ' inner join zakaznik z on objednavka.FK_zakaznik = z.ID' \
            ' where Trasovaci_cislo=%s and z.ID=%s'

        data=(tracert_number,user_ID)
        cursor=self._database.cursor
        cursor.execute(sql,data)
        result=cursor.fetchone()
        self._database.connection.commit()
        if result == None:
            return None
        else:
            order= Order(
                creation_date=result[1],
                date_of_payment=result[2],
                set_tracert_number=int(result[0])
            )
            order._payment_state=result[3]
            order.state_of_order=result[4]
            return order




    def get_all_products(self):
        """

        Method will get all products from _database and return them

        :return: data tuple
        """
        sql='Select zbozi.Nazev,Cena_ks_Euro,Typ,Strih, v.Nazev from zbozi inner join vyrobce v on zbozi.FK_vyrobce = v.ID'
        self._database.cursor.execute(sql)
        data=self._database.cursor.fetchall()
        self._database.connection.commit()
        return data

    def get_all_information_about_order(self,tracert_number,user_id):
        """

        :param tracert_number:
        :return:
        """
        sql='Select z.Nazev, voz.Pocet_ks ' \
            'From objednavka ' \
            'inner join vazba_objednavka_zbozi voz on objednavka.ID = voz.FK_objednavka' \
            ' inner join zbozi z on voz.FK_zbozi = z.ID ' \
            'inner join zakaznik  on objednavka.FK_zakaznik = zakaznik.ID' \
            ' where objednavka.Trasovaci_cislo=%s and zakaznik.ID=%s'
        self._database.cursor.execute(sql, (tracert_number, user_id))
        data=self._database.cursor.fetchall()
        self._database.connection.commit()
        if len(data)==None:
            return None
        else:
            return data




