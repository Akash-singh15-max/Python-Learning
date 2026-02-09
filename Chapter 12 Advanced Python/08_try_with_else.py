try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("Try is successfull")

    # if our try statement run else also run,
    # if our try statement invalid else don't run.