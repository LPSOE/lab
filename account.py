class Account:

    def __init__(self, name:str) -> None:
        """
        function to set up account object.
        ...
        :param name: Account name
        """
        self.__account_name = "John"
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        """
        function to set up deposit object
        :param amount: cannot deposit negative amount of money
        :return: False

        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True


    def withdraw(self, amount) -> bool:
        if amount <= 0 or amount >= self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
