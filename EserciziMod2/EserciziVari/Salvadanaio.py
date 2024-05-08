"""
Per comprarvi l’ultimo gadget tecnologico, avete risparmiato inserendo monete
in un salvadanaio. Purtroppo non avete tenuto i conti, e non sapete quanti soldi ci sono
dentro. È facile ottenere il valore totale rompendo il salvadanaio, ma sarebbe un peccato
romperlo senza essere sicuri che ci siano abbastanza soldi per il vostro gadget. Fortunata-
mente, avete a disposizione le seguenti informazioni: il peso totale T delle monete contenute
nel salvadanaio, il vettore dei pesi p[1...n] e quello dei valori v[1...n], dove p[i ] è il peso in 
grammi e v[i ] è il valore in centesimi dell’i-esimo tipo di moneta fra gli n tipi di monete
prodotti nel vostro stato. Scrivere in pseudocodice un algoritmo che restituisca il minimo
valore in centesimi che può essere contenuto nel salvadanaio, e valutarne la complessità. Per
esempio, supponete che il peso totale sia 50 grammi, e le monete a disposizione siano quella
da 200 centesimi (2€), che pesa 50 grammi, e quella da 50 centesimi, che pesa 10 grammi. È pos-
sibile ottenere i 50 grammi del peso totale con una singola moneta da 200 centesimi, o con
5 da 50 centesimi per un totale di 250 centesimi. Quindi il valore da restituire è 200, che è il
minimo fra i due totali
"""


def SalvadanaioMemoization(
    pesi: list, valori: list, t: int, i: int, cache: dict = dict()
) -> int:
    
    if t < 0:
        return float("inf")
    if i == 0 and t > 0:
        return float("inf")
    if t == 0:
        return 0
    cache[i, t] = min(
        SalvadanaioMemoization(pesi, valori, t - pesi[i-1], i, cache) + valori[i-1],
        SalvadanaioMemoization(pesi, valori, t, i - 1, cache),
    )
    return cache[i, t]


pesi = [50, 10]
valori = [200, 50]
T = 50
cache = dict()
num_monete = len(valori)

print(SalvadanaioMemoization(pesi, valori, T, num_monete, cache))
