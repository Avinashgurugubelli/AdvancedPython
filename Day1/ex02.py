'''
module ex02

working with properties in class
'''

class Book:
    def __init__(self, **kwargs):
        self.__title = kwargs.get('title')
        self.__price = kwargs.get('price')
        self.__author = kwargs.get('author')

    def __str__(self):
        return 'Book [Title ={}, Price ={}, Author ={}]'.format(self.__title, self.__price, self.__author)

    # Getter for title
    @property
    def title(self):
        return self.__title

    #  Setter for title
    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if type(value) not in (int, float):
            raise TypeError('Invalid type for price; only int and float allowed')
        if value <= 0:
            raise ValueError('invalid value for price; must be >0')
        self.__price = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    '''
    __iadd__ corresponding to the += operator
    left hand side of the operator is the invoking object
    right hand side is the value
    also this function must return the invoking object
    '''
    def __iadd__(self, value):
        if type(value) in (int, float):
            self.price += value
        elif type(value) == str:
            self.title += value
        return self
    # Other operator functions:
        # followinf functions should return the invoking objects
        # __isub__, __imul__, __idiv__, __imod__  --> -=, *=, /=, %=
    #  following functions should return the result of respective operation
        # __add__, __sub__, __mul__, __div__, __mod__ --> +, -, *, / , %
    #  following functions should return true or false
        # __gt__, __ge__, __lt__, __le__, __eq__, __ne__ ->> >, >=, <, <=, ==, !
def main():
    b1 = Book(title='Angular 4', author='Avinash', price=300)
    print (b1)
    print ('Title  =', b1.title) # Invokes the title() function
    print ('Price  =', b1.price)
    print ('Author  =', b1.author)

    b1.title = 'Angular 6'
    b1.price = 600
    b1.author = 'Avinash Gurugubelli'
    print (b1)
    b1 += 100 # this will work because of __iadd__ or else we should write b1.price += 100 
    print (b1)
if __name__ == "__main__":
    main()
