def bisection_solver(f, a, b, tol=1e-6, max_iter=100):
    steps = 0
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    while (b - a) / 2 > tol and steps < max_iter:
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, steps
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        steps += 1

    return (a + b) / 2, steps