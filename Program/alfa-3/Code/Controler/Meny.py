from Code.Controler.CustomerMeny import CustomerMeny
from Code.Controler.OrderMeny import OrderMeny
from Code.Controler.StatisticMeny import StatisticMeny
from Code.Model.Gateway.CustomerGateway import CustomerGateway
from Code.Model.Workers.ConfigurationWorker import ConfigurationWorker
from Code.Model.DatabaseConnection import DatabaseConnection


class Meny:
    """
    Class is the main controler for user
    """
    def __init__(self):
        self._server = ConfigurationWorker().get_data_from_cofiguration_file('host')
        self._database=ConfigurationWorker().get_data_from_cofiguration_file('database')
        ConfigurationWorker().get_data_from_cofiguration_file('password')
        ConfigurationWorker().get_data_from_cofiguration_file('user')
        self._run=True


    def start_program(self):
        """

        Method represent Main meny od app

        :return: void
        """
        print(f'ALFA 3 \n server:{self._server} \n database:{self._database}')
        while self._run==True:
            value=input('control:\n customer - 1\n order - 2 \n reports - 3 \n end of program - end')
            if value=='1':
                CustomerMeny().Meny()
            elif value=='2':
                email=input('customer email')
                customer=CustomerGateway().get_id(email)
                if customer==None:
                    print('Customer with email like that doesnt exist in _database')
                    continue
                else:
                 order_meny=OrderMeny(customer)
                 order_meny.Meny()
            elif value=='3':
                StatisticMeny().Meny()
                continue
            elif value=='end':
                self._run=False

            else:
                print(f' value {value} is not an opinion!\n try again')
                continue




