from newton import newton_solver
from bisection import bisection_solver
from functions import f, df

def compare_methods(f, df, x0, a, b, tol=1e-6):
    print("⚖️ Comparing Newton-Raphson and Bisection...\n")
    root_n, steps_n = newton_solver(f, df, x0, tol)
    print(f"Newton-Raphson → Root: {root_n:.6f} | Steps: {steps_n}")

    root_b, steps_b = bisection_solver(f, a, b, tol)
    print(f"Bisection       → Root: {root_b:.6f} | Steps: {steps_b}")

    faster = "Newton-Raphson" if steps_n < steps_b else "Bisection"
    print(f"\n✅ {faster} method converged faster.\n")

# Example usage
compare_methods(f, df, x0=10, a=1, b=30)