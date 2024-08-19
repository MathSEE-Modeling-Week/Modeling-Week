# MathSEE Modeling-Week

## Introduction 
In fields such as physics, economics, and statistics, complex models are constructed to replicate real-world phenomena. During this process, various types of uncertainties inevitably arise. A model is always an abstraction of reality and cannot incorporate every detail. This abstraction is crucial for focusing on significant aspects while ignoring less important details, making the complexity of reality more manageable and computable. However, this simplification introduces uncertainties.

Uncertainties can stem from naturally variable phenomena or from a lack of knowledge and the inability to account for all aspects of the real world. In response, Uncertainty Quantification (UQ) aims to address these uncertainties and evaluate their impact on a model’s output. To comprehensively understand the implications of these uncertainties, models must be computed multiple times with varying input values.

When examining a model we must first know what kind of UQ problem we are looking at. Our main focus in the following lies on forward and inverse problems.

In a forward problem, the analysis focuses on understanding how variations in input parameter values affect a model’s output. Often, uncertainties surround the exact values of a model’s input parameters, and only a range or a distribution of their values is known. By evaluating the model across these input values, not only can single output values be determined, but also knowledge about the distribution and the characteristics of these values throughout the output space is gained.

Conversely, in inverse problems, the input parameter values are unknown, but an observed outcome is available. The task here is to identify the input values that best explain the observed outcome. When used as input values for a model, those values should lead to an output close to the known observation.

The following exercises will lead you through differnt mathematical models and methods to solve them. You can follow the exercises below and at any point start working on your own projects. 
The exercises include mathematically modeled problems like the Heat Conduction Model and the 3 Body Problem. For the Uncertainty Quantification methods, you can find examples for classic Monte Carlo (MC), Quasi Monte Carlo (QMC), and Markov Chain Monte Carlo (MCMC). In exercise six you will learn how to run your models on a High Performance Computer.


When moving forward with the exercises we will introduce UM-Bridge. You can check out the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) and follow the Quickstart Guide and/or the Tutorial to get familiar with UM-Bridge.
The example solutions are all written in Python so we strongly suggest using Python as well, if you prefer another language make sure it is supported by UM-Bridge [here](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html).


## 1 The first exercise
In the first exercise we are looking at the Predator-Prey Model.

### 1.1 Predator-Prey Model
Get familiar with the [Predator-Prey Dynamical System](UQ/predprey.ipynb).

In exercise three we are going to look at the Predator-Prey Model as a UQ problem.

### 1.2 Integrate UM-Bridge
Now that you are familiar with the Predator-Prey Dynamical System, you can write the model as a UM-Bridge server.
Use the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html) to get to know UM-Bridge and then look at the implementation [here](UQ/predprey_server.ipynb).

When implementing your UM-Bridge server in a jupyter notebook it is necessary to add the following two lines at the very top of the cell:

```
import nest_asyncio
nest_asyncio.apply()
```

**The purpose of UM-Bridge:** UM-Bridge serves as an interface that enables communication between advanced computational models written in various programming languages. UM-Bridge views these models as functions mapping input vectors onto output vectors. The models are designed as servers that can connect to clients through HTTP. Server and client only exchange input and output data without any further information about each other’s implementation specifics. This way concearns stay seperated. (For further information read the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/index.html)).


## 2 Second exercise
In order to solve a Uncertainty Quantification problem a variey of methods can be used. In this exercise we are starting simple by getting to know the Monte Carlo method.

### 2.1 Monte Carlo
Get familiar with the [Monte Carlo](UQ/MC_1.1.ipynb) (MC) method. 
In the example we sample from the following distribution:

$X\sim \mathcal{N}(0.5, 0.01)$.

### 2.2 Monte Carlo as an UM-Bridge client
Implement the MC method as an UM-Bridge client. [Here](UQ/MC_1.3.ipynb) you can find an example client.

### 2.3 A simple model
Now you can test your MC client on a simple model. Implement a UM-Bridge server that solves the following function:

$f(x) = sin(2\pi x)$

Compare your implementation to the [example solution](UQ/MC_1.2.ipynb), to make sure your setup is correct.

### 2.4 Solve an integral using UM-Bridge
The last step of this first exercise is to combine the UM-Bridge server and the UM-Bridge client to solve the following integral:

$\int_{0}^{1} f(x) \\textit{d}x$.

First, run the server from **2.3**. Then connect the MC client to the server. Look at the result and vary the sample size until you get a satisfactory result. 

Note: If you are running your server and client in a notebook you must put them in two different files to prevent the server from blocking the client's execution.


## 3 Exercise three
In this exercise we are looking at the Predator-Prey Model as a UQ problem and solve it with the MC method

### 3.1 Predator-Prey Model as a UQ problem
Look at the following [notebook](UQ/predprey_UQ.ipynb) and get familiar with the problem.

### 3.2 MC client for Predator-Prey Model
Take a look at the [MC client](UQ/predprey_client.ipynb) for the Predator-Prey Model.

### 3.3 Solve the Predator-Prey UQ problem with UM-Bridge
To solve the Predator-Prey UQ problem with UM-Bridge, run the Predator-Prey client from exercise **1.2** and connect your MC client from exercise **3.2**.


