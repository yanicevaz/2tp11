class Rational:
    def __init__(self,numerateur,denumerateur):
        self.__num = numerateur
        if denumerateur == 0:
            print( f"Le denumerateur est nul")
        else:
            self.__denum = denumerateur

    def __add__(self, frac1):
        if self.__denum == frac1.__denum:
            return Rational(self.__num + frac1.__num, self.__denum)
        else:
            num = self.__num * frac1.__denum + frac1.__num * self.__denum
            denum = self.__denum * frac1.__denum
            return Rational(num,denum)
    def __sub__(self, frac1):
        if self.__denum == frac1.__denum:
            return Rational(self.__num - frac1.__num, self.__denum)
        else:
            num = self.__num * frac1.__denum - frac1.__num * self.__denum
            denum = self.__denum * frac1.__denum
            return Rational(num,denum)

    def __mul__(self, frac1):
        return Rational(self.__num * frac1.__num, self.__denum * frac1.__denum)

    def __str__(self):
        return (f"le rationnel est {self.__num} / {self.__denum}")


ratio1 = Rational(3,1)
ratio2 = Rational(4,2)
print(ratio1)
print(ratio2)
print(ratio1+ratio2)
print(ratio1-ratio2)
print(ratio1*ratio2)
