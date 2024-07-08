# MathSEE Modeling-Week

## Introduction 
As a start, you can follow the exercises below and at any point start working on your own projects. 
The exercises include mathematically modeled problems like the Heat Conduction Model and the 3 Body Problem. For the Uncertainty Quantification methods, you can find examples for calssic Monte Carlo (MC), Quasi Monte Carlo (QMC), and Markov Chain Monte Carlo (MCMC). 
When moving forward with the exercises we will introduce UM-Bridge. You can check out the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) and follow the Quickstart Guide and/or the Tutorial to get familiar with UM-Bridge.
The example solutions are all written in Python so we strongly suggest using Python as well, if you prefer another language make sure it is supported by UM-Bridge.  

## 1 The first exercise
### 1.1 Monte Carlo
For the first exercise have a look at the classic [Monte Carlo method](UQ/MC.ipynb)
We start simple by implementing the classic Monte Carlo (MC) method that samples from the following distribution:

$X\sim \mathcal{N}(0.5, 0.01)$.

Change the sample size, and see what effect it has on the estimated solution. 

To compare your results, [here](UQ/MC_1.1.ipynb) you can find a description of the method as well as an example of the implementation. 

### 1.2 Integrate UM-Bridge
At this point now you can start writing your first simple UM-Bridge model. Use the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) to get to know UM-Bridge and then implement a UM-Bridge server that solves the following function:

$f(x) = sin(2\pi x)$

If you are implementing your UM-Bridge server in a jupyter notebook it is necessary to add the following two lines at the very top of the cell:

```
import nest_asyncio
nest_asyncio.apply()
```

Compare your implementation to the [example solution](UQ/MC_1.2.ipynb), to make sure your setup is correct.

### 1.3 Monte Carlo as a UM-Bridge client
We are now interested in solving the following integral:

$\int^{1}_{0}f(x)dx$.

To solve this integral implement the Monte Carlo method as an UM-Bridge client. [Here](UQ/MC_1.3.ipynb) you can find an example client.

### 1.4 Solve an integral using UM-Bridge
The last step of this first exercise is to combine the UM-Bridge server and the UM-Bridge client to solve the integral. 

First, run the server. Then connect the client to the server. Look at the result and vary the sample size until you get a satisfactory result. 

Note: If you are running your server and client in a notebook you must put them in two different files to prevent the server from blocking the client's execution.





