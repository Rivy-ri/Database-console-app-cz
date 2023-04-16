import os
import csv

from Code.Model.DatabaseObjects.Customer import Customer
from Code.Model.ObjectFacade import ObjectFacade


class CustomerWorker:
    def __init__(self, path):
        """
        Initialize the CustomerWorker class with a path to a CSV file.

        :param path: the path to the CSV file to read.
        """
        if os.path.exists(path) and '.csv' in path:
            self.path = path
        else:
            raise ValueError

    def read_csv(self):
        """
        Read the CSV file, process each row, and return a list of Customer objects.
        """
        with open(self.path) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            items = []
            for row in reader:
                if row:
                    new_customer = Customer(
                        name=row[0],
                        lastname=row[1],
                        email=row[2],
                        phone=row[3],
                        gender=row[4],
                    )
                    items.append(new_customer)
            return items

    def insert_list(self, customer_list):
        """
        Insert a list of Customer objects into the _database.

        :param customer_list: the list of Customer objects to insert.
        """
        failed = 0
        successful = 0
        for customer in customer_list:
            try:
                state = ObjectFacade().customer.insert(customer)
                if state:
                    successful += 1
                else:
                    failed += 1
            except Exception as e:
                print(f"Error inserting customer: {e}")
                failed += 1

        print(f'Successful inserts: {successful}\nFailed inserts: {failed}')
        return



