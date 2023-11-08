def search_for_sum(a,h):
    trovato = bin_search_sum(a,h)
    return trovato
def bin_search_sum(a,h):
    start = 0
    n=len(a)
    end = n - 1
    
    while (start <= end):
        mid = (start + end) // 2
        sum = 0
        for i in range(mid):
            sum += a[i]
        
        if (sum == h):
            return True
        elif (sum < h):
            start = mid + 1
        else:
            end = mid - 1
    return False
a = [1,1,1,2,2,2,2]
print(search_for_sum(a,5))