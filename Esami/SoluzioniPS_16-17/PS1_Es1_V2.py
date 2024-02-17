def trova_elemento_mancante(A):
  """
  Trova l'elemento mancante in un array ordinato di interi distinti.

  Parametri:
    A: Un array ordinato di n interi distinti compresi fra 1 e n + 1.

  Restituisce:
    L'elemento mancante in A.
  """

  n = len(A)
  low = 0
  high = n - 1

  # L'elemento mancante è sicuramente fuori dall'array se n è 0 o 1
  if n <= 1:
    return n + 1
  mancante = 0
  # Ciclo di ricerca binaria
  while low <= high:
    mid = (low + high) // 2

    # Controlla se l'elemento mancante si trova nella metà sinistra
    if A[mid] != mid + 1:
      high = mid - 1
    else:
      # L'elemento mancante si trova nella metà destra
      mancante = a[mid]+1
      low = mid + 1

  # L'elemento mancante è low, che ora punta all'indice fuori dall'array
  return mancante

a = [1, 2, 3, 5, 6, 7]

print(f"Elemento mancante : {trova_elemento_mancante(a)}")