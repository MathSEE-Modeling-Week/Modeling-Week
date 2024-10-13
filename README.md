# MathSEE Modeling-Week

This work is licensed under [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Introduction 
Complex mathematical models are commonly used to describe and thus shed light on various real-world phenomena across sciences and technologies. They are essential tools in these fields because they allow us to explore, understand and predict complex phenomena in ways that would be impossible, impractical, or too costly to do through direct experimentation alone. During this process, various types of uncertainties inevitably arise. A model is always an abstraction of reality and cannot incorporate every detail. This abstraction is crucial for focusing on significant aspects while ignoring less important details, making the complexity of reality more manageable and computable. However, this simplification introduces uncertainties.

Uncertainties can stem from naturally variable phenomena, a lack of knowledge, or the inability to account for all aspects of the real world. Uncertainty Quantification (UQ) aims to address these uncertainties and evaluate their impact on a model’s output. To comprehensively understand the implications of these uncertainties, models must be computed multiple times with varying input values.

When examining a model, we must first know what kind of UQ problem we are looking at. Our primary focus in the following lies on forward and inverse problems.

In a forward problem, the analysis focuses on understanding how variations in input parameter values affect a model’s output. Often, uncertainties surround the exact values of a model’s input parameters, and only a range or a distribution of their values is known. By evaluating the model across these input values, not only can single output values be determined, but knowledge about the distribution and the characteristics of these values throughout the output space is also gained.

Conversely, in inverse problems, the input parameter values are unknown, but an observed outcome is available. The task is identifying the input values that best explain the observed outcome. When used as input values for a model, those values should lead to an output close to the known observation.

The following tutorials will introduce you to different mathematical models and methods for solving them. You can follow the tutorials below and, at any point, start working on your own projects. 
The tutorials include mathematically modeled problems like the Heat Conduction Model and the 3 Body Problem. For the Uncertainty Quantification methods, you can find examples of classic Monte Carlo (MC), Quasi Monte Carlo (QMC), and Markov Chain Monte Carlo (MCMC). Tutorial six will teach you how to run your models on a high-performance computer.


When proceeding with the tutorials, we will introduce UM-Bridge. To familiarize yourself with UM-Bridge, you can check out the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) and follow the Quickstart Guide and/or the Tutorial. The example solutions are all written in Python, so we strongly suggest using it as well. If you prefer another language, make sure it is supported by UM-Bridge [here](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html).

## 1 Basic Modeling
In this first tutorial, we'll familiarize ourselves with ordinary differential equations (ODEs) and how they can be used to model real-world interactions between two species. Specifically, we'll explore the Lotka-Volterra equations, which describe the dynamics between predators and prey. We use this as a reference because it is a real-world example that, while not too complex, effectively demonstrates the interactions between different species.

### 1.1 Predator-Prey Model
Let's look at the first notebook: [Predator-Prey Dynamical System](Models/Predator-Prey/predprey.ipynb). It contains a model description and tutorials to help you study and understand the system.

The third tutorial will examine the Predator-Prey Model as a UQ problem.

## 2 UM-Bridge
In this section, we will learn about the UM-Bridge interface.

**The purpose of UM-Bridge:** UM-Bridge serves as an interface that enables communication between advanced computational models written in various programming languages. UM-Bridge views these models as functions mapping input vectors onto output vectors. The models are designed as servers that can connect to clients through HTTP. The server and client only exchange input and output data without further information about each other’s implementation specifics. This way, concerns stay separated; for details, we refer to the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html).

### 2.1 A Simple Model
To get familiar with UM-Bridge, let's start by implementing a simple server for the following function:

$f(x) = sin(2\pi x)$.

This model will serve as a basic example of how UM-Bridge works. The function takes an input $x$ and returns the function value $sin(2 \pi x)$.

When implementing your UM-Bridge server in a Jupyter notebook, it is necessary to add the following two lines at the very top of the cell:

```
import nest_asyncio
nest_asyncio.apply()
```

This ensures compatibility with the notebook environment. To learn about the correct implementation of a UM-Bridge server, go to the [Model section](https://um-bridge-benchmarks.readthedocs.io/en/docs/umbridge/models.html) of the UM-Bridge documentation. 

To ensure that your setup is correct, compare your implementation to the [example solution](UQ/Monte_Carlo/MC_server.ipynb).

### 2.2 Predator-Prey Model as UM-Bridge Server
Once you're comfortable with the simple example from 2.1, the next step is implementing the Predator-Prey model (introduced in 1.1) as an UM-Bridge server. The Predator-Prey model is more complex and will help you see how UM-Bridge can manage multi-dimensional models.

For further details on UM-Bridge server implementation, revisit the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html). Once you're finished or if you need help, you can just refer to the sample implementation of the Predator-Prey Model server [here](Models/Predator-Prey/predprey_server.ipynb) for guidance. 

