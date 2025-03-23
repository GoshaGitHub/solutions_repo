# Theoretical Basis: Projectile Motion

## 1. Motion of a Projectile
When a projectile (such as a ball, bullet, or rocket) is launched at an angle to the horizontal, it follows a parabolic trajectory. This occurs due to two forces:

- The horizontal velocity remains constant (if we don't take air resistance).
- The vertical velocity changes due to gravity.

### Key Equations of Motion
#### Horizontal coordinate (x):
$$
x = v_0 \cos(\theta) t
$$
where:
- $v_0$ is the initial velocity,
- $\theta$ is the launch angle,
- $t$ is the time.

#### Vertical coordinate (y):
$$
y = v_0 \sin(\theta) t - \frac{1}{2} g t^2
$$

where:
- $g$ is the acceleration due to gravity (typically $9.81 \text{ m/s}^2$).

---

## 2. Range of Flight (R)
The range is the horizontal distance traveled by the projectile before it lands.

To find the range, we first determine the flight time (T), which is the time it takes for the projectile to return to the ground ($y = 0$):
$$
T = \frac{2 v_0 \sin(\theta)}{g}
$$

Now, substituting $T$ into the equation for $x$:
$$
R = v_0 \cos(\theta) \cdot \frac{2 v_0 \sin(\theta)}{g}
$$

Using the trigonometric identity $2 \sin(\theta) \cos(\theta) = \sin(2\theta)$, we get:
$$
R = \frac{v_0^2 \sin(2\theta)}{g}
$$

---

## 3. Range Analysis Based on Angle
From the equation, we observe:

- Maximum range is achieved at $\theta = 45^\circ$, since $\sin(2\theta) = 1$.
- If the angle is too small ($\theta \approx 0^\circ$), the projectile moves almost straight and falls nearby.
- If the angle is too large ($\theta \approx 90^\circ$), the projectile moves mostly upward and lands almost at the launch point.
---
## 4. Python code for simulation
Also, to better understand projectile motion, I wrote a Python script that simulates and visualizes the trajectory of our projectile. The script plots the parabolic path of a projectile based on different launch angles and initial velocities, which you can write by yourself. It uses the `matplotlib` and `numpy` libraries to generate the graphs. Here is the code:

```python

    import numpy as np
    import matplotlib.pyplot as plt

    def draw_trajectories(angles, initial_velocity, g):
        plt.figure(figsize=(10, 5))
        
        for angle in angles:
            angle_rad = np.radians(angle)
            time_of_flight = (2 * (initial_velocity * np.sin(angle_rad))) / g
            t = np.linspace(0, time_of_flight, num=500)
            
            x = initial_velocity * np.cos(angle_rad) * t
            y = initial_velocity * np.sin(angle_rad) * t - 0.5 * g * t**2
            
            plt.plot(x, y, label=f'Angle: {angle}°')
        
        plt.title(f'Projectile Trajectories (Initial Velocity: {initial_velocity} m/s)')
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.legend()
        plt.grid(True)
        plt.show()

    initial_velocity = 20 
    g = 9.81

    angles = list(map(float, input("Enter angles separated by spaces (in degrees): ").split()))

    draw_trajectories(angles, initial_velocity, g)

