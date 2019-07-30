
# population_dynamics_start.py
#
# VARIABLE DICTIONARY POPULATION DYNAMICS:
# --------------------------------------------------------------------
#  The defining equations are:   
#    Moose population: M[t+1] = M[t] + (M[t] * births per moose - M[t] * moose death fraction * W[t]) * ts
#    Wolf population:  W[t+1] = W[t] + (W[t] * births per wolf * M[t] - W[t] * wolf death fraction) * ts
#        
#  brM : moose birth rate
#  dfM : moose death fraction
#  brW : wolf birth rate
#  dfW : wolf death fraction
#  ipM : initial moose population
#  ipW : initial wolf population
# ---------------------------------------------------------------------

# Model parameters
time_step = 0.0833    # simulation time step in years (a month)
start_time = 0        # in years
end_time = 50         # in years
brM = 0.2           # Moose birth rate 
dfM = 0.003         # Moose death fraction due to wolves
brW = 0.001         # Wolf birth rate
dfW = 0.5           # Wolf death fraction
ipM = 500           # Initial moose population
ipW = 20            # Initial wolf population
# Derived constants
N = int((end_time - start_time) / time_step)    # number of simulation steps
# Time-varying quantities, arrays with one value per time step
# The syntax, "[0]*(N+1)," creates a one-dimensional array of length N+1 whose values are all zero.

t = [0]*(N+1)       # time in hours  
M = [0]*(N+1)       # moose population  
W = [0]*(N+1)       # wolf population
# TODO: Initialize variables
t[0] =           
M[0] = 
W[0] = 
# create a for loop that calculates both moose and wolf populations 
# for a given simulation step
for i in range(N):
    t[i+1] = t[i] + time_step
    
    # Calculate current moose population
    M[i+1] = M[i] + (M[i]*brM - M[i]*dfM*W[i])*time_step
    
    # TODO: Calculate current wolf population
    
    
# Now plot and show both populations on the same plot in respect to time  
    
# Plot the moose population
plt.plot(t, M, color = "blue", label = "Moose Population")
   
# TODO: Plot the wolf population.
# HINT: use color="red" and label="Wolf Population" to differentiate the moose plot from the wolf plot.



plt.show()

















