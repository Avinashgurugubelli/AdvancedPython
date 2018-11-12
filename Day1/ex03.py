'''
module exo3

working with inheritance in python
Note:- 
single underscore - example: _id :- protected variable
double underscore - example: __id :- private variable

No specific polymorphism in python because there no explicit declaration of variable like string, float etc..
'''

class Person(object):
    def __init__(self, **kwargs):
        self._name = kwargs.get('name')
        self._email = kwargs.get('email')
        print ('person __init__() called')

    def __str__(self):
        return 'Person [Name= {}, Email = {}]' .format(self._name, self._email)

class Resource(object):
    def __init__(self, **kwargs):
        self._id = kwargs.get('id')
        self._location = kwargs.get('location')
        print ('Resource __init__() called')
    def __str__(self):
         return 'Resource [Id= {}, Location = {}]'.format(self._id, self._location)

# Multiple Inheritance
class Employee(Person, Resource):
    def __init__(self, **kwargs):
        # super().__init__( **kwargs) by default it will call the person because it is the first inherited
        Person.__init__(self, **kwargs)
        Resource.__init__(self, **kwargs)

    def __str__(self):
        return 'Employee [Id= {}, Location = {}, Name= {}, Email = {}]' .format(self._id, self._location, self._name, self._email)


def main():
    e1 = Employee(name = 'Avinash', email = 'avi@gmail.com', location = 'Bangalore', id = 1234)
    # print (dir(e1))
    print(e1)

if __name__ == "__main__":
    main()