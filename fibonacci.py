def fibonacci(n):
    """This is documentation string for function. It'll be available by fibonacci.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []

    a = 1

    b = 1

    while a < n:
        result.append(a)

        tmp_var = b

        b = b + a

        a = tmp_var

    return result

print(fibonacci(9000))
