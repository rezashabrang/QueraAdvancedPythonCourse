import math
def get_func(ls):
    arF = []
    def sq(a):
        return a*a
    def rec(a, b):
        return a*b
    def tri(a, h):
        return a*h/2
    def cir(r):
        return math.pi*r*r
    for i in ls:
        if i =="square":
            arF.append(sq)
        elif i=="rectangle":
            arF.append(rec)
        elif i=="circle":
            arF.append(cir)
        elif i=="triangle":
            arF.append(tri)
    return arF
