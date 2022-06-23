import numpy as np
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
def sub(x, y):
    return x - y
def add(x, y):
    return x + y
def neg(x):
    return -x
def pow(x, y):
    return x ** y
def sqrt(x):
    return np.sqrt(x)
def log(x):
    return np.log(x)
def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)
def tan(x):
    return np.tan(x)
def max(x, y):
    return np.where(np.abs(x) > np.abs(y), x, y)
def min(x, y):
    return np.where(np.abs(x) < np.abs(y), x, y)
# 待补充