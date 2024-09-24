# MathSEE Modeling-Week

This work is licensed under [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Introduction 
In fields such as physics, economics, and statistics, complex models are constructed to replicate real-world phenomena. They are essential tools in these fields because they allow us to explore, understand and predict complex phenomena in ways that would be impossible, impractical, or too costly to do through direct experimentation alone. During this process, various types of uncertainties inevitably arise. A model is always an abstraction of reality and cannot incorporate every detail. This abstraction is crucial for focusing on significant aspects while ignoring less important details, making the complexity of reality more manageable and computable. However, this simplification introduces uncertainties.

Uncertainties can stem from naturally variable phenomena or from a lack of knowledge and the inability to account for all aspects of the real world. In response, Uncertainty Quantification (UQ) aims to address these uncertainties and evaluate their impact on a model’s output. To comprehensively understand the implications of these uncertainties, models must be computed multiple times with varying input values.

When examining a model we must first know what kind of UQ problem we are looking at. Our main focus in the following lies on forward and inverse problems.

In a forward problem, the analysis focuses on understanding how variations in input parameter values affect a model’s output. Often, uncertainties surround the exact values of a model’s input parameters, and only a range or a distribution of their values is known. By evaluating the model across these input values, not only can single output values be determined, but also knowledge about the distribution and the characteristics of these values throughout the output space is gained.

Conversely, in inverse problems, the input parameter values are unknown, but an observed outcome is available. The task here is to identify the input values that best explain the observed outcome. When used as input values for a model, those values should lead to an output close to the known observation.

The following exercises will lead you through different mathematical models and methods to solve them. You can follow the exercises below and at any point start working on your own projects. 
The exercises include mathematically modeled problems like the Heat Conduction Model and the 3 Body Problem. For the Uncertainty Quantification methods, you can find examples for classic Monte Carlo (MC), Quasi Monte Carlo (QMC), and Markov Chain Monte Carlo (MCMC). In exercise six you will learn how to run your models on a High Performance Computer.


When moving forward with the exercises we will introduce UM-Bridge. You can check out the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) and follow the Quickstart Guide and/or the Tutorial to get familiar with UM-Bridge.
The example solutions are all written in Python so we strongly suggest using Python as well, if you prefer another language make sure it is supported by UM-Bridge [here](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html).


## 1 Basic Modeling
In this first exercise, we'll familiarize ourselves with ordinary differential equations (ODEs) and how they can be used to model real-world interactions between two species. Specifically, we'll explore the Lotka-Volterra equations, which describe the dynamics between predators and prey. We use this as a reference because it is a real-world example that, while not too complex, effectively demonstrates the interactions between different species.

### 1.1 Predator-Prey Model
Refer to the first notebook: [Predator-Prey Dynamical System](UQ/predprey.ipynb). This contains a description of the model, along with exercises to help you study and understand the system.

In the third exercise, we will examine the Predator-Prey Model as a UQ problem.

## 2 UM-Bridge
In this section, we will get to know the UM-Bridge interface.

**The purpose of UM-Bridge:** UM-Bridge serves as an interface that enables communication between advanced computational models written in various programming languages. UM-Bridge views these models as functions mapping input vectors onto output vectors. The models are designed as servers that can connect to clients through HTTP. Server and client only exchange input and output data without any further information about each other’s implementation specifics. This way concerns stay seperated. (For further information read the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html)).

### 2.1 A Simple Model
To get familiar with UM-Bridge, let's start by implementing a simple server for the following function:

$f(x) = sin(2\pi x)$.

This model will serve as a basic example to demonstrate how UM-Bridge works. The function takes an input $x$ and returns the function value $sin(2 \pi x)$.

When implementing your UM-Bridge server in a Jupyter notebook, it is necessary to add the following two lines at the very top of the cell:

```
import nest_asyncio
nest_asyncio.apply()
```

This ensures compatibility with the notebook environment. Compare your implementation to the [example solution](UQ/MC_server.ipynb), to make sure your setup is correct.

### 2.2 Predator-Prey Model as UM-Bridge Server
Once you're comfortable with the simple example from 2.1, the next step is to implement the Predator-Prey model (introduced in 1.1) as an UM-Bridge server. The Predator-Prey model is more complex and will help you see how UM-Bridge can manage multi-dimensional models.

You can reference the sample implementation of the Predator-Prey Model server [here](UQ/predprey_server.ipynb) for guidance. For further details on UM-Bridge, revisit the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html).

The server is now running and ready to handle requests from a client. Since the model itself has been implemented, we can proceed to make model evaluations. A client request corresponds to a function evaluation of the Lotka-Volterra system. To see how you can interact with the server and evaluate the model, refer to the [first client](/UQ/predprey_firstclient.ipynb). This notebook demonstrates how to connect to the Predator-Prey Model server and perform function evaluations by specifying the model parameters.

## 3 Basic UQ Methods

To solve an Uncertainty Quantification (UQ) problem, a variety of methods can be used. In this section, we are starting simple by getting to know the Monte Carlo (MC) method.

