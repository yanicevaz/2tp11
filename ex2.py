class Complex:
    def __init__(self,re,im):
        self.__reel = re
        self.__imaginaire = im

    def __add__(self, complex1):
        return Complex(self.__reel+complex1.__reel,self.__imaginaire+complex1.__imaginaire)

    def __sub__(self,complex1):
        return Complex(self.__reel-complex1.__reel,self.__imaginaire-complex1.__imaginaire)

    def __mul__(self,complex1):
        return Complex(self.__reel*complex1.__reel,self.__imaginaire*complex1.__imaginaire)

    def __truediv__(self,complex1):
        return Complex(self.__reel/complex1.__reel,self.__imaginaire/complex1.__imaginaire)

    def __abs__(self):
        return (self.__reel**2 + self.__imaginaire**2) ** (1/2)

    def __eq__(self, complex1):
        return (self.__reel == complex1.__reel) and (self.__imaginaire == complex1.__imaginaire)

    def __ne__(self, complex1):
        return (self.__reel != complex1.__reel) or (self.__imaginaire != complex1.__imaginaire)

    def __str__(self):
        return (str(self.__reel)  + " + "+ str(self.__imaginaire)+"i")
if __name__ == "__main__":
    cplx1 = Complex(1, 1)
    cplx2 = Complex(2, 2)
    print(cplx1 + cplx2)
    print(cplx1 - cplx2)
    print(cplx1 * cplx2)
    print(cplx1 / cplx2)
    print(abs(cplx1))
    print(cplx1 == cplx2)
    print(cplx1 != cplx2)
