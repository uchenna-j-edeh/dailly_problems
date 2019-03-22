# -*- coding: utf-8 -*-
"""
Where the object’s type is fixed, but we want to have several different ways to create it. This
is called a Simple Factory.
"""
import re

class Money:
    """ Imagine modeling a jar of coins. There are different ways oof specifying it. 
        Factory method can be useful in this instance
    """
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    @classmethod
    def money_from_pennies(cls, num_pennies):
        """
        Factory function that takes a single argument, returning
        an appropriate Money instance.
        """
        dollars, cents = divmod(num_pennies, 100)
        return cls(dollars, cents)

    @classmethod
    def money_from_string(cls, amount):
        """
        Another factory function, creating Money from a string amount. 
        Example, a string such as "$12.34"
        """
        match = re.search(r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
        assert match is not None, 'Invalid amount: {}'.format(amount)
        dollars = int(match.group('dollars'))
        cents = int(match.group('cents'))
        return cls(dollars, cents)

if __name__ == "__main__":
    money = Money.money_from_pennies(791)
    print('You got ${0}.{1}'.format(money.dollars, money.cents))
