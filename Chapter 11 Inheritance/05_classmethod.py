# class Employee:
#     a = 1
#     def show(self):
#         print(f"The class attribute of a is {self.a}")

# e = Employee()

# e.a = 45
# e.show()

# # Here output will 45 but we want class attribute to be print, here we use
# # @classmethod


class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()