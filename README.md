# MathSEE Modeling-Week

## Introduction 
In fields such as physics, economics, and statistics, complex models are constructed to replicate real-world phenomena. During this process, various types of uncertainties inevitably arise. A model is always an abstraction of reality and cannot incorporate every detail. This abstraction is crucial for focusing on significant aspects while ignoring less important details, making the complexity of reality more manageable and computable. However, this simplification introduces uncertainties.

Uncertainties can stem from naturally variable phenomena or from a lack of knowledge and the inability to account for all aspects of the real world. In response, Uncertainty Quantification (UQ) aims to address these uncertainties and evaluate their impact on a model’s output. To comprehensively understand the implications of these uncertainties, models must be computed multiple times with varying input values.

When examining a model we must first know what kind of UQ problem we are looking at. Our main focus in the following lies on forward and inverse problems.

In a forward problem, the analysis focuses on understanding how variations in input parameter values affect a model’s output. Often, uncertainties surround the exact values of a model’s input parameters, and only a range or a distribution of their values is known. By evaluating the model across these input values, not only can single output values be determined, but also knowledge about the distribution and the characteristics of these values throughout the output space is gained.

Conversely, in inverse problems, the input parameter values are unknown, but an observed outcome is available. The task here is to identify the input values that best explain the observed outcome. When used as input values for a model, those values should lead to an output close to the known observation.

The following exercises will lead you through differnt mathematical models and methods to solve them. You can follow the exercises below and at any point start working on your own projects. 
The exercises include mathematically modeled problems like the Heat Conduction Model and the 3 Body Problem. For the Uncertainty Quantification methods, you can find examples for classic Monte Carlo (MC), Quasi Monte Carlo (QMC), and Markov Chain Monte Carlo (MCMC). 
When moving forward with the exercises we will introduce UM-Bridge. You can check out the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) and follow the Quickstart Guide and/or the Tutorial to get familiar with UM-Bridge.
The example solutions are all written in Python so we strongly suggest using Python as well, if you prefer another language make sure it is supported by UM-Bridge [here](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html).


## 1 The first exercise
In the first exercise we are looking at the Predator-Prey model and solve it with the Monte Carlo method.

### 1.1 Predator-Prey Model
Get familiar with the [Predator-Prey Model](UQ/predprey.ipynb).

### 1.2 Integrate UM-Bridge
At this point we are writing the model as a UM-Bridge server. Use the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) to get to know UM-Bridge and then look at the implementation [here](UQ/predprey.model.ipynb).

The purpose of UM-Bridge: UM-Bridge serves as an interface that enables communication between advanced computational models written in various programming languages. UM-Bridge views these models as functions mapping input vectors onto output vectors. The models are designed as servers that can connect to clients through HTTP. Server and client only exchange input and output data without any further information about each other’s implementation specifics. This way concearns stay seperated.

### 1.3 Solving the Predator-Prey Model
To solve the 



## 1 The first exercise
The first exercises focuses on solving forward UQ problems. We are starting off by looking at the Monte Carlo method. 
### 1.1 Monte Carlo
Open the first notebook to get familiar with the [Monte Carlo](UQ/MC_1.1.ipynb) (MC) method. 
In the example we sample from the following distribution:

$X\sim \mathcal{N}(0.5, 0.01)$.

### 1.2 Integrate UM-Bridge
At this point now you can start writing your first simple UM-Bridge model. Use the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) to get to know UM-Bridge and then implement a UM-Bridge server that solves the following function:

$f(x) = sin(2\pi x)$

If you are implementing your UM-Bridge server in a jupyter notebook it is necessary to add the following two lines at the very top of the cell:

```
import nest_asyncio
nest_asyncio.apply()
```

Compare your implementation to the [example solution](UQ/MC_1.2.ipynb), to make sure your setup is correct.

### 1.3 Monte Carlo as an UM-Bridge client
We are now interested in solving the following integral:

$\int^{1}_{0}f(x)dx$.

To solve this integral implement the Monte Carlo method as an UM-Bridge client. [Here](UQ/MC_1.3.ipynb) you can find an example client.

### 1.4 Solve an integral using UM-Bridge
The last step of this first exercise is to combine the UM-Bridge server and the UM-Bridge client to solve the integral. 

First, run the server. Then connect the client to the server. Look at the result and vary the sample size until you get a satisfactory result. 

Note: If you are running your server and client in a notebook you must put them in two different files to prevent the server from blocking the client's execution.

## Exercise two
In the second exercise we explore variations of the Monte Carlo method.
### 2.1 Quasi Monte Carlo
Get familiar with the [quasi Monte Carlo](UQ/QMC.ipynb) (QMC) method and implement the method as an UM-Bridge client.

### 2.2 Markov Chain Monte Carlo
To solve inverse UQ problems take a look at the [Markov Chain Monte Carlo](UQ/MCMC.ipynb) (MCMC) method. 

### 2.3 The benefit of UM-Bridge
You might ask yourselves why we are implementing all these UQ methods as UM-Bridge clients instead of directly incorporating them into our models. What initially seems like an extra step actually provides a significant advantage: it allows you to implement your UQ code once and then apply it to any UM-Bridge model of your choice. This eliminates the need to repeatedly implement the same UQ method for different models.

In the following sections, you will explore various models to which you can apply your UQ clients. If you have your own models, try implementing them as UM-Bridge servers and solving them with your newly created UM-Bridge clients.

Note: Make sure that the input and output dimensions of your UM-Bridge clients and servers are compatible.

## Exercise three
In this third exercise we are looking at three more advanced models. All of them concern a forward UQ problem.
### 3.1 Predator-Prey Dynamical System
Open the notebook about the [Predator-Prey Dynamical System](UQ/predprey.ipynb). Here you will learn about the model and how to set up your MC client for this specific problem.

### 3.2 Three Body Problem
In [this](CR3BP.ipynb) notebook you can find the discription and implementation of the three body Problem.

### 3.3 Steady State Heat Conduction Problems
This is an exercise that concerns UQ for Bayesian Inverse Problem governed by a PDE. The PDE that you will consider is the [Steady State Heat Equation](Heat_Conduction/heatconduction_UQ.ipynb). Also, in this notebook [MCMC for Heat Equation](Heat_Conduction/heatconduction_MCMC.ipynb)you will gain an understanding of how to create the MCMC algorithm for this problem. 