## 4 Exercise four
In this exercise we explore variations of the Monte Carlo method.

### 4.1 Quasi Monte Carlo
Get familiar with the [quasi Monte Carlo](UQ/QMC.ipynb) (QMC) method and implement the method as an UM-Bridge client.

### 4.2 Markov Chain Monte Carlo
To solve inverse UQ problems take a look at the [Markov Chain Monte Carlo](UQ/MCMC.ipynb) (MCMC) method. 

### 4.3 The benefit of UM-Bridge
You might ask yourselves why we are implementing all these UQ methods as UM-Bridge clients instead of directly incorporating them into our models. What initially seems like an extra step actually provides a significant advantage: it allows you to implement your UQ code once and then apply it to any UM-Bridge model of your choice. This eliminates the need to repeatedly implement the same UQ method for different models.

In the following exercises, you will be introduced to various models to which you can apply your UQ clients. If you have your own models, try implementing them as UM-Bridge servers and solving them with your newly created UM-Bridge clients.

Note: Make sure that the input and output dimensions of your UM-Bridge clients and servers are compatible.


## 5 Exercise five
In this fifth exercise we are looking at some more advanced models.

### 5.1 Three Body Problem
This exercise is about UQ for Bayesian Inverse Problem governed by ODEs and you will work on [Circlar Restricted Three-Body Problem (CR3BP)](CR3BP/CR3BP_UQ.ipynb). Moreover, you will learn how to construct [Metropolis Hastings algorithm for CR3BP](CR3BP/CR3BP_MCMC.jpynb) which is a commonly acknowledge algorithm for MCMC.

### 5.2 Steady State Heat Conduction Problems
This is an exercise that concerns UQ for Bayesian Inverse Problem governed by a PDE. The PDE that you will consider is the [Steady State Heat Equation](Heat_Conduction/heatconduction_UQ.ipynb). Also, in this notebook [MCMC for Heat Equation](Heat_Conduction/heatconduction_MCMC.ipynb) you will gain an understanding of how to create the MCMC algorithm for this problem. 

### 5.3 A computaionally demanding model


## 6 Exercise six
In this exercise you will learn how to run your model on a High Performance Computer (HPC).
Letting your model run on a HPC is beneficial whenever it is computationally demanding and has a long processing time. The HPC can execute your model faster by for example running it in parallel. 

### 6.1 Register on the HPC
In this course we are using the [bwUniCluster2.0](https://wiki.bwhpc.de/e/BwUniCluster2.0).
To access this HPC follow the instruction for the [registration](https://wiki.bwhpc.de/e/Registration/bwUniCluster).

### 6.2 Set up UM-Bridge
To set up UM-Bridge on the HPC log in to the HPC and follow the instructions from the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/umbridge/hpc.html) on HPCs.

### 6.3 Run a model on the HPC
To run a model on the bwUniCluster2.0 it must be put into a container. The prefered container for the bwUniCluster2.0 is Docker but you can also use Singularity. You can follow the instructions below to run your model on the HPC UM-Bridge setup. 

1. **UM-Bridge server as a Python script:** First you have to have to transfere your UM-Bridge server into a Python script (.py). In the script you can loos the first two lines of code:
   ```
   import nest_asyncio
   nest_asyncio.apply()
   ```
   those are only necessary in notebooks.
3. **Install Docker:** Go to [Docker.com](https://www.docker.com/) and install Docker on your local machine.
4. **Sign up to Docker Hub:** Go to [Docker Hub](https://hub.docker.com/) and create an account.
5. **Write a Dockerfile:** To create a Docker container you need to write a Dockerfile and place it into the folder next to your Python script.
6. **Build the Docker image:** ```docker build -t my_server```
7. **Run the Docker container:** To finally run your UM-Bridge server from the Docker container do: ```docker run -it -p 4242:4242 my_server```
8. **Upload the container to Docker Hub**
   
   7.1 **Tag the Docker image:** ```docker tag my_server <yourusername>/my_server:latest```
   
   7.2 **Log in to Docker Hub:** ```docker login```
   
   7.3 **Push the image to Docker Hub:** ```docker push <yourusername>/my_server:latest```
   
   7.4 **Verify the upload:** ```docker run -it -p 4242:4242 <yourusername>/my_server```
   
8. **Upload the container to the HPC**
    
   8.1 **Log in to bwUniCluster2.0:** ```ssh <username>@bwunicluster.scc.kit.edu```

   
   8.2 **Import the container image with enroot:** ```enroot import docker://<yourusername>/my_server```
   
   8.3 **Create a container with enroot:** ```enroot create --name my_server <yourusername>+my_server.sqsh```
   
   8.4 **Start the container with enroot:** ```enroot strat my_server```
   
9. **Edit job.sh:** Go to the job.sh file in your UM-Bridge HPC setup and add the following line: ```enroot strat my_server```
10. **Run the load-balancer:** ```./load-balancer```
11. **Create a tunnel from your local machine to the HPC:** ```ssh <username>@bwunicluster.scc.kit.edu -N -f -L 4242:localhost:4242```
12. **Connect your UM-Bridge client through the tunnel** by simply running the client on your local machine on port 4242.






