def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(add(3,4,6))


def calculate(**kwargs):
    print(kwargs)

calculate(add =3,multiply=5)


class Car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw["model"]
