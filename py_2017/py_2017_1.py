# define function example
# review function definition

def add():
    """function example"""
    print(2 + 3)
    a = 'asd\'d'
    print(a)
    b = 'isn\'t " he said'
    print(b)
    result = b
    # review return value(s)
    return b  # to retuen single value is easy

# review class definition


class MyClass:
    """Class doc example"""
    a = "In class arg1"

    def myclass_func1(self):  # self is more like a modifier indicating a local var
        print(' f1 called')
        self.r = '1'
        print(self.r)

    def myclass_func2(self):
        print(' f2 called')
        self.r = "Self arg 2 "
        a = self.r + ' function2 var'
        print(a)

    def mycalss_func3(self, arg=[]):
        print(' f3 called')
        self.r = ['a']

        # arg.append(self.r) #here self.r reference is added, later r becomes ['a','a','a'], so we see that instead if['a']
        arg.append('a')  # here ['a'] reference is added, so we see ['a', 'a'] instead of more ['a','a','a'],
        # conclusion: Python is dangerous the arg reference is passed not value so it can be changed inside a function!!!

        self.r.append('a')
        self.r.append('a')
        print(self.r)
        print(arg)


class MyClass2:
    """Class doc example"""
    a = "In class arg1"

    def __init__(self):  # initialization method for a class, auto run when an instance
        self.r = 'i'

    def myclass_func1(self):  # self is more like a modifier indicating a local var
        print(' y f1 called')
        # self.r='1' #cannot do this # for MyClass because self.r is not initialized
        print(self.r)

    def myclass_func2(self):
        print(' y f2 called')
        self.r = "Self arg 2 "
        a = self.r + ' function2 var'
        print(a)

    def mycalss_func3(self, arg=[]):
        print(' y f3 called')
        self.r = ['a']


def func_x2(i):
    i=2*i
    return  i

# region Code folding region example:Visual Studio style
# method web method1
# review call functions
c = add()
# review class instantiation
x = MyClass()
x.myclass_func1()
x.myclass_func2()
q = ['q']
x.mycalss_func3(q)
x.mycalss_func3(q)
x.mycalss_func3(q)

# endregion

# cat_note
x = MyClass2()
x.myclass_func1()
x.myclass_func2()
q = ['q']
x.mycalss_func3(q)
x.mycalss_func3(q)
x.mycalss_func3(q)

# method
x = 'asd'
print(x)

par1=1
q=func_x2(par1)
print('result q='+q.__str__())
print('par1 ='+par1.__str__())