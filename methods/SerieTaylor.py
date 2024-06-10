import sympy as sp
from math import factorial
"""
                Serie de taylor

datos de entrada: 
    f:funcion
    x0: punto entorno al cual se construye el polinomio
    n: grado del polinomio
"""
#funcion - punto inicial y grado de polinomio
def Serie_Taylor(f,x0,n):
    x = sp.symbols("x")
    polinomio = 0
    for k in range(1,n+1):
        df = sp.diff(f,x,k)
        dfx0 = df.subs(x,x0) #Solamente evalua un punto en la fución
        polinomio=polinomio+dfx0*(x-x0)**k/factorial(k)
    return polinomio





