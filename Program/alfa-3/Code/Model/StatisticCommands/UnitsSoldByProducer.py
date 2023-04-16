from Code.Interfaces.ICommand import ICommand
from Code.Model.DatabaseConnection import DatabaseConnection


class UnitsSoldByProducer(ICommand):
    def __init__(self):
        self._database =DatabaseConnection()
    def get_report(self):
        sql='Select * from pocet_prodanych_ks_podle_vyrobce'
        self._database.cursor.execute(sql)
        list_for_results= self._database.cursor.fetchall()
        self._database.connection.commit()
        return list_for_results



