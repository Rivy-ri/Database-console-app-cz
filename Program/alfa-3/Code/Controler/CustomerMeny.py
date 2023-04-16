from Code.Model.DatabaseObjects.Customer import Customer
from Code.Model.ObjectFacade import ObjectFacade
from Code.Model.Workers.CustomerWorker import CustomerWorker


class CustomerMeny:
    def __init__(self):
        self.facade_customer=ObjectFacade().customer

    def Meny(self):
        """

        Method work as user control over _database, by using facade

        :return: void
        """
        result=input('Customer meny \n create new customer - 1 '
                     '\n delete customer - 2 \n update customer - 3 \n find by e-mail -4 \n import csv file - 5 \n return - 6')
        if result=='1':
            name=input('name for new customer: \n')
            lastname=input('lastname for new customer: \n')
            while True:
                email=input('email for new customer: \n')
                if Customer().valid_email_check(email)==True:
                    break
                else:
                    continue

            while True:
                phone = input('phone number for new customer: \n')
                if Customer().valid_phone_number(phone)==True:
                    break
                else:
                    continue

            while True:
                gender=input('gender choices(F,M,N) \n female-F \n male-M \n nonbinar-N')
                if gender.upper()=="F" or gender.upper()=='M' or gender.upper()=='N':
                    new_customer=Customer(name,lastname,email,phone,gender)
                    state=self.facade_customer.insert(new_customer)
                    if state==True:
                        print('Succesfuly inserted')
                        return

                    else:
                        print('something went wrong with insert')
                        return

                else:
                    continue

        elif result=='2':
            email=input('email of customer you want to delete')
            customer_to_delete=Customer(
                email=email
            )
            state=self.facade_customer.delete(customer_to_delete)
            if state==True:
                print('Succesfuly deleted')
                return
            else:
                print('nothing was deleted')
                return

        elif result == '3':
            old_name=input('Write yor name')
            old_lastname=input('write your lastname')
            old_email=input('write your email')
            old_customer=Customer(old_name,old_lastname,old_email)
            new_email=input('write your new email or old if you dont want to change it')
            new_phone=input('write your new phone number or old if you dont want to change it')
            new_customer=Customer(None,None,new_email,new_phone)
            state=self.facade_customer.update(old_customer,new_customer)
            if state==True:
                print('update was succesfull')
                return
            else:
                print('print update wasnt succesfull')
                return

        elif result == '4':
            email = input('email of customer you want to find')
            customer = Customer(
                email=email
            )
            state=self.facade_customer.find_by_email(customer)
            if isinstance(state,Customer)==True:
                print(str(state))
            else:
                print(state)

        elif result == '5':
            path=input('path to csv file example mycsv.csv')
            worker=CustomerWorker(path)
            list=worker.read_csv()
            worker.insert_list(list)
            return

        elif result == '6':
            return