def func_square(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results


numbers = [1, 2, 3, 4]
a = func_square(*numbers)
print(a)
