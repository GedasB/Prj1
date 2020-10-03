class Calculator():

    def add(self, first=0, second=0):
        try:
            first = float(first)
            second = float(second)
        except ValueError:
             raise Exception("Can not evaluate to number")
        return (first + second)

    def substract(self, first=0.0, second=0.0):
        return first - second

    def multiply(self, first=0.0, second=0.0):
        return first * second

    def divide(self, first=0.0, second=1):
        if second == 0:
            raise Exception("Divide by Zero is forbidden")
        return first / second

    def power(self, first=0.0, second=0.0):
        return first ** second

#Calculator.add("2", "3b")

