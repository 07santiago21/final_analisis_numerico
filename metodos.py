
"""

ceros

"""







import numpy as np
import sympy as sp


def biseccion(f, a, b, tol):
    if (f(a) * f(b) > 0):
        print("pailas")
        return

    contador = 0
    while abs(a - b) > tol:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        contador += 1

    print("Iteraciones bisección: ", contador)
    return c


def posicion_falsa(f, a, b, tol):
    if f(a) * f(b) > 0:
        print("pailas")
        return

    contador = 0
    while True:
        c = (a - f(a) * (a - b)) / (f(a) - f(b))

        if abs(f(c)) <= tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        contador += 1

    print("Iteraciones posición falsa: ", contador)
    return c


def secante(f, h0, h1, tol):
    h = [h0, h1]

    while abs(h[-1] - h[-2]) > tol:
        next_h = h[-1] - (f(h[-1]) * (h[-2] - h[-1])) / (f(h[-2]) - f(h[-1]))
        h.append(next_h)

        print(h[-1])

    return h[-1]


def newton(f, x0, tol, variable = None):
    if not variable:
      variable = sp.symbols('x')  # Define 'x' as a symbol

    df = sp.diff(f, variable)
    xv = [x0]

    next_x = sp.lambdify(variable, variable - f/df)

    while True:
        xv.append(next_x(xv[-1]))

        if abs(xv[-1] - xv[-2]) < tol:
            break

    return xv[-1]



"""
interpolacion y ajuste de curvas

"""


import numpy as np
import time

# Gauss-Seidel (sumatorias y matrices)
# Matrices
def Gauss_s(A, b, tolerancia):
  xo = [np.zeros(len(b))]
  D = np.diag(np.diag(A))

  L = D - np.tril(A)

  U = D - np.triu(A)

  tiempo_inicial = time.time()
  Tg = np.dot(np.linalg.inv(D - L) , U)

  Cg = np.dot(np.linalg.inv(D - L) , b)

  lam, vec =  np.linalg.eig(Tg)
  radio = max(abs(lam))

  if radio >= 1:
    print("El sistema iterativo no converge a la solución única del sistema")
    return

  contador = 0
  errores = []

  while True:
    contador += 1
    xo.append(np.dot(Tg, xo[-1]) + Cg)# aqui

    error = max(np.abs(xo[-2] - xo[-1]))
    errores.append(error)

    if error <= tolerancia:
      break

  tiempo_final = time.time()
  duracion = tiempo_final - tiempo_inicial

  return xo, duracion, errores


# Gauss-Seidel sumatorias
def Gauss_s_sumas(A, b, tol):
  cont = 0

  # Número máxima de iteraciones
  M = 50

  norm = float('inf') # Aleatorio, mayor a la tolerancia

  n = len(b)
  xo = np.zeros(n)
  x1 = np.zeros(n)

  x = [xo.copy()]

  tiempo_inicial = time.time()
  errores = []

  while (norm > tol and cont < M):
    for i in range(n):
      aux = 0
      for j in range(n):
        if i != j:
          aux = aux + A[i, j] * xo[j]
        x1[i] = (b[i] - aux) / A[i, i]

    norm = np.max(np.abs(x1 - xo))
    errores.append(norm)
    x.append(x1.copy())
    xo = x1.copy()

  tiempo_final = time.time()
  duracion = tiempo_final - tiempo_inicial

  return x, duracion, errores


# Eliminación Gaussiana
def eliminacion_gaussiana(A, b):
  n = len(b)

  for k in range(n-1):
    # TO DO: Si el pivote es cero cambiarlo al valor mayor en valor absoluto en la misma columna
    # TODO: Preguntar el TODO de arriba (a wilson)
    # Condicional
    # Línea de intercambio
    for i in range(k+1, n):
      lam = A[i, k] / A[k,k]
      A[i, k:n] = A[i, k:n] - lam * A[k, k:n]
      b[i] = b[i] - lam * b[k]


  x = np.zeros(n) # Crear un arreglo de n cantidad de ceros
  # Resolver las variables
  for k in range(n-1, -1, -1):
    # Ecuación general que surge de despejar la variable x_k en cada fila
    x[k] = (b[k] - np.dot(A[k, k+1:n], x[k+1:n]))/ A[k, k] # np.dot() producto punto entre dos matrices

  return x


"""
interpolacion y ajuste de curvas 

"""


import numpy as np
from typing import List, Union, Tuple
import sympy as sp
import matplotlib.pyplot as plt


def newton(f, x0, tol, variable = None):
    if not variable:
      variable = sp.symbols('x')  # Define 'x' as a symbol

    df = sp.diff(f, variable)
    xv = [x0]

    next_x = sp.lambdify(variable, variable - f/df)

    while True:
        xv.append(next_x(xv[-1]))

        if abs(xv[-1] - xv[-2]) < tol:
            break

    return xv[-1]




