value = [-1, 1, 1] + [-1] * 998

def f(n):
    if value[n] != -1: return value[n]
    value[n] = f(n - 1) + f(n - 2)
    return value[n]