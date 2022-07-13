def foo():
    print("currently inside foo!")

def bar():
    print("currently inside bar!")

def add_and_print(x, y):
    print(x + y)

def say_hello_to(name):
    print("hello " + name)

def add_and_return(x, y):
    return x + y

def say_hello_to_except_Alex(name):
    if name == "Alex":
        return 
    else: 
        return "Hello, " + name

def add_to_6(x):
    val = 6
    return x + val

def hello_default(name='bill', location='boston'):
    print("Hello, " + name + " you must be from " + location + "!")

print("not in any function")
bar()
foo()
print("not in any function")
add_and_print(4,5)
say_hello_to("john")
val = add_and_return(6,8)
print(val)
print(say_hello_to_except_Alex("Alex"))
print(say_hello_to_except_Alex("bob"))
print(add_to_6(5))
hello_default()
hello_default(name='john')
hello_default(location="nj")