from statistics import mean

class Coffee:
    all =[]

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    def __repr__(self):
        return f'Coffee(name = {self.name})'
    
    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, new_coffee_name):
        if not hasattr(self, 'name'):
            if isinstance(new_coffee_name, str) and len(new_coffee_name) >= 3:
                self._name = new_coffee_name
            else:
                raise Exception('Coffee name must be a string and at least three characters long')
        else:
            raise Exception('Name cannot be changed once created.')

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customer_set = set([order.customer for order in Order.all if order.coffee == self])
        return list(customer_set)
    
    def num_orders(self):
        if not self.orders():
            return 0
        else:
            return len(self.orders())
        
    def average_price(self):
        price_list = [order.price for order in Order.all if order.coffee == self]
        return mean(price_list)

class Customer:
    all =[]

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    def __repr__(self):
        return f'Customer(name = {self.name})'
        
    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, new_customer_name):
        if isinstance(new_customer_name, str) and 1 <= len(new_customer_name) <= 15:
            self._name = new_customer_name
        else:
            raise Exception('Customer name must be a string and be between one and fifteen characters long')

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        coffee_set = set([order.coffee for order in Order.all if order.customer == self])
        return list(coffee_set)
    
    def create_order(self, coffee, price):
       return Order(customer=self, coffee=coffee, price=price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.customers():
            return None
        else:
            big_spender = None
            high_total_spent = 0

            for customer in Customer.all:
                cust_total = sum([order.price for order in Order.all if order.customer == customer and order.coffee == coffee])
                if cust_total > high_total_spent:
                    high_total_spent = cust_total
                    big_spender = customer

            return big_spender
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def __repr__(self):
        return f'Order(customer = {self.customer.name}, coffee = {self.coffee.name}, price = {self.price})'
    
    @property
    def price (self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not hasattr(self, 'price'):
            if isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
                self._price = new_price
            else:
                raise Exception('Price must have a decimal value and be between 1.0 and 10.0')
        else:
            raise Exception('You cannot change the price once it is created.')
    
    @property
    def customer (self):
        return self._customer
    
    @customer.setter
    def customer (self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception('Customer must be a customer object')

    @property
    def coffee (self):
        return self._coffee
    
    @coffee.setter
    def coffee (self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception('Coffee must be a coffee object')