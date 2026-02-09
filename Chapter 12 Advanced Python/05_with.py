# we can use multile context manager in a single with
with(
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    a = f1.read()
    b = f2.read()
    print(a,b)