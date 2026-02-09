def myfunc():
    print("Hello from module function")
myfunc()

if __name__ == "__main__":
    # if this code is directly executed by running the file it's present in
    print("We are directly running this code")
    myfunc()
    print(__name__)