#!/usr/bin/env python
# coding: utf-8

# ### 1.2 UM-Bridge Model Integration
# 
# In this section, UM-Bridge model server can be found in the following. It is used to solve the steady state temperature distribution by considering the value of $k$ and number of grid of points as inputs. 

# In[ ]:


# umbridge server
import nest_asyncio
nest_asyncio.apply()
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special
from mpl_toolkits.mplot3d import axes3d
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from scipy.linalg import block_diag
import numpy
import umbridge
from scipy import linalg

class PDEModel(umbridge.Model):
    def __init__(self):
        super().__init__("forward")
        self.L = 4
       # self.k = 40
        self.g = 4 * 10**6
        self.T_0 = 200
        self.Deltax = Deltay = 1 
       # self.N = int(self.L/self.Deltax)
        
    def get_input_sizes(self, config):
        return [2]  # for the values k and n(number of mesh grid in a row)
        
    def get_output_sizes(self, config):
        return [9]  # for the output variables T
        
    def __call__(self, parameters, config):
        #g = parameters[0][0]
        k = parameters[0][0]
        n = parameters[0][1]
        A = self.f(n, config)
        b = self.h(n, self.g, k, config)
        T = self.solve(A, b, config)
        return [T.tolist()]
        
    # coefficient matrix
    def f(self, n, config):
        Ddiag  = -4 * np.eye(n-1)
        Dupper = np.diag([1] * (n - 2), 1)
        Dlower = np.diag([1] * (n - 2), -1)
        D = Ddiag + Dupper + Dlower
        Ds = [D] * (n- 1)
        B1  = block_diag(*Ds)
        I = np.ones((n - 1) * (n - 2))
        Iupper = np.diag(I, n - 1)
        Ilower = np.diag(I, -n + 1)
        B2 = Iupper + Ilower
        matrix = B1 + B2
        return matrix

    
    # matrix for the right hand side of the equation
    def h(self, n, g, k, config):
        b = np.zeros((n - 1)**2)
        b[:(n-1)] = -(g/k) * (self.Deltax **2) - self.T_0
        b[(n-1):(n - 1)**2]=  -(g/k) * (self.Deltax **2)
        return b

    
    # solve the linear system 
    def solve(self, x, y, config):
        solution = linalg.solve(x, y)
        return solution

        
    def supports_evaluate(self):
        return True

pde_model = PDEModel()
umbridge.serve_models([pde_model], 4242) # start model server 


# `======== Running on http://0.0.0.0:4242 ========
# (Press CTRL+C to quit)`
