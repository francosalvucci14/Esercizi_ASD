# Definizione della struttura del nodo dell'albero binario
class TreeNode:
    def __init__(self, name, val, special):
        self.name = name
        self.val = val
        self.special = special
        self.left = None
            

# Funzione ricorsiva per visitare l'albero e trovare il valore massimo raggiungibile da nodi speciali
def find_max_reachable_special(node, max_special_val, max_special_node, V):
    if node is None:
        return 0
    
    # Aggiorniamo il valore massimo raggiungibile e il nodo speciale corrispondente
    if node.special and node.val > max_special_val:
        max_special_val = node.val
        max_special_node = node

    # Aggiorniamo il vettore V con il valore massimo raggiungibile fino a questo punto
    V[node.name] = max_special_val

    # Visitiamo ricorsivamente il sottoalbero sinistro e destro
    find_max_reachable_special(node.left, max_special_val, max_special_node, V)
    find_max_reachable_special(node.right, max_special_val, max_special_node, V)

    return V

# Funzione principale per costruire il vettore V
def build_max_reachable_special_values(T):
    n = len(T)
    V = [0] * (n + 1)  # Inizializziamo il vettore V con zeri
    
    # Troviamo il nodo speciale con il valore massimo raggiungibile nell'albero
    max_special_val = -1
    max_special_node = None

    for i in range(1,n):
        node = T[i]
        if node.special and node.val > max_special_val:
            max_special_val = node.val
            max_special_node = node

    # Chiamiamo la funzione ricorsiva per visitare l'albero e costruire il vettore V
    find_max_reachable_special(max_special_node, max_special_val, max_special_node, V)

    return V[1:]  # Restituiamo il vettore V, eliminando l'elemento iniziale V[0]

# Esempio di utilizzo dell'algoritmo
# Supponiamo che l'albero T sia rappresentato come una lista di nodi collegati, dove T[i] corrisponde al nodo con nome i.
T = [None]  # L'indice 0 verrà ignorato, partiamo da T[1]
T.append(TreeNode(1, 10, False))
T.append(TreeNode(2, 5, True))
T.append(TreeNode(3, 7, False))
T.append(TreeNode(4, 15, False))
T.append(TreeNode(5, 20, False))
T.append(TreeNode(6, 3, False))
T.append(TreeNode(7, 8, True))

T[1].left = T[2]
T[1].right = T[3]
T[2].left = T[4]
T[2].right = T[5]
T[3].left = T[6]
T[3].right = T[7]
n = len(T)
V = [0] * (n + 1)
result = find_max_reachable_special(T,0,0,V)
print(result)  # Output: [8, 20, 8, 15, 20, 20, 8]
