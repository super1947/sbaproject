class Smartphone:
    def __init__(self, brand, details):
        self._brand = brand
        self._details = details

    def __str__(self):
        return f'str : {self._brand} - {self._details}'

    def __repr__(self):
        return f'repr : {self._brand} - {self._details}'


Smartphone1 = Smartphone('Iphone', {'color': 'White', 'price': 10000})
Smartphone2 = Smartphone('Galaxy', {'color': 'Black', 'price': 8000})
Smartphone3 = Smartphone('Blackberry', {'color': 'Silver', 'price': 6000})

print(Smartphone1)
print(Smartphone1.__dict__)
print(Smartphone2.__dict__)
print(Smartphone3.__dict__)


# ID 확인 : 숫자가 모두 다름
print(id(Smartphone1))
print(id(Smartphone2))

print(Smartphone1._brand == Smartphone2._brand)
print(Smartphone1 is Smartphone2)

Smartphone_list = ['Iphone', 'Galaxy', 'Blackberry']
for x in Smartphone_list:
    print(repr(x))
    print(x)

print(Smartphone.__doc__)
