a = 69

def func():
    global a # global keyword changed the value in global data
    a = 3
    print(a)

func()
print(a)