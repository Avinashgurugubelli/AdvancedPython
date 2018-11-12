'''
module exo1

example of creating and using classes in python
'''

class Book:
    __publisher = 'Avinash' # Not recommended to have as property unless it's shared data
    # constructor
    # __init__ is a special function automatically called by python when the obj is newly created
    def __init__(self, **kwargs):
        self.__title = kwargs.get('title')
        self.__price = kwargs.get('price')
        if kwargs.get('publisher') != None:
            self.__publisher = kwargs.get('publisher')

        # print ('id of self is {}'.format(id(self)))

    # this is a user defined function, to be called using an obj's ref ex:- b1.print_info()
    # python passes b1 to the function os first argument
    # implicitly (like book.print_info(b1))
    def print_book_info(self):
        print ('info about book')
        # print('Title      =', self.__title)
        # print ('Price     =', self.__price)
        # print('publisher  =', self.__publisher)
        print(self.__str__())
    def __str__(self):
        return 'Book [Title ={}, price ={}, publisher ={}]'.format(self.__title, self.__price, self.__publisher)
def book_test():
    b1 = Book(title='let us c', price=299)
    b2 = Book(title = 'let us c', price =299, publisher = 'some other author')
    # print ('id of b1 is {}'.format(id(b1)))
    # print ('type of b1 is {}'.format(type(b1)))
    print('book one details')
    b1.print_book_info()
    print('-----------------------------')
    print('book two details')
    b2.print_book_info()
    # print ('attributes of b1...')
    # print (dir(b1))

if __name__ == "__main__":
    book_test()
    