def a():
    print("Start of a()")
    b()  # Call b().

def b():
    print("Start of b()")
    c()  # Call c().

def c():
    print("Start of c()")
    42 / 0  # This will cause a zero divided error.

a()  # Call a().
