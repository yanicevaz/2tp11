class Cercle:
    def __init__(self,r):
        self.__rayon = r

    def __add__(self, r1):
        return Cercle(self.__rayon+r1.__rayon)

    def __lt__(self, r1):
        return self.__rayon < r1.__rayon

    def __gt__(self, r1):
        return self.__rayon > r1.__rayon

if __name__ == "__main__":
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)