After starting the notebook, your server will run and be ready to handle requests from a client. Since the model itself has been implemented, we can proceed to make model evaluations. A client request corresponds to a function evaluation of the Lotka-Volterra system. To see how you can interact with the server and evaluate the model, refer to the [first client](Models/Predator-Prey/predprey_firstclient.ipynb). This notebook demonstrates connecting to the Predator-Prey Model server and performing function evaluations by specifying the model parameters.

For a more detailed explanation of UM-Bridge clients, check out the [Client section](https://um-bridge-benchmarks.readthedocs.io/en/docs/umbridge/clients.html) in the UM-Bridge documentation.

**Note**: If you are running your UM-Bridge server and client in a notebook, you must put them in two files to prevent the server from blocking the client's execution.

## 3 Basic UQ Methods

A variety of methods can be used to solve an uncertainty quantification (UQ) problem. In this section, we will start by learning the Monte Carlo (MC) method.

### 3.1 Monte Carlo
Let's get familiar with the [Monte Carlo](UQ/Monte_Carlo/MC.ipynb) (MC) method first. In the example, we sample from the following distribution:

$X\sim \mathcal{N}(0.5, 0.1)$.

You can find a few tasks in the notebook, such as varying the sample size or changing the distribution. These will help you explore how different parameters influence the results and how the Monte Carlo method works in practice.

### 3.2 Monte Carlo as a UM-Bridge Client
Next, you will implement the MC method as a UM-Bridge client. [Here](UQ/Monte_Carlo/MC_client.ipynb) you can find an example MC client template.

#### Solve an Integral using UM-Bridge
The final step of this tutorial involves using the UM-Bridge framework to solve the following integral:

$\int_{0}^{1} f(x) \\textit{d}x$, where $f(x) = sin(2\pi x)$.

1. Run the [UM-Bridge server](UQ/Monte_Carlo/MC_server.ipynb) as defined in section **2.1** to set up the model.
2. Connect the [MC client](UQ/Monte_Carlo/MC_client.ipynb) to the server and evaluate the function $f(x)$ at random points $X_i \sim \mathcal{U}([0, 1])$.
3. Look at the result of the MC estimator and vary the sample size $N$ to see how it affects the estimate's accuracy.

## 4 UQ Application
In this tutorial, we examine the Predator-Prey Model from section 1 as a UQ problem and solve it using the MC method.

### 4.1 Predator-Prey Model as a UQ problem
For details on the UQ problem, please look at the following [notebook](Models/Predator-Prey/predprey_UQ.ipynb). In this case, we consider a forward UQ problem where perturbations in the initial conditions for both predator and prey populations occur. The notebook also includes a Monte Carlo simulation, though it does not utilize the UM-Bridge framework.

### 4.2 MC Client for Predator-Prey Model
Implement the MC simulation for the Predator-Prey Model as a UM-Bridge client. For a sample solution, refer to the  [MC client](Models/Predator-Prey/predprey_client.ipynb) for the Predator-Prey Model.

To solve the UQ problem for the Predator-Prey model with UM-Bridge, follow these steps:

1. Run the [Predator-Prey model](Models/Predator-Prey/predprey_server.ipynb) from tutorial 2.2 to set up the server.
2. Connect your MC client to the server and perform the simulation to evaluate the effect of uncertainty in the initial conditions.


## Next Steps: Exploring Models and UQ Methods
So far, you've been introduced to various simple models, UQ methods, and the UM-Bridge interface, gaining a foundational understanding of how these components work together. From this point on, you can choose to dive deeper into either advanced UQ methods (Section 5), more complex models (Section 6), or HPC (Section 7).

We encourage you to form teams and work on projects, focusing on one of these areas. Modeling teams formulate a UQ problem, determining whether it is a forward or inverse problem. UQ teams study a UQ method. Ultimately, it would be ideal if modeling teams and UQ teams collaborated. You can either work on one of the following topics or one of the topics proposed by the researchers during the Modeling Week.

---
## 5 Advanced UQ Methods
In this tutorial, we explore variations of the Monte Carlo method by introducing the Quasi-Monte Carlo (QMC) and Markov Chain Monte Carlo (MCMC) methods. These methods build upon concepts from the previous section and offer different approaches to improving convergence and solving specific types of problems.

### 5.1 Quasi Monte Carlo
The QMC method enhances classic Monte Carlo sampling by using low-discrepancy sequences for more uniform sampling. Get familiar with the [Quasi Monte Carlo](UQ/Quasi_Monte_Carlo/QMC.ipynb) (QMC) method and implement it as a UM-Bridge client. You can find a sample solution [here](UQ/Quasi_Monte_Carlo/QMC_client.ipynb).

### 5.2 Markov Chain Monte Carlo
In this section, you will explore the Markov Chain Monte Carlo (MCMC) method's general principles, focusing on the Metropolis-Hastings algorithm. The [notebook](UQ/Markov_Chain_Monte_Carlo/MCMC.ipynb) demonstrates how to apply MCMC sampling to a 2D target distribution and provides an example using a UM-Bridge benchmark as target distribution. MCMC can be used to solve inverse UQ problems. Try implementing the given 2D target distribution as an UM-Bridge model (server) and the introduced Metropolis-Hastings algorithm as a UM-Bridge client. You can find a sample solution for the model [here](UQ/Markov_Chain_Monte_Carlo/MCMC_posterior_server.ipynb) and for the client [here](UQ/Markov_Chain_Monte_Carlo/MCMC_client.ipynb).

### 5.3. Mulitlevel Monte Carlo
If you are interested in learning more about the Multilevel Monte Carlo method, you can check out [this notebook](UQ/Multilevel_Monte_Carlo/Exercise_MLMC.ipynb).

### 5.4. Multilevel Markov Chain Monte Carlo
If  you are interested in learning more about the Multilevel Monte Carlo method, you can check this [paper](https://doi.org/10.1137/19M12696). 

---
### The Benefit of UM-Bridge
You might ask yourselves why we are implementing all these UQ methods as UM-Bridge clients instead of directly incorporating them into our models. What initially seems like an extra step provides a significant advantage: it allows you to implement your UQ code once and then apply it to any UM-Bridge model of your choice. This eliminates the need to implement the same UQ method for different models repeatedly.

In the following tutorials, you will be introduced to various models you can apply to your UQ clients. If you have your own models, try implementing them as UM-Bridge servers and solving them with your newly created UM-Bridge clients.

Note: Make sure that the input and output dimensions of your UM-Bridge clients and servers are compatible.

---

## 6 Advanced Models
In this section, we examine some more advanced, real-life models. Once we identify the UQ challenge, we apply appropriate methods to quantify the uncertainties. As in the previous sections, we provide the models through UM-Bridge, referring to those with server-client integration.

### 6.1 Three-Body Problem
This tutorial is about UQ for Bayesian Inverse Problems governed by ODEs, and you will work on [Circular Restricted Three-Body Problem (CR3BP)](Models/CR3BP/CR3BP_UQ.ipynb). You can review the construction of the UM-Bridge server [here](Models/CR3BP/CR3BP_server.ipynb), for this model. Moreover, you will learn how to construct [Metropolis Hastings algorithm for CR3BP](Models/CR3BP/CR3BP_client.ipynb), a commonly acknowledged MCMC algorithm. 

### 6.2 Steady State Heat Conduction Problems
This is a tutorial that concerns UQ for Bayesian Inverse Problems governed by PDEs. The PDE that you will consider is the [Steady State Heat Equation](Models/Heat_Conduction/heatconduction_UQ.ipynb). To implement the model, check the UM-Bridge server [here](Models/Heat_Conduction/heatconduction_server.ipynb). Also, in this notebook [MCMC for Heat Equation](Models/Heat_Conduction/heatconduction_client.ipynb) you will gain an understanding of how to create the MCMC algorithm for this problem. 

### 6.3 Groundwater Flow and Contaminant Transportation 
If you would like to advance your work in modeling, consider working on the tutorials related to Groundwater Flow and Contaminant Transportation [Exercise 1](Models/Groundwater_Flow_and_Contaminant_Transport/Exercise_ContaminantTransport_ForwardUQ.ipynb), [Exercise 2](Models/Groundwater_Flow_and_Contaminant_Transport/Exercise_ContaminantTransport_InverseUQ.ipynb). Each tutorial addresses different types of uncertainties. As you dive into these problems, you may implement and solve the model using the UM-Bridge server and client. 

### 6.4 A computationally demanding Model
All the previous models we have examined so far can be quickly computed, but this is not always the case. An example of a more computationally demanding model is the [L2-Sea model](Models/L2-Sea/L2-benchmark_model.ipynb) from the UM-Bridge benchmark. To test the L2-Sea model, please take a look at the [client](Models/L2-Sea/L2-benchmark_client.ipynb).

## 7 High Performance Computing
This tutorial teaches you how to run your model on a high-performance computer (HPC).
Letting your model run on an HPC is beneficial whenever it is computationally demanding and has a long processing time. The HPC can execute your model faster by, for example, running it in parallel. It will also save your personal computer from having to put all its computational power into computing the model.

### 7.1 Register on the HPC
Register and log in to the HPC system of your choice.

### 7.2 Set up UM-Bridge
To set up UM-Bridge on the HPC log and follow the instructions from the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/umbridge/hpc.html) on HPCs.

### 7.3 Run a Model on the HPC
Go [here](bwUniCluster20.md) for detailed instructions on running a UM-Bridge server on bwUniCluster2.0. If you are working with a different HPC system, go to its documentary for further information.
