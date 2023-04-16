import datetime

from Code.Model.ObjectFacade import ObjectFacade
from Code.Model.DatabaseObjects.Order import Order
from prettytable import PrettyTable


class OrderMeny:
    """

    Class reperesent user controler over orders in shape of user meny

    """
    def __init__(self,user):
        self.order=ObjectFacade().order
        self.user_id=user

    def Meny(self):
        """

        Method start meny tahat's controled by user

        :return: void
        """
        result=input('Order meny'
                     '\n create new order - 1 '
                     '\n update order - 2'
                     '\n update items in order - 3'
                     '\n write  order and items - 4'
                     '\n delete order - 5'
                     )
        if result=='1':
            create_date=datetime.date.today()
            payment_date=create_date+datetime.timedelta(days=14)
            new_order=Order(
                creation_date=create_date,
                date_of_payment=payment_date,
                owner=self.user_id
            )
            while True:
                print('select product and write amount in this format: product,1 ')
                products=self.order.get_all_products()
                table=PrettyTable(['Name','Price in EU','Type','gender','creator'])
                for product in products:
                    table.add_row(product)
                table.title='Our products we can offer'
                print(table)
                want_to_add=True
                while want_to_add == True:
                    item = input('add item from collection').split(',')
                    item_exists = False
                    for product in products:
                        if product[0] == item[0]:
                            try:
                                quantity = int(item[1])
                                if quantity <= 0:
                                    raise ValueError
                                item_exists = True
                                new_order.add_product_into_order((item[0], quantity))
                                break
                            except ValueError:
                                print("Invalid quantity entered")
                                break
                    if not item_exists:
                        print('Item not found in collection')
                        continue
                    result = input('wana add more? y/n')
                    if result == 'y':
                        continue
                    elif result == 'n':
                        state = self.order.insert(new_order)
                        if state == True:
                            print('Order was succesfully created')
                            return
                        else:
                            print('Order wasn created, something went wrong')
                            return



        elif result=='2':
            tracer_number=input('what is tracert number of your order?')
            order = self.order.find_by_tracer_number(int(tracer_number),self.user_id[0])
            if order!=None:
                while True:
                    choice=input('what do you want to change\n status with the carrier by one stage - 1 \n set payment status on true - 2')
                    if choice=='1':
                        order.state_of_order='add'
                        break
                    elif choice=='2':
                        order._payment_state=True
                        break
                    else:
                        print('wrong input')
                        continue
            state=self.order.update(int(tracer_number),order)
            if state == True:
                print('sucessfuly updated')
            else:
                print('something went wrong with update')


        elif result=='3':
            tracert_number = input("Enter the trace number of the order you want to change: ")
            items = self.order.get_all_information_about_order(tracert_number, self.user_id)
            new_order = items.copy()
            table = PrettyTable(["Item name", "Amount"])
            for item in items:
                table.add_row(item)
            table.title=f'Order {tracert_number} details '
            print(table, end=' ')

            products = self.order.get_all_products()
            table = PrettyTable(['Name', 'Price in EU', 'Type', 'grnder', 'creator'])
            for product in products:
                table.add_row(product)
            table.title='Our products we can offer'
            print(table)

            while True:
                value = input("To insert a new item, use the syntax: name_of_item,new_amount. \n"
                              "To delete an item, use the syntax: name_of_item,0. \n"
                              "To end changing items, type 'end': ")
                if value == 'end':
                    original_order = Order(None, None, self.user_id, int(tracert_number))
                    original_order.order_items = items
                    altered_order = Order(None, None, None, int(tracert_number))
                    altered_order.order_items = new_order
                    state = self.order.update_items_in_order(original_order, altered_order)
                    if state:
                        print('Changes in order were successful.')
                        break
                    else:
                        print('Something went wrong during the change.')
                        break
                else:
                    item_name, item_amount = value.split(',')
                    item_amount = int(item_amount)
                    if item_amount == 0 and (item_name, 0) in new_order:
                        new_order.remove((item_name, 0))
                    elif item_amount >= 1 and (item_name, item_amount) not in new_order:
                        new_order.append((item_name, item_amount))



        elif result=='4':
            tracert_number = input("Enter the trace number of the order to show details of the order ")
            order=self.order.find_by_tracer_number(int(tracert_number),self.user_id[0])
            data=self.order.get_all_information_about_order(int(tracert_number),self.user_id[0])
            table=PrettyTable(['name of product', 'ordered amount'])
            for row in data:
                table.add_row(row)

            table.title=str(order)
            print(table)
            return


        elif result=='5':
            tracert_number=input('tracert number of order')
            state=self.order.delete(tracert_number)
            if state == True:
                print('order was sucessfuly deleted')
            else:
                print('order wasnt sucessfuly deleted')