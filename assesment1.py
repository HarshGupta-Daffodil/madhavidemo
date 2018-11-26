# Write a function that is using generator expression for printing square of first 10 number.
def print_square():
    sqr_num=(x**2 for x in range(1,11))
    #iterate using for loop
    for sq in sqr_num:
        print(sq)
    #iterate using while Loop
    while True:
        try:
            print(next(sqr_num))
        except StopIteration:
            break    

print_square()    

#Write a generator function that can return a series of number passed into function.

def get_series(a,b):
    while a<b:
        yield a
        a+=1

for a in get_series(1,10):
    print(a)

# Create a custom decorator in python that can log the class name and the arguments passed into it to the console    
class CustomDecorator:
    def __init__(self,func):
        self.func=func

    def __call__(self,*args):
        print("class name is {} and arguments passed into it are {}".format(self.__class__.__name__,args))

@CustomDecorator
def print_(x,y):
    return x,y

print_("arg1","arg2")
print_("arg1","agr2","arg3","arg4")










