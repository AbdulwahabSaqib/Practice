from abc import ABC, abstractmethod


class Arithmatic(ABC):
    @abstractmethod
    def disp (self):
        pass


class Addition(Arithmatic):
    def disp(self):
        print("Addition")


class Multiplication(Arithmatic):
    def disp(self):
        print("Multiplication")


class Subtraction(Arithmatic):
    def disp(self):
        print("Division")


class Division(Arithmatic):
    def disp(self):
        print("Division")


Plus = Addition()
Multiply = Multiplication()
Substract = Subtraction()
Divide = Division()

Plus.disp()
Multiply.disp()
Substract.disp()
Divide.disp()
