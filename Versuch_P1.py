# Title: "Stability Analysis of Dynamic Systems using Numerical Integration Methods"


# Explanation: This project aims to demonstrate the effectiveness of different numerical integration methods 
# in solving dynamic differential equations.


# By comparing the results obtained from the Implicit Euler and 
# Runge-Kutta 4 methods with those from the Explicit Euler method, the project highlights how stability 
# and accuracy can vary. 


# Ultimately, the goal is to showcase how the Implicit Euler and Runge-Kutta 4 
# methods offer superior performance, with the latter achieving a remarkable 90% similarity to the 
# exact solution of the system's function.


import matplotlib.pyplot as plt
import numpy as np

a = 0  # Define the value for 'a' used in the functions
# Wert für a definieren, da er in den Funktionen verwendet wird

def f(t, y):
    """
    Defines the system of differential equations.
    Args:
        t (float): Time parameter.
        y (numpy array): State vector.
    """

    yo = y.shape[0]
    result = np.zeros(yo,)
    result[0] = y[1]
    result[1] = -((a**2) + 1) * y[0] - 2 * a * y[1]  
    return result

def euler(t, y, h):
    """
    Implements the Euler method for solving ordinary differential equations.
    Args:
        t (float): Time parameter.
        y (numpy array): State vector.
        h (float): Step size.
    """
    plt.title('Euler-Verfahren')
    return y + h * f(t, y)
    
    
    

def euler_implicit(t, y, h):
    """
    Implements the Implicit Euler method for solving ordinary differential equations.
    """

    plt.title('Implizit-Euler-Verfahren')
    A = np.array([[1, -h], [((a**2) + 1) * h, 1 + 2 * a * h]])  
    return np.linalg.solve(A, y)


def rk4(t, y, h):
    """
    Implements the Runge-Kutta 4 method for solving ordinary differential equations.
      """
    plt.title('Runge-Kutta 4 Verfahren')
    k1 = f(t, y)
    k2 = f(t + h/2, y +(h*k1)/2)
    k3 = f(t + h/2, y +(h* k2)/2)
    k4 = f(t +h , y + (h* k3))
    return (y + (h/6)*(k1 + 2*k2 + 2*k3 + k4))
      
        
        
def double_step(t, y, h, Integrator):
    """
    Performs two steps with half the step size using the specified integrator.
    Args:
        
        Integrator (function): Integrator function (e.g., euler, euler_implicit, rk4).
    Returns:
        numpy array: New state vector after two steps with half the step size.
    """
    plt.title('Double Step')
    y_new = Integrator(t, y, h/2)
    y_new = Integrator(t + h/2, y_new, h/2)
    return y_new


def error_order(t0, y0, h_min, h_max, Integrator, legends):
    """
    Calculates the error order against different step sizes and plots the result.
     """
    h = np.linspace(h_min, h_max, 100)
    error = np.zeros(100)
    error_i = np.zeros(len(y0))
    
    for i in range(100):
        y_double = double_step(t0, y0, h[i], Integrator)
        y_single = Integrator(t0, y0, h[i])
        error_i = y_double - y_single
        error[i] = np.linalg.norm(error_i)
    
    plt.plot(np.log10(h), np.log10(error))
    legends.append('double error')
    plt.legend(legends)
    plt.show()
     

def solve(t0, tn, y0, h, Integrator):
    """
    Solves the differential equation over a given time interval using the specified integrator and plots the result.
    Args:
        t0 (float): Initial time.
        tn (float): Final time.
        y0 (numpy array): Initial state vector.
        h (float): Step size.
        Integrator (function): Integrator function (e.g., euler, euler_implicit, rk4).
    """
    num_steps = int((tn - t0) / h)
    t = np.linspace(t0, tn, num_steps)
    y = np.zeros((len(y0), num_steps))
    y[:, 0] = y0
    
    for i in range(num_steps - 1):
        y[:, i+1] = Integrator(t[i], y[:, i], h)
    
    plt.plot(t, y[0])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid(True)
    return t, y
     

def aufgabe1():
    """
    Executes task 1: solving the differential equation and plotting the result.
    """

    legends = ['0.001', '0.01', '0.02', '0.05', 'y_exakt']
    h_values = [0.001, 0.01, 0.02, 0.05]
    for h in h_values:
        t, y = solve(0, 20*np.pi, np.array([0, 1]), h, rk4) # change the parameters here to display different funtions (i.e: euler or rk4)
        y_exakt = np.exp(-a*t) * np.sin(t)
        plt.plot(t, y_exakt)
    plt.legend(legends)
    plt.show()

def aufgabe2():
    """
    Executes task 2: calculating error order against different step sizes and plotting the result.
    """

    legends = []
    error_order(0, np.array([0, 1]), 0.01, 0.1, rk4, legends) # change the parameters here to display different funtions (i.e: euler or rk4)
    plt.show()

aufgabe1()
aufgabe2()