### 3.1 Monte Carlo
Get familiar with the [Monte Carlo](UQ/MC.ipynb) (MC) method. In the example, we sample from the following distribution:

$X\sim \mathcal{N}(0.5, 0.01)$.

In the notebook, you can find a few tasks, such as varying the sample size or changing the distribution. This will help you to explore how different parameters influence the results and how the Monte Carlo method works in practice.

### 3.2 Monte Carlo as an UM-Bridge Client
Next, you will implement the MC method as an UM-Bridge client. [Here](UQ/MC_client.ipynb) you can find an example MC client template.

#### Solve an Integral using UM-Bridge
The final step of this exercise involves using the UM-Bridge framework to solve the following integral:

$\int_{0}^{1} f(x) \\textit{d}x$, where $f(x) = sin(2\pi x)$.

1. Run the [UM-Bridge server](UQ/MC_server.ipynb) as defined in section **2.1** to set up the model.
2. Connect the [MC client](UQ/MC_client.ipynb) to the server and evaluate the function $f(x)$ at random points $X_i \sim \mathcal{U}([0, 1])$.
3. Look at the result of the MC estimator and vary the sample size $N$ to see how it affects the accuracy of the estimate.

Note: If you are running your server and client in a notebook you must put them in two different files to prevent the server from blocking the client's execution.

## 4 UQ Application
In this exercise we are looking at the Predator-Prey Model as a UQ problem and solve it with the MC method

### 4.1 Predator-Prey Model as a UQ problem
Look at the following [notebook](UQ/predprey_UQ.ipynb) and get familiar with the problem.

### 4.2 MC Client for Predator-Prey Model
Take a look at the [MC client](UQ/predprey_client.ipynb) for the Predator-Prey Model.

### 4.3 Solve the Predator-Prey UQ problem with UM-Bridge
To solve the Predator-Prey UQ problem with UM-Bridge, run the Predator-Prey client from exercise **1.2** and connect your MC client from exercise **3.2**.


## 5 Advanced UQ Methods
In this exercise we explore variations of the Monte Carlo method.

### 5.1 Quasi Monte Carlo
Get familiar with the [quasi Monte Carlo](UQ/QMC.ipynb) (QMC) method and implement the method as an UM-Bridge client.

### 5.2 Markov Chain Monte Carlo
To solve inverse UQ problems take a look at the [Markov Chain Monte Carlo](UQ/MCMC.ipynb) (MCMC) method. 

### 5.3 The Benefit of UM-Bridge
You might ask yourselves why we are implementing all these UQ methods as UM-Bridge clients instead of directly incorporating them into our models. What initially seems like an extra step actually provides a significant advantage: it allows you to implement your UQ code once and then apply it to any UM-Bridge model of your choice. This eliminates the need to repeatedly implement the same UQ method for different models.

In the following exercises, you will be introduced to various models to which you can apply your UQ clients. If you have your own models, try implementing them as UM-Bridge servers and solving them with your newly created UM-Bridge clients.

Note: Make sure that the input and output dimensions of your UM-Bridge clients and servers are compatible.


## 6 Advanced Models
In this fifth exercise we are looking at some more advanced models.

### 6.1 Three Body Problem
This exercise is about UQ for Bayesian Inverse Problem governed by ODEs and you will work on [Circular Restricted Three-Body Problem (CR3BP)](CR3BP/CR3BP_UQ.ipynb). Moreover, you will learn how to construct [Metropolis Hastings algorithm for CR3BP](CR3BP/CR3BP_MCMC.ipynb) which is a commonly acknowledge algorithm for MCMC.

### 6.2 Steady State Heat Conduction Problems
This is an exercise that concerns UQ for Bayesian Inverse Problem governed by a PDE. The PDE that you will consider is the [Steady State Heat Equation](Heat_Conduction/heatconduction_UQ.ipynb). Also, in this notebook [MCMC for Heat Equation](Heat_Conduction/heatconduction_MCMC.ipynb) you will gain an understanding of how to create the MCMC algorithm for this problem. 

### 6.3 A computaionally demanding Model
All the previouse models we have looked at so far can be fastly computed. This is not always the case. An example for a more computationaly demanding model is the [L2-Sea model](UQ/L2-benchmark_model.ipynb) from the UM-Bridge benchmark.

To test the L2-Sea modle have a look at the [client](UQ/L2-benchmark_client.ipynb).

## 7 High Performance Computing
In this exercise you will learn how to run your model on a High Performance Computer (HPC).
Letting your model run on a HPC is beneficial whenever it is computationally demanding and has a long processing time. The HPC can execute your model faster by for example running it in parallel. 

### 7.1 Register on the HPC
Register and Login to the HPC sytem of your choice.

### 7.2 Set up UM-Bridge
To set up UM-Bridge on the HPC log in to the HPC and follow the instructions from the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/umbridge/hpc.html) on HPCs.

### 7.3 Run a Model on the HPC
Go [here](UM-Bridge_on_bwUniCluster2.0.md) to get a detailed instructon on how to run a UM-Bridge server on the bwUniCluster2.0. If you are working with a different HPC system go to its documentary for more information.





