
# Steffensen’s Method accelerates the convergence of fixed-point iteration using Aitken’s Δ² process. It does not require derivatives and is useful when you want rapid convergence for functions where simple fixed-point iteration would be slow
def steffensen(f, x0, max_iterations=100, epsilon=1e-10):
    x = x0

    for k in range(max_iterations):
        x1 = f(x)              # First approximation: f(x)
        x2 = f(x1)             # Second approximation: f(f(x))

        denominator = x2 - 2 * x1 + x
        if denominator == 0:   # Avoid division by zero
            break

        # Aitken acceleration formula:
        x_new = x - ((x1 - x)**2) / denominator

        if abs(x_new - x) < epsilon:  # Convergence test
            break

        x = x_new

    return x
	


# Newton-Raphson method implementation
# This is the Newton-Raphson Method for finding a root of a function. It uses the derivative (here, numerically approximated) and iteratively refines the guess. The function is general, but the example uses it to solve for mass in a velocity problem.
def derivative(m, h=1e-6):
    return (velocity_difference(m + h) - velocity_difference(m - h)) / (2 * h)


def newton_method(x0, max_iter=100, tol=1e-10):
    """
    Newton's method to find root of velocity_difference function
    
    Parameters:
    x0: initial guess for mass
    max_iter: maximum number of iterations
    tol: tolerance for convergence
    
    Returns:
    x: approximated root
    history: list of iterations for visualization
    """
    x = x0
    history = [(x, velocity_difference(x))]
    
    for i in range(max_iter):
        # Compute derivative
        f_prime = derivative(x)
        
        # Avoid division by zero
        if abs(f_prime) < 1e-10:
            break
            
        # Newton step
        x_new = x - velocity_difference(x) / f_prime
        
        # Ensure mass stays positive
        if x_new <= 0:
            x_new = x / 2  # Fallback strategy
            
        # Add to history
        history.append((x_new, velocity_difference(x_new)))
        
        # Check for convergence
        if abs(x_new - x) < tol:
            x = x_new
            break
            
        x = x_new
        
    return x, history


# This is the Bisection Method (Felező módszer) for finding a root in a given interval [a, b] where the function changes sign. It returns the approximate root and the history of intervals for analysis or plotting.

def felezo(a, b, MaxIter, Eps):
    """
    Bisection method with data collection for plotting
    """
    i = 0
    history = []  # To store iterations for plotting
    
    # Initial interval
    history.append((a, b, (a+b)/2))
    
    while(i < MaxIter):
        m = (a+b)/2
        
        if(f(m) == 0) or ((0.5 * abs(b-a)) < Eps):
            return m, history
        
        if f(m)*f(a) > 0:
            a = m
        else:
            b = m
            
        history.append((a, b, m))
        i += 1
    
    return m, history  # Return the last midpoint and history





# This is the implementation of the Secant Method (Húrmódszer) for finding the root of a function. It takes two initial values (a, b), a function f, a maximum number of iterations, and a tolerance. It iteratively updates the guess for the root using the secant formula until the solution converges or the maximum number of iterations is reached.

def HurModszer(a, b, f, k_max, tol=1e-10):
    x = b
    s = a
    
    for k in range(1, k_max):
        if (f(x) == f(s)):
            print("Division by zero")
            break
        
        x_new = x - (x - s / (f(x) - f(s)))*f(x)
        
        if(f(x_new) == 0):
            break
        
        if abs(f(x_new)) < tol:
            return x_new  # root found

        if f(x_new) * f(x) < 0:
            s = x

        x = x_new

    return x
