def newton_solver(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    steps = 0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero!")
        x_new = x - fx / dfx
        steps += 1
        if abs(x_new - x) < tol:
            return x_new, steps
        x = x_new
    raise ValueError("Did not converge")