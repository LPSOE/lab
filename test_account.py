import pytest
from account import *

class Test:

    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        # negative, zero, positive
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(1.5) is True
        assert self.a1.get_balance() == pytest.approx(1.5, abs=0.01)

    def test_withdraw(self):
        # negative, zero, positive invalid, positive valid

        assert self.a1.withdraw(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0

        self.a1.deposit(10)
        assert self.a1.withdraw(20) is False
        assert self.a1.get_balance() == 10

        assert self.a1.withdraw(1.5) is True
        assert self.a1.get_balance() == 8.5
