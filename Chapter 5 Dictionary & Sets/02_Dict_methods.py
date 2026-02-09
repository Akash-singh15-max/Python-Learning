# marks = {} # empty dictonary
# print(type(marks))

marks = {
    "Akash": 100,
    "Sumit": 69,
    "Vishal": 90,
    0: "Harry"
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Akash": 99, "Renuka": 100})
print(marks)

print(marks.get("lucky"))

print(marks.get("Akash"))

print(marks.get("Akash2")) # prints none 
print(marks["Akash2"]) # return an error