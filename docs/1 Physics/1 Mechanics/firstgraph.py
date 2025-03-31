import numpy as np
import matplotlib.pyplot as plt

def calculate_trajectory(v0, angle, g=9.81, b=0.1, with_air=False):
    angle_rad = np.radians(angle)

    if not with_air:
        t_flight = 2 * v0 * np.sin(angle_rad) / g
        t = np.linspace(0, t_flight, 100)
        x = v0 * np.cos(angle_rad) * t
        y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
    else:
        def y_func(t):
            return (v0*np.sin(angle_rad) + g/b)*(1-np.exp(-b*t))/b - g*t/b

        t_flight = 0
        dt = 0.01
        while y_func(t_flight) >= 0:
            t_flight += dt

        t = np.linspace(0, t_flight, 100)
        x = (v0 * np.cos(angle_rad) * (1 - np.exp(-b*t))) / b
        y = y_func(t)

    return x, y

v0 = float(input("Enter initial velocity (m/s): "))
angles = list(map(float, input("Enter angles (degrees, space-separated): ").split()))

plt.figure(figsize=(10, 6))
for angle in angles:
    x, y = calculate_trajectory(v0, angle, with_air=False)
    plt.plot(x, y, label=f'{angle}° (no air)')

    x_air, y_air = calculate_trajectory(v0, angle, with_air=True)
    plt.plot(x_air, y_air, '--', label=f'{angle}° (with air)')

plt.title(f'Projectile Trajectories (v0 = {v0} m/s)')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.axhline(0, color='black', linestyle='-', linewidth=0.5) 
plt.legend()
plt.grid(True)
plt.show()