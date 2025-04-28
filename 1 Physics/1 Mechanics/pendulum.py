import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
g = 9.81   
L = 1.0    
omega0 = np.sqrt(g / L)

# System of ODEs
def pendulum(t, y, b, omega0, A, omega_drive):
    theta, omega = y
    dydt = [omega, -b*omega - omega0**2 * np.sin(theta) + A*np.cos(omega_drive*t)]
    return dydt

# Simulation function
def simulate_pendulum(b, A, omega_drive, y0=[0.2, 0.0], t_span=(0,100), num_points=5000):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    sol = solve_ivp(pendulum, t_span, y0, t_eval=t_eval, args=(b, omega0, A, omega_drive))
    return sol.t, sol.y[0], sol.y[1]

# Example of plotting
def plot_simulation(b, A, omega_drive, title):
    t, theta, omega = simulate_pendulum(b, A, omega_drive)
    fig, axs = plt.subplots(1, 2, figsize=(12,5))
    
    axs[0].plot(t, theta)
    axs[0].set_title('Angle vs Time')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Angle (rad)')
    
    axs[1].plot(theta, omega)
    axs[1].set_title('Phase Portrait')
    axs[1].set_xlabel('Angle (rad)')
    axs[1].set_ylabel('Angular Velocity (rad/s)')
    
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

# Simulations
plot_simulation(b=0.0, A=0.0, omega_drive=2/3, title='Simple Pendulum')
plot_simulation(b=0.1, A=0.0, omega_drive=2/3, title='Damped Pendulum')
plot_simulation(b=0.0, A=1.2, omega_drive=2/3, title='Forced Pendulum')
plot_simulation(b=0.1, A=1.2, omega_drive=2/3, title='Forced Damped Pendulum - Moderate Chaos')
plot_simulation(b=0.2, A=1.5, omega_drive=2/3, title='Forced Damped Pendulum - Strong Chaos')