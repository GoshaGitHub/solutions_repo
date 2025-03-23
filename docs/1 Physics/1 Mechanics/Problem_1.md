# Theoretical Basis: Projectile Motion

## 1. Motion of a Projectile
When a projectile (such as a ball, bullet, or rocket) is launched at an angle to the horizontal, it follows a parabolic trajectory. This occurs due to two forces:

- The horizontal velocity remains constant (assuming air resistance is negligible).
- The vertical velocity changes due to gravity.

### Key Equations of Motion
#### Horizontal coordinate (x):
\[
x = v_0 \cos(\theta) t
\]
where:
- \( v_0 \) is the initial velocity,
- \( \theta \) is the launch angle,
- \( t \) is the time.

#### Vertical coordinate (y):
\[
y = v_0 \sin(\theta) t - \frac{1}{2} g t^2
\]
where:
- \( g \) is the acceleration due to gravity (typically \( 9.81 \text{ m/s}^2 \)).

---

## 2. Range of Flight (R)
The range is the horizontal distance traveled by the projectile before it lands.

To find the range, we first determine the flight time (T), which is the time it takes for the projectile to return to the ground (\( y = 0 \)):
\[
T = \frac{2 v_0 \sin(\theta)}{g}
\]

Now, substituting \( T \) into the equation for \( x \):
\[
R = v_0 \cos(\theta) \cdot \frac{2 v_0 \sin(\theta)}{g}
\]

Using the trigonometric identity \( 2 \sin(\theta) \cos(\theta) = \sin(2\theta) \), we get:
\[
R = \frac{v_0^2 \sin(2\theta)}{g}
\]

---

## 3. Range Analysis Based on Angle
From the equation, we observe:

- Maximum range is achieved at \( \theta = 45^\circ \), since \( \sin(2\theta) = 1 \).
- If the angle is too small (\( \theta \approx 0^\circ \)), the projectile moves almost straight and falls nearby.
- If the angle is too large (\( \theta \approx 90^\circ \)), the projectile moves mostly upward and lands almost at the launch point.

