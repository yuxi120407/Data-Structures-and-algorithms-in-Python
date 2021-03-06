##def check_numb(numb):
##    if not (isinstance(numb, float) or isinstance(numb, int)):
##        raise ValueError('price should be a number')
    
class CreditCard:
    """A consumer credit card. """

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
            The initial balance is zero.
            customer the name of the customer (e.g., John Bowman )
            bank the name of the bank (e.g., California Savings )
            acnt the acount identifier (e.g., 5391 0375 9387 5309 )
            limit credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        self.check_positive_numb(price)       
            
        if price + self._balance > self._limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self.check_positive_numb(amount)
        
        self._balance -= amount

    ## Static methods are methods which are needed in a class but need not be part of any instance

    @staticmethod 
    def check_positive_numb(numb):
        if (not (isinstance(numb, float) or isinstance(numb, int))) or (numb < 0):
            raise ValueError('price should be a positive number')




if __name__ == '__main__':
    cc = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309 ', 1000)
    print(cc.charge(-100))

    print(cc.get_balance())
