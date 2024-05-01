


# Stability Analysis of a Dynamic System

## Overview

A lab experiment; Stability Analysis of a mathematical Dynamic System using Numerical Integration Methods (i.e. Euler and Runge-Kutta-4 methods).

This project aims to demonstrate the effectiveness of different numerical integration methods in solving dynamic differential equations. By comparing the results obtained from the Implicit Euler and Runge-Kutta 4 methods with those from the Explicit Euler method, the project highlights how stability and accuracy can vary. Ultimately, the goal is to showcase how the Implicit Euler and Runge-Kutta 4 methods offer superior performance, with the latter achieving a remarkable 90% similarity to the exact solution of the system's function.

## Project Description

The project contains Python scripts implementing the Implicit Euler, Runge-Kutta 4, and Explicit Euler methods for solving ordinary differential equations. It includes functions to define the system of differential equations, implement the numerical integration methods, perform error analysis, and plot the results.

## Collaborators

- **Fares Al-Huri** - Student, Hannover University of Applied Sciences and Arts

- **Galal Al-habbari** - Student, Hannover University of Applied Sciences and Arts

- **M.Eng. Mohammed Beyki** - Supervisor, Hannover University of Applied Sciences and Arts

## Dependencies

- Python version 3.12.2
- NumPy and Matplotlib libraries

## How to Execute

To execute the project:

1. Clone the repository to your local machine.
2. Install the necessary dependencies (Python 3, NumPy, Matplotlib).
3. Open the Python script in a text editor or an integrated development environment (IDE).

### Showing Different Graphs

#### Implicit Euler Method
To show the graph for the Implicit Euler method:
- In the Python script, locate the function `aufgabe1()`.
- Within this function, there is a loop over `h_values`, which represents different step sizes.
- Uncomment the line `t, y = solve(0, 20*np.pi, np.array([0, 1]), h, euler_implicit)` to use the Implicit Euler method.
- Run the Python script. It will display a graph showing the solution obtained using the Implicit Euler method.

  
  ![image](https://github.com/ImCavaliere/Stability-of-a-Dynamic-System/assets/92309733/a817baa3-fed9-4e12-8ff9-7ddd152bba90)


#### Runge-Kutta 4 Method
To show the graph for the Runge-Kutta 4 method:
- In the Python script, locate the function `aufgabe1()`.
- Within this function, there is a loop over `h_values`, which represents different step sizes.
- Uncomment the line `t, y = solve(0, 20*np.pi, np.array([0, 1]), h, rk4)` to use the Runge-Kutta 4 method.
- It will display a graph (Figure bleow) showing the more precise solution obtiained:
- ![image](https://github.com/ImCavaliere/Stability-of-a-Dynamic-System/assets/92309733/1b4d57d1-476b-40f9-8c01-b663b869c249)


  The following figure shows the error order when setting the minimal and maximal step sizes on the `rk4` method as 0.01 and 0.1 respectively:

  
  ![image](https://github.com/ImCavaliere/Stability-of-a-Dynamic-System/assets/92309733/257948c0-df90-47a8-aadd-ca74bb3dd385)

  
 

### Analyzing Different Scenarios

To analyze different scenarios, you can modify the parameters passed to the `solve()` function within the `aufgabe1()` function. Specifically, you can adjust the initial time, final time, initial state vector, and step size. Similarly, you can modify the parameters passed to the `error_order()` function within the `aufgabe2()` function to change the range of step sizes for error analysis.

By adjusting these parameters, you can explore various scenarios and analyze the behavior of the system under different conditions.


You can execute each task by calling the corresponding function in the Python script.

## How to Contribute

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your contribution.
3. Make your changes and commit them to your branch.
4. Push your branch to your forked repository.
5. Open a pull request to submit your changes for review.

## Acknowledgments

- MathWorks
- Hannover University of Applied Sciences

