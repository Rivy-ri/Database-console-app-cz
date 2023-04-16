from Code.Interfaces.ICommand import ICommand
from Code.Model.DatabaseConnection import DatabaseConnection


class MostPopularProducts(ICommand):
    def __init__(self):
        self._database=DatabaseConnection()

    def get_report(self):
        sql='Select * From MostPopularAndPositiveProducts'
        self._database.cursor.execute(sql)
        list=self._database.cursor.fetchall()
        self._database.connection.commit()
        return list