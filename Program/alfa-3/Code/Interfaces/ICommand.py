class ICommand:
    """
    Interface for statistic that work as command pattern
    """
    def get_report(self):
        """
        method that return statistic from _database
        :return:
        """
        raise NotImplementedError