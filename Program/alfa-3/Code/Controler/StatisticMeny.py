from Code.Model.StatisticCommands.MostPopularProduct import MostPopularProducts
from Code.Model.StatisticCommands.UnitsSoldByProducer import UnitsSoldByProducer
from prettytable import PrettyTable


class StatisticMeny:
    """
    Class represent user control to get statistic from _database
    """
    def Meny(self):
        """

        Method represen user controler

        :return:
        """
        while True:
            selection=input('Select which report you want to see \n by number of sold items from producer - 1'
                            '\n by most buyed items and theyr rewiev - 2')
            if selection =='1':
                report=UnitsSoldByProducer().get_report()
                table=PrettyTable(['Name of company',' Number of sold units'])
                for item in report:
                    table.add_row(item)
                print(table)
                return

            elif selection=='2':
                report=MostPopularProducts().get_report()
                table=PrettyTable(['product name','number of bought items','avg review'])
                for item in report:
                    table.add_row(item)
                print(table)
                return

            else:
                print('wrong input')
                continue
