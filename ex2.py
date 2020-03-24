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

    def

