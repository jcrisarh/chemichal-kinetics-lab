from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt
def generate_temp_positions_and_remaining_interval(tf, dt):
    """Calculate the number of time points and the remaining time interval.

    Determine the number of temporal positions required to cover the
    simulation interval from zero to the final simulation time `tf`,
    using the requested time step `dt`. If `tf` is not an exact multiple
    of `dt`, include an additional time point at `tf` and calculate the
    remaining time interval required to reach it.

    ## Parameters

    tf : float
    Final simulation time.
    dt : float
    Requested time step size.

    ## Returns

    n_time_points : int
    Total number of time points required, including the initial
    and final time points.
    dt_final : float
    Remaining time interval after the regular time steps. Zero if
    no additional, shorter time step is required.
    """
    tf_decimal = Decimal(str(tf))
    dt_decimal = Decimal(str(dt)) #high precision decimals
    complete_steps = tf_decimal//dt_decimal
    pre_final_temp = complete_steps * dt_decimal
    delta_t_final = tf_decimal - pre_final_temp
    temp_positions = complete_steps + 1
    if delta_t_final != Decimal('0'):
        temp_positions = complete_steps + 2
    return int(temp_positions), int(complete_steps), float(delta_t_final)


def chemical_kinetics_one(a0, b0, x0, k, tf, dt):
    """Simulate the reaction A + B -> X using the explicit Euler method.

    ## Parameters

    a0 : float
    Initial concentration of reactant A (mol/L).
    b0 : float
    Initial concentration of reactant B (mol/L).
    x0 : float
    Initial concentration of product X (mol/L).
    k : float
    Reaction rate constant (L/(mol·s), assuming time is in seconds).
    tf : float
    Final simulation time (s).
    dt : float
    Time step for the explicit Euler method (s).

    ## Returns

    ...
    """
    temp_pos, steps, delta_fin = generate_temp_positions_and_remaining_interval(tf, dt)
    tarray = np.zeros((temp_pos, 4)) # temp_pos is the number of temporal positions until the simulation time
    t0 = 0                               #4 per storing time, X, A, B.
    tarray[0,0] = t0 #initial time
    tarray[0,1] = x0
    tarray[0,2] = a0
    tarray[0,3] = b0

    for i in range (1, steps + 1):
        t0 += dt
        rf = k*(a0*b0)
        dx = rf * dt
        x0 += dx
        a0 -= dx
        b0 -= dx
        tarray[i,0]=t0
        tarray[i,1]=x0
        tarray[i,2]=a0
        tarray[i,3]=b0
    
    if delta_fin !=0:
        rf = k*(a0*b0)
        dx = rf * delta_fin
        x0 += dx
        a0 -= dx
        b0 -= dx
        tarray[steps + 1, 0] = tf
        tarray[steps + 1 , 1] = x0
        tarray[steps + 1, 2] = a0
        tarray[steps + 1, 3] = b0

    return tarray
    #t = tarray[:,0]
    #x = tarray[:,1]
    #a = tarray[:,2]
    #b = tarray[:,3]	

    #plt.grid(True)
    #plt.grid(color = 'k', linewidth = 2)

    #plt.xlabel("tiempo (t)", fontsize = 20)
    #plt.ylabel("concentracion (C)", fontsize = 20)
    #plt.title("C vs t", fontsize = 20)

    #plt.plot(t, a, label="A")
    #plt.plot(t, b, label="B")
    #plt.plot(t, x, label="X")
    #plt.show()
    