# Polinomial simple (interpolación) (usamos Gauss-Seidel)
def Pol_simple_2(x_data: Union[np.ndarray, List[float]], y_data: Union[np.ndarray, List[float]]) -> np.ndarray:
    n: int = len(x_data)
    M_p: np.ndarray = np.zeros([n, n])

    for i in range(n):
        M_p[i, 0] = 1
        for j in range(1, n):
            M_p[i, j] = M_p[i, j-1] * x_data[i]

    resultado: np.ndarray = np.linalg.solve(M_p, y_data)

    return resultado



# Convertir a polinomio (polinomial simple)
def Poly(a_i: List[float], ux: Union[int, float, np.ndarray]) -> Union[int, float, np.ndarray]:
    P: Union[int, float, np.ndarray] = 0
    for i in range(len(a_i)):
        P = P + a_i[i] * ux ** i
    return P


# --------

# Lagrange
def langrange_polinomio(x_d: List[float], y_d: List[float]) -> sp.Expr:
    x = sp.symbols('x')
    n = len(x_d)
    S = 0

    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L = L * ((x - x_d[j]) / (x_d[i] - x_d[j]))

        S += L * y_d[i]

    return sp.expand(S)


# Mínimos cuadrados
def minimos_cuadrados(Dx: np.ndarray, Dy: np.ndarray) -> Tuple[float, float]:
    n = len(Dx)
    Sx = sum(Dx)
    Sf = sum(Dy)
    Sfx = sum(Dx * Dy)
    Sx2 = sum(Dx ** 2)

    a0 = (Sf * Sx2 - Sx * Sfx) / (n * Sx2 - Sx ** 2)
    a1 = (n * Sfx - Sf * Sx) / (n * Sx2 - Sx ** 2)

    return a0, a1

#graficar polinomios
def plot_graph(Px: np.ndarray, Ty: np.ndarray, ux: np.ndarray, poly_values: Union[int, float, np.ndarray],
               xlabel: str, ylabel: str, title: str, label_data: str = 'Datos O', label_poly: str = 'Polinomio'):

    plt.plot(Px, Ty, 'vr', label=label_data)
    plt.plot(ux, poly_values, 'b', label=label_poly)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()


# transformar polinomios
def plot_transformed_data(x_a, y_p):
    plt.figure(figsize=(9, 9))

    # Plot original data
    plt.subplot(331)
    plt.plot(x_a, y_p, 'pb', label='Observados')
    plt.xlabel('Años')
    plt.ylabel('Poblacion')
    plt.legend()

    # Plot x squared
    plt.subplot(332)
    plt.plot(x_a * 2, y_p, 'dr', label='$x^2$')
    plt.legend()

    # Plot x cubed
    plt.subplot(333)
    plt.plot(x_a * 3, y_p, 'dr', label='$x^3$')
    plt.legend()

    # Plot square root of y
    plt.subplot(334)
    plt.plot(x_a, np.sqrt(y_p), 'dr', label='$\sqrt{y}$')
    plt.legend()

    # Plot 1 divided by the square root of y
    plt.subplot(335)
    plt.plot(x_a, 1. / np.sqrt(y_p), 'dg', label='$1/\sqrt{y}$')
    plt.legend()

    # Plot natural log of x
    plt.subplot(336)
    plt.plot(np.log(x_a), y_p, 'dc', label='$\log(x)$')
    plt.legend()

    # Plot natural log of x and y
    plt.subplot(337)
    plt.plot(np.log(x_a), np.log(y_p), 'dg', label='$\log(x) \log(y)$')
    plt.legend()

    # Plot natural log of y
    plt.subplot(338)
    plt.plot(x_a, np.log(y_p), 'db', label='$\log(y)$')
    plt.legend()

    # Plot y squared
    plt.subplot(339)
    plt.plot(x_a, y_p**2, 'dm', label='$y^2$')
    plt.legend()

    # Show plot
    plt.show()




"""

ecuaciones diferenciales

"""


# Método de Euler
def Euler(f, a, b, c0, h):
    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    yeu = [c0]
    for i in range(n):
        yeu.append(yeu[i] + h * f(t[i], yeu[i])) # reemplazar aqui runge kutta
    return t, yeu



def runge_kutta_4(f, a, b, c0, h):
    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    yeu = [c0]
    for i in range(n):
        k1 = h * f(t[i], yeu[i])
        k2 = h * f(t[i] + 0.5 * h, yeu[i] + 0.5 * k1 )
        k3 = h * f(t[i] + 0.5 * h, yeu[i] + 0.5 * k2)
        k4 = h * f(t[i] + h, yeu[i] + k3 )
        yeu.append(yeu[i] + ((k1 + 2 * k2 + 2 * k3 + k4))/ 6)
    return t, yeu




import ast
A_= "[-3., 2., 1.], [6., -8., -2.], [1., -1., -2.]"
A_string = f'[{A_}]'
A_M = ast.literal_eval(A_string)
list_of_lists = [[float(item) for item in sublist] for sublist in A_M]
A_M = np.array(list_of_lists)

print(A_M)



B_= "[2., 1., 3.]"
B_string = f'{B_}'
B_M = ast.literal_eval(B_string)
list_of_lists_B = [float(sublist) for sublist in B_M]
B_M = np.array(list_of_lists_B)
print(B_M)


