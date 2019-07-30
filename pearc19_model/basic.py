
#PEARC19 Student Modeling Challenge
#Population Dynamics
#Team 4

'''
 VARIABLE DICTIONARY POPULATION DYNAMICS:
 --------------------------------------------------------------------
  The defining equations are:   
    Moose population: M[t+1] = M[t] + (M[t] * births per moose - M[t] * moose death fraction * W[t]) * ts
    Wolf population:  W[t+1] = W[t] + (W[t] * births per wolf * M[t] - W[t] * wolf death fraction) * ts
        
  brM : moose birth rate
  dfM : moose death fraction
  brW : wolf birth rate
  dfW : wolf death fraction
  ipM : initial moose population
  ipW : initial wolf population
 ---------------------------------------------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt

all = ['pop_dyn']


'''
Function to run the population dynamics model.
inputs : parameters for the model
outputs: time series, Moose pop., Wolf pop. 
'''
def pop_dyn(brM = 0.2,    #moose birth rate
            dfM = 0.003,  #moose death fraction
            brW = 0.001,  #wolf birth rate
            dfW = 0.5,    #wolf death fraction
            ipM = 25,     #initial moose population
            ipW = 800     #initial wolf population 
           ):   
    
    # Model parameters
    time_step = 0.0833    # simulation time step in years (a month)
    start_time = 0        # in years
    end_time = 50         # in years
    
    # Derived constants
    N = int((end_time - start_time) / time_step)    # number of simulation steps
    
    # Time-varying quantities, arrays with one value per time step
    t = np.zeros(N+1) # time in hours  
    M = np.zeros(N+1) # moose population  
    W = np.zeros(N+1) # wolf population

    t[0] = 0          
    M[0] = ipM
    W[0] = ipW

    # create a for loop that calculates both moose and wolf populations 
    # for a given simulation step

    for i in range(N):
        
        t[i+1] = t[i] + time_step
        M[i+1] = M[i] + (M[i]*brM - M[i]*dfM*W[i])*time_step
        W[i+1] = W[i] + (W[i]*brW - W[i]*dfW)*time_step

    return t,M,W
