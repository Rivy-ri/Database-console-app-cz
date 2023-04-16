class IGateway:
    """
    Gtaeway interface
    """

    def insert(self,object):
        raise NotImplemented
    def delete(self,object):
        raise NotImplemented
    def update(self,object_old,object_new):
        raise NotImplemented
