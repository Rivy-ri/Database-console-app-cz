import datetime
import random
from enum import Enum


class Order:
    def __init__(self,creation_date:datetime.date=None,date_of_payment:datetime=None,owner:int=None,set_tracert_number:int=0):
        self.creation_date=creation_date
        self.date_of_payment=date_of_payment
        self._state_of_order=StatesOfOrder.obdrzena
        self._payment_state=False
        if set_tracert_number==0:
            self._tracer_number=self._create_tracet_number()
        else:
            self._tracer_number =set_tracert_number
        self.owner=owner
        self.order_items=[]

    def __str__(self):
        text_part_one=f'Order number:{self._tracer_number} \n created:{self.creation_date} \n day of payment: {self.date_of_payment}\n '
        if self._payment_state==False:
            text_part_tow='Not payed yet'
        else:
            text_part_tow='Is payed'

        return text_part_one+text_part_tow
    @property
    def state_of_order(self):
        return self._state_of_order

    @state_of_order.setter
    def state_of_order(self, specific_state):
        if specific_state == 'add':
            new_value = int(StatesOfOrder[self._state_of_order].value) + 1
            try:
                if new_value < 5:
                    self._state_of_order = StatesOfOrder(new_value).name
                else:
                    raise ValueError('the order is in last stage')
            except ValueError as ve:
                return ve
        else:
            self._state_of_order = specific_state


    @property
    def tracer_number(self):
        return self._tracer_number

    @tracer_number.setter
    def tracer_number(self,new_tracert_number):
        self._tracer_number=new_tracert_number



    def _create_tracet_number(self):
        """

        Method creaet number of order

        :return:
        """
        random_number=random.randrange(1000000)
        number=int(self.creation_date.year)+int(self.creation_date.day)+random_number
        if number%4:
            number=number/4

        else:
            number=number/3

        return int(number)

    def add_product_into_order(self,product):
        if product not in self.order_items:
            self.order_items.append(product)
            return True
        else:
            return False

    def delete_from_order(self,product):
        for item in self.product_items:
            if item.name == product.name:
                self.product_items.remove(item)
                return True
            else:
                continue
            return False



class StatesOfOrder(Enum):
    obdrzena=1
    pripravena=2
    odeslana=3
    k_vyzvednuti=4