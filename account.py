class Account:

    def __init__(self, name:str) -> None:
        """
        function to set up account object.
        ...
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        """
        function to set up deposit object
        :param amount: cannot deposit negative amount of money
        :return: False
        :param amount: amount add upon account balance
        :return: True
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True


    def withdraw(self, amount) -> bool:
        """
        :param amount: amount less then 0 or more than account balance
        :return: false

        :param amount: decrement amount to account balance
        :return: True
        """
        if amount <= 0 or amount >= self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> int:
        """
        :return: account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        :return: account name
        """
        return self.__account_name
