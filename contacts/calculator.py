class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


if __name__ == '__main__':
    calc = Calculator(4, 6)  # num1 = 4, num2 = 6
    sumResult1 = calc.sum()
    sumResult2 = calc.sub()
    sumResult3 = calc.mul()
    sumResult4 = calc.div()

    print(f'덧셈결과 : {sumResult1}')
    print(f'뺄셈결과 : {sumResult2}')
    print(f'곱셈결과 : {sumResult3}')
    print(f'나눗셈결과 : {sumResult4:.3f}')
