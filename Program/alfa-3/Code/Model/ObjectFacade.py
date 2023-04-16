from Code.Model.Gateway.CustomerGateway import CustomerGateway
from Code.Model.Gateway.OrderGateway import OrderGateway
class ObjectFacade:
    def __init__(self):
        self.customer=CustomerGateway()
        self.order=OrderGateway()


