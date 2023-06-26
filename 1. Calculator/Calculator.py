class Calculator:
    def __init__(self, input_numbers):
        self.numbers = input_numbers

    def data_input(self):
        self.data = [int(input("Data input: " + str(i + 1) + " = "))
                     for i in range(self.numbers)]


class BasicOperations(Calculator):
    def addition(self):
        n1, n2 = self.data
        return n1 + n2

    def subtraction(self):
        n1, n2 = self.data
        return n1 - n2

    def multiplication(self):
        n1, n2 = self.data
        return n1 * n2

    def division(self):
        n1, n2 = self.data
        return n1 / n2


set1 = BasicOperations(2)
set1.data_input()

print(set1.addition())
print(set1.multiplication())
