import numpy as np 

def adagrad(gradient_func, beta_init, learning_rate = 0.1, epsilon = 1e-8, max_iter = 100):
    beta = beta_init
    g_accum = np.zeros_like(beta)
    history = [beta.copy()] 
    for i in range(max_iter):
        grad = gradient_func(beta)
        g_accum += grad**2
        beta = beta - learning_rate * grad / np.sqrt(g_accum + epsilon)
        history.append(beta.copy())
        print("Iteration: ", i, beta - learning_rate * grad / np.sqrt(g_accum + epsilon))


    return beta, history


def objective_grad(beta):
    return 2 * (beta -3)

beta_ii = np.array([0.0])

optimized_beta , beta_history = adagrad(objective_grad, beta_ii, learning_rate = 0.1, max_iter = 100)

print("Optimized beta: ", optimized_beta)