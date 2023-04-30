class Account:

    def __init__(self, name: str) -> None:
        """
        function to set up account object.
        ...
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        function to set up deposit object and amount cannot be less than 0
        :param amount: deposit amount into account balance
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True


    def withdraw(self, amount: float) -> bool:
        """
        function to withdraw money
        :param amount: withdraw amount from account balance
        :return: action of withdraw

        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        function to return account balance
        :param: get total account balance
        :return: action of left over amount
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        function should return account name
        :param: name should be in string type
        :return: account name
        """
        return self.__account_name
