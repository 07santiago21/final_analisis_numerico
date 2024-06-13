
import numpy as np
import time

# Gauss-Seidel (sumatorias y matrices)
# Matrices
def Gauss_s(A, b, tolerancia= 1e-5):
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
    return "El sistema iterativo no converge a la solución única del sistema"


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

  return xo[-1]


# Gauss-Seidel sumatorias
def gauss_seidel_sumatorias(A, b, tol=1e-5, max_iter=100):
  xo = np.zeros(len(b))
  n = len(b)
  x1 = np.zeros(n)
  norm = 2  # Inicialmente mayor que la tolerancia
  cont = 0

  while norm > tol and cont < max_iter:
    for i in range(n):
      aux = 0
      for j in range(n):
        if i != j:
          aux -= A[i, j] * xo[j]
      x1[i] = (b[i] + aux) / A[i, i]

    norm = np.max(np.abs(x1 - xo))
    xo = x1.copy()
    cont += 1

  return x1

# Eliminación Gaussiana


def eliminacion_gaussiana(A, b):
  n = len(b)
  x = np.zeros(n)

  for k in range(0, n-1):
    for i in range(k+1, n):
      lambd = A[i, k]/(A[k, k])
      A[i, k:n] =  A[i, k:n] - lambd*A[k, k:n]
      b[i] = b[i] - lambd*b[k]
      print(lambd)

  for k in range(n-1, -1, -1):
    x[k] = (b[k]-np.dot(A[k, k+1:n], x[k+1:n]))/A[k,k]

  return x


def pivot(A, b):
  A = A.astype(float)
  b = b.astype(float)
  n = len(b)

  for k in range(n - 1):
    # Pivoteo parcial
    max_index = np.argmax(abs(A[k:n, k])) + k
    if A[max_index, k] == 0:
      return "El método no converge a la solución del sistema."

    if max_index != k:
      A[[k, max_index]] = A[[max_index, k]]
      b[[k, max_index]] = b[[max_index, k]]

    for i in range(k + 1, n):
      lam = A[i, k] / A[k, k]
      A[i, k:n] -= lam * A[k, k:n]
      b[i] -= lam * b[k]

  x = np.zeros(n)
  for k in range(n - 1, -1, -1):
    x[k] = (b[k] - np.dot(A[k, k + 1:n], x[k + 1:n])) / A[k, k]

  return x