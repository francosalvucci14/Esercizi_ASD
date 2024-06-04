"""
Si vuole illuminare una pista ciclabile di n tratte. In ogni tratta `e possibile, volendo, installare un
lampione. Se installato sulla tratta i, un lampione `e in grado di illuminare la tratta i e le due tratte
immediatamente precedenti e immediatamente successive i (ovvero le tratte i − 2 e i − 1, se esistono,
e le tratte i+1 e i+2, se esistono). Il costo di installazione, per`o, non `e uniforme. Pi`u precisamente,
installare un lampione nella tratta i costa ci. Progettare un algoritmo di programmazione dinamica
che trova il costo minimo con cui `e possibile illuminare l’intera pista ciclabile, ovvero il costo di una
soluzione migliore possibile in cui ogni tratta `e illuminata da almeno un lampione.
"""

def min_cost_lampione(costs):
    n = len(costs)
    dp = [0] * n
    dp[0] = costs[0]
    dp[1] = costs[1]
    
    for i in range(2, n):
        dp[i] = min(dp[i-2], dp[i-1]) + costs[i]
    
    # Find the positions of the lamp posts
    lamp_post_positions = []
    i = n - 1
    while i >= 0:
        if i == 0:
            lamp_post_positions.append(i)
            break
        elif i == 1:
            lamp_post_positions.append(i)
            break
        elif dp[i] == dp[i-2] + costs[i]:
            lamp_post_positions.append(i)
            i -= 2
        else:
            lamp_post_positions.append(i-1)
            i -= 3

    # Reverse the list to get the correct order
    lamp_post_positions.reverse()

    # Print the positions of the lamp posts
    print("Lamp post positions:")
    for position in lamp_post_positions:
        print(position)
    
    return min(dp[n-1],dp[n-2])

def min_cost_to_illuminate(n, costs):
    # Extend dp array to handle base cases for i < 5
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # No cost to illuminate zero segments
    
    for i in range(1, n + 1):
        # Lampione sulla tratta i-1
        if i >= 1:
            dp[i] = min(dp[i], dp[i-3] + costs[i-1])
        # Lampione sulla tratta i-2
        if i >= 2:
            dp[i] = min(dp[i], dp[i-4] + costs[i-2])
        # Lampione sulla tratta i-3
        if i >= 3:
            dp[i] = min(dp[i], dp[i-5] + costs[i-3])
        # Se i < 4, possiamo accedere a dp[i] usando i valori di dp iniziali
            
    return dp[n]


costs = [2, 5, 3, 1, 6, 8, 4, 2]
n=len(costs)
min_cost = min_cost_lampione(costs)
print(f"The minimum cost to illuminate the entire bike path is: {min_cost}")

print(min_cost_to_illuminate(n, costs))