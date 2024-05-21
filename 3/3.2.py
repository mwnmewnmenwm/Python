# с рекурсией
def a_recursive(k):
    if k == 1:
        return 1
    return 2 * b_recursive(k-1) + a_recursive(k-1)

def b_recursive(k):
    if k == 1:
        return 1
    return 2 * a_recursive(k-1) + b_recursive(k-1)

k = 5
a_k = a_recursive(k)
b_k = b_recursive(k)
print("с рекурсией:")
print(f"a_{k} = {a_k}")
print(f"b_{k} = {b_k}")



# без рекурсии
def iterative(k):
    a = [0] * (k + 1)
    b = [0] * (k + 1)
    a[1] = 1
    b[1] = 1
    
    for i in range(2, k + 1):
        a[i] = 2 * b[i-1] + a[i-1]
        b[i] = 2 * a[i-1] + b[i-1]
    return a[k], b[k]

k = 5
a_k, b_k = iterative(k)
print("без рекурсии:")
print(f"a_{k} = {a_k}")
print(f"b_{k} = {b_k}")