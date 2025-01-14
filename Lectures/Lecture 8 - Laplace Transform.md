---
tags:
  - Marinus
  - Lectures
  - _FirstPass
  - LLM
---
All topics are covered in the lectures
have a look at the tutorials on how to solve the questions
Take time to solve multiple choice questions in past exams, they are similar to the open questions

answer sheet
formula sheet
scratch paper

# Recap: z-Transform

- The z-domain is a place where we can treat signals as a bunch of polynomials
- z transform as a discrete signal

## Overview
- The z-transform is a generalization of the frequency response in discrete time:
    - Represents signals and systems as a polynomial for the complex variable $z$.
    - The z-transform of a length-$L$ discrete signal $x[n]$ is given by:

      $$
      X(z) = \sum_{k=0}^{L-1} x[k] z^{-k}, \tag{1}
      $$

- The system function is the z-transform of a system:

  $$
  H(z) = \sum_{k=0}^{M} b_k z^{-k} = \sum_{k=0}^{M} h[k] z^{-k}, \tag{2}
  $$

- The relationship between the frequency domain and the z-domain is:

  $$
  H(e^{j\omega}) = H(z) \big|_{z = e^{j\omega}} \tag{3}
  $$

## z-Domain Relationships
- The z-domain connects the time domain and the frequency domain:
    - From **time domain**: $H(z) = \sum_k h[n] z^{-k}$.
    - To **frequency domain**: 

      $$
      H(e^{j\omega}) = H(z) \big|_{z = e^{j\omega}} = \sum_k h[n] e^{-j\omega k}.
      $$

![[Pasted image 20250114131142.png]]
- Certain patterns and characteristics are much more clear in some domains as another.

	Week 3-7 we were in the discrete frequency domain now lets go to the continuous time domain
# The Continuous Fourier Transform (CFT)

## Definition
- Consider a continuous-time signal $x(t)$. The Continuous Fourier Transform (CFT) for $x(t)$ is defined as:

  $$
  X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt. \tag{4}
  $$

- The resulting $X(\omega)$ represents the signal in the **continuous frequency domain**.

## Inverse Continuous Fourier Transform
- The inverse CFT of $X(\omega)$ is given by:

  $$
  x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega) e^{j\omega t} d\omega. \tag{5}
  $$

## Interpretation
- Equation (5) indicates the weight or importance of each frequency $\omega$ in the original signal $x(t)$ as represented by $X(\omega)$.

# Convolution in the Continuous Time

## Definition
- The convolution of two continuous-time signals $x(t)$ and filter $h(t)$ is defined as:

  $$
  y(t) = h(t) \ast x(t) = \int_{-\infty}^{\infty} h(\tau) x(t - \tau) d\tau. \tag{6}
  $$
- instead of a sum we have an integral
## Properties in the Frequency Domain
- In the continuous-time domain, **convolution** is equivalent to **multiplication** in the frequency domain. 
- Specifically, the Fourier transform of the convolution of two signals equals the product of their Fourier transforms:

  $$
  y(t) = h(t) \ast x(t) \longleftrightarrow Y(\omega) = H(\omega) X(\omega),
  $$

  where:
    - $Y(\omega)$ is the Fourier transform of $y(t)$,
    - $X(\omega)$ is the Fourier transform of $x(t)$,
    - $H(\omega)$ is the Fourier transform of $h(t)$.

# LTI Systems and ODEs

## Key Concepts
- In **discrete time**, LTI systems can be represented by **difference equations**.
- In **continuous time**, **Causal LTI systems** can be represented by **ordinary differential equations (ODEs)**.

## General Form of a Causal LTI System
- The general form of a causal LTI system in continuous time as an ODE is given by:

  $$
  \sum_{k=0}^{N} a_k \frac{d^k y(t)}{dt^k} = \sum_{k=0}^{M} b_k \frac{d^k x(t)}{dt^k},
  $$
- Left: feedback
- Right: feedforward
  where:
    - $x(t)$ is the **input**,
    - $y(t)$ is the **output**,
    - $a_k$ and $b_k$ are the **system coefficients**.

## Important Note
- The system requires **initial conditions** to be fully defined.

# LTI Systems and ODEs - Example

## Problem Statement
- Consider the following LTI system in continuous time:

  $$
  a_1 \frac{dy(t)}{dt} + a_0 y(t) = b_0 x(t).
  $$

## Solution
- The solution for the system is given by:

  $$
  y(t) = \frac{b_0}{a_1} \int_{-\infty}^{t} x(\tau) e^{\frac{a_0}{a_1}(t-\tau)} d\tau.
  $$

## Impulse Response
- To compute the impulse response of the system, i.e., $x(t) = \delta(t)$:

  $$
  y(t) = \frac{b_0}{a_1} e^{-\frac{a_0}{a_1} t} u(t),
  $$

  where $u(t)$ is the unit step function.
- as you can see, close relationship between discrete and continuous systems
- z-transform analysis: there is a similar expression of a coeff, coeff and continuous step
- 
## Discussion
- Does this look familiar from the discrete-time case?
- Under what conditions is the system **stable** (i.e., bounded output)?
	- ratio between a1 and a0 needs to be bigger than 0 
	- decay to zero
	- assess the stability 
	- can we do it simpler?
		- yes layer, laplace transform

---
# The Laplace Transform

## Definition
- The Laplace transform is a generalization of the Fourier transform. It is defined as:

  $$
  X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} dt, \tag{7}
  $$

  where $s$ is a complex number.
  - x(s) closely related to the frequency domain

## One-Side Laplace Transform
- The Laplace transform can be simplified by looking at the **one-side Laplace transform**, which is defined as:

  $$
  X(s) = \int_{0}^{\infty} x(t) e^{-st} dt, \tag{8}
  $$

  under the assumption that $x(t) = 0$ for $t < 0$.
  - for simplified calculations

- The one-side Laplace transform is denoted as $X(s) = \mathcal{L}\{x(t)\}$.

# The Inverse Laplace Transform

## Definition
- The inverse Laplace transform is defined as:

  $$
  x(t) = \lim_{T \to \infty} \frac{1}{2\pi j} \int_{\gamma - jT}^{\gamma + jT} X(s) e^{st} ds, \tag{9}
  $$

  where $\gamma$ is a real number such that the integral converges.

## Practical Use
- In practice, already-known Laplace transforms are used to find the inverse Laplace transform.
- The inverse Laplace transform is denoted as:

  $$
  x(t) = \mathcal{L}^{-1}\{X(s)\}.
  $$
# Relation Between the Laplace and Fourier Transforms

## Key Concept
- The Fourier transform is a special case of the Laplace transform when $s = j\omega$.
- The Fourier transform of a signal $x(t)$ is given by:

  $$
  X(j\omega) = X(s) \big|_{s = j\omega}.
  $$

## Recall
- In discrete time, the $z$ variable is related to the frequency domain by:

  $$
  X(e^{j\omega}) = X(z) \big|_{z = e^{j\omega}}.
  $$

- This slight difference in relation has relevant implications for the poles and zeros of the Laplace transform.

# Detailed Relation Between the Laplace and Fourier Transforms

## Key Derivation
- Consider the Laplace transform of a signal $x(t)$, denoted as $X(s)$, where $s = \sigma + j\omega$.
- The Laplace transform can be expressed as:

  $$
  X(s) = \int_{-\infty}^\infty x(t) e^{-st} dt,
  $$

  which expands to:

  $$
  X(s) = \int_{-\infty}^\infty x(t) e^{-(\sigma + j\omega)t} dt.
  $$

  Simplifying further:

  $$
  X(s) = \int_{-\infty}^\infty (x(t) e^{-\sigma t}) e^{-j\omega t} dt.
  $$

  Finally:

  $$
  X(s) = \mathcal{F}\{x(t)e^{-\sigma t}\},
  $$

  where $\mathcal{F}$ denotes the Fourier transform.

## Interpretation
- The Laplace transform of a signal $x(t)$ can be seen as the **Fourier transform** of the signal $x(t)e^{-\sigma t}$.

# Properties of the Laplace Transform

## Key Properties

### Linearity
- The Laplace transform is linear:

  $$
  \mathcal{L}\{a x_1(t) + b x_2(t)\} = a X_1(s) + b X_2(s).
  $$

### Time Shifting
- Time-shifting property:

  $$
  \mathcal{L}\{x(t - t_0)\} = e^{-s t_0} X(s).
  $$

### Frequency Shifting
- Frequency-shifting property:

  $$
  \mathcal{L}\{e^{at} x(t)\} = X(s - a).
  $$

## Note
- These properties are derived from the definition of the Laplace transform and the properties of the exponential function.

# Convolution in the Laplace Domain

## Key Concept
- Convolution in the time domain is equivalent to multiplication in the Laplace domain.

## Relation
- In the time domain:

  $$
  y(t) = x(t) \ast h(t),
  $$

- In the Laplace domain:

  $$
  Y(s) = X(s) H(s).
  $$

This property highlights the efficiency of using the Laplace transform for analyzing linear time-invariant (LTI) systems.


# Properties of the Laplace Transform

## Derivative
- The Laplace transform of a derivative of a signal is given by:

  $$
  \mathcal{L} \left\{ \frac{d^n x(t)}{dt^n} \right\} = s^n X(s) - s^{n-1} x(0) - s^{n-2} \frac{dx(0)}{dt} - \dots - \frac{d^{n-1} x(0)}{dt^{n-1}},
  $$

  with initial conditions $x(0)$, $\frac{dx(0)}{dt}$, ..., $\frac{d^{n-1} x(0)}{dt^{n-1}}$.

## Integral
- The Laplace transform of the integral of a signal is given by:

  $$
  \mathcal{L} \left\{ \int_{0}^{t} x(\tau) d\tau \right\} = \frac{1}{s} X(s).
  $$

# Relevant Laplace Transform Pairs

| **Function**                    | **Time Domain**                   | **s-Domain**                                     |
|----------------------------------|------------------------------------|-------------------------------------------------|
| **Unit pulse**                  | $\delta(t)$                       | $1$                                             |
| **Delayed pulse**               | $\delta(t - \tau)$                | $e^{-\tau s}$                                   |
| **Unit step**                   | $u(t)$                            | $\frac{1}{s}$                                   |
| **Ramp**                        | $t u(t)$                          | $\frac{1}{s^2}$                                 |
| **Exponential decay**           | $e^{-at} u(t)$                    | $\frac{1}{s + a}$                               |
| **Sine**                        | $\sin(\omega t) u(t)$             | $\frac{\omega}{s^2 + \omega^2}$                 |
| **Cosine**                      | $\cos(\omega t) u(t)$             | $\frac{s}{s^2 + \omega^2}$                      |
| **Exponentially Decaying Sine** | $e^{-at} \sin(\omega t) u(t)$     | $\frac{\omega}{(s + a)^2 + \omega^2}$           |
| **Exponentially Decaying Cosine** | $e^{-at} \cos(\omega t) u(t)$   | $\frac{s + a}{(s + a)^2 + \omega^2}$            |
*Table: Relevant Laplace Transform Pairs*

# ODEs and the Laplace Transform

## Key Concept
- An ODE (with well-defined initial conditions) is given by:

  $$
  \sum_{k=0}^{N} a_k \frac{d^k y(t)}{dt^k} = \sum_{k=0}^{M} b_k \frac{d^k x(t)}{dt^k},
  $$

- In the **s-domain**, the ODE becomes a polynomial equation in $s$ of the form:

  $$
  \sum_{k=0}^{N} a_k s^k Y(s) = \sum_{k=0}^{M} b_k s^k X(s),
  $$

  where:
    - $X(s)$ and $Y(s)$ are the **Laplace transforms** of $x(t)$ and $y(t)$, respectively.
    - $\{a_k\}_{k=0}^{N}$ and $\{b_k\}_{k=0}^{M}$ are the **system coefficients**.
- We have a polynomial in the s-domain and we do what we want with it into the time domain or something magical like that.

# Transfer Function

## Definition
- The transfer function of a system is defined as:
- b - coeffs of input 
- a - coeffs of the output

  $$
  H(s) = \frac{Y(s)}{X(s)} = \frac{\sum_{k=0}^{M} b_k s^k}{\sum_{k=0}^{N} a_k s^k}.
  $$

## Solving the ODE in the s-Domain
- Solving the ODE in the **s-domain** is equivalent to solving a polynomial equation in $s$.
- The solution of the ODE in the s-domain is given by:

  $$
  Y(s) = H(s) X(s).
  $$

- To return to the time domain, take the **inverse Laplace transform** of $Y(s)$.

## Note
- In practice, computing the inverse Laplace transform involves:
    - Using tables,
    - Techniques such as partial fraction decomposition,
    - Software with symbolic computation capabilities (e.g., MATLAB, Mathematica, or Python-sympy).


# Example: LTI System

## Problem
- Consider the LTI system:

  $$
  a_1 \frac{dy(t)}{dt} + a_0 y(t) = b_0 x(t),
  $$
We need to move the expression to the s-domain and then solve as a polynomial for y
  with initial conditions:
  - $y(0) = 0$,
  - $x(0) = 0$.

## Solution
- Taking the Laplace transform of the system gives:

  $$
  a_1 s Y(s) + a_0 Y(s) = b_0 X(s).
  $$

- Solving for the transfer function:

  $$
  H(s) = \frac{Y(s)}{X(s)} = \frac{b_0}{a_1 s + a_0}.
  $$
# Example: LTI System (Stability Analysis)

## System Output
- The output of the system is given by:

  $$
  Y(s) = H(s) X(s) = \frac{b_0}{a_1 s + a_0} X(s).
  $$

- Let the input $x(t) = \delta(t)$, so $X(s) = 1$. Then:

  $$
  Y(s) = \frac{b_0}{a_1} \left( \frac{1}{s + a_0 / a_1} \right).
  $$
have a look at [[Lecture 8 - Laplace Transform#Relevant Laplace Transform Pairs]]
specifically exponential decay
## Inverse Laplace Transform
- Taking the inverse Laplace transform of $Y(s)$:

  $$
  y(t) = \mathcal{L}^{-1}\{Y(s)\} = \mathcal{L}^{-1} \left\{ \frac{b_0}{a_1} \cdot \frac{1}{s + a_0 / a_1} \right\}.
  $$

- Using Laplace transform tables, the result is:

  $$
  y(t) = \frac{b_0}{a_1} e^{-\frac{a_0}{a_1} t} u(t).
  $$

## Question
- **What are the conditions in the s-domain for the system to be stable?**
  - The system is stable if all poles of $H(s)$ have negative real parts (i.e., the real part of $-a_0 / a_1$ must be negative).
- analysing the poles of the (s+a0/a1)
- apparently s-domain is fantastic.
	- wish i knew what he was talking about.

# Stability Analysis in the Continuous Domain

## Initial Value Theorem
- If $x(t) = 0$ for $t < 0$, and $x(t)$ does not have any impulses at $t = 0$, then:

  $$
  \lim_{t \to 0^+} x(t) = \lim_{s \to \infty} sX(s).
  $$

## Final Value Theorem
- If $x(t) = 0$ for $t < 0$, and $x(t)$ has a finite limit as $t \to \infty$, then:

  $$
  \lim_{t \to \infty} x(t) = \lim_{s \to 0} sX(s).
  $$

### Notes
- These theorems provide a convenient way to determine the initial and final values of a time-domain signal directly from its Laplace transform.


# Poles and Zeroes

## Transfer Function Representation
- The transfer function can be rewritten as:

    $$
    H(s) = G \frac{\prod_{m=0}^{M} (s - z_m)}{\prod_{n=0}^{N} (s - p_n)},
    $$

where:
	- $G$ is a constant,
	- $z_i$ are the roots of the numerator (zeroes of the transfer function),
	- $p_i$ are the roots of the denominator (poles of the transfer function).

## Stability Condition
- For a system $H(s)$ to be stable:
    - All poles must be in the **left half of the complex $s$-plane**, i.e., $\text{Re}\{p_i\} < 0$.
    - first order system some condition a0 / a1 
	    - generalised condition 
	    - if real part of pulse is positive: system is stable

# Example: Transfer Function Analysis

## Transfer Function
- Consider the transfer function:

    $$
    H(s) = \frac{Y(s)}{X(s)} = \left( \frac{b_0}{a_1} \right) \left( \frac{1}{s + a_0 / a_1} \right).
    $$

## Analysis
- There are **no zeroes** for $b_0 \neq 0$.
- The poles of the system are given by the roots of the denominator, i.e.:

    $$
    s = -\frac{a_0}{a_1}.
    $$

- The system is **stable** if the ratio $a_0 / a_1 > 0$.

# Applications of the Laplace Transform

## Overview
- The Laplace Transform is a powerful tool for modeling and analyzing systems.
- Three applications of the Laplace Transform include:

    - **Mechanical spring-damper system**.
    - **Armature-controlled DC motor**.
# Mechanical Spring-Damper System

![[Pasted image 20250114140844.png]][[lec8-main.pdf#page=51&offset=28.346,255.118|lec8-main, Applications of the Laplace Transform]]

## System Description
- Consider a mechanical spring-damper system with:
    - Mass: $M$,
    - Spring constant: $k$,
    - Friction coefficient: $r$.

- The equation of motion for the system is:

    $$
    M \frac{d^2 y(t)}{dt^2} + r \frac{dy(t)}{dt} + k y(t) = x(t),
    $$

    where:
        - $x(t)$ is the input force,
        - $y(t)$ is the output displacement.

## Initial Conditions
- Assume:
    - $y(0) = 0$,
    - $\frac{dy(t)}{dt} \big|_{t=0} = 0$.

## Laplace Transform
- Taking the Laplace transform of the equation of motion gives:

    $$
    M s^2 Y(s) + r s Y(s) + k Y(s) = X(s).
    $$
## Transfer Function
- The transfer function of the system is:

    $$
    H(s) = \frac{Y(s)}{X(s)} = \frac{1}{M s^2 + r s + k} = \frac{1/M}{s^2 + 2 \zeta \omega_n s + \omega_n^2},
    $$

    where:
        - $\zeta = \frac{r}{2\sqrt{M k}}$ (damping ratio),
        - $\omega_n = \sqrt{\frac{k}{M}}$ (natural frequency).

## System Properties
- The system does not have zeroes.
- The poles are given by (abc formula): $$
    s_{1,2} = -\zeta \omega_n \pm \omega_n \sqrt{\zeta^2 - 1}.
    $$

## Transfer Function
- When $\zeta_n = 1$, the transfer function of the system becomes:
$$
    H(s) = \frac{1/M}{s^2 + 2\omega_n s + \omega_n^2} = \frac{1/M}{(s + \omega_n)^2}.
    $$

## System Poles
- The poles of the system are:
$$
    s_{1,2} = -\omega_n.
    $$

## Impulse Response
- The impulse response of the system is given by:
$$
    h(t) = \frac{1}{M} t e^{-\omega_n t} u(t),
    $$

    where $u(t)$ is the unit step function.

# Armature-controlled DCmotor

![[Pasted image 20250114141321.png]]

## Circuit Equation
- The linear model of the DC motor circuit is given by:
$$
    L_a \frac{di_a(t)}{dt} + R_a i_a(t) + k_f \omega(t) = V_a(t),
    $$

    where:
        - $i_a(t)$: armature current,
        - $\omega(t)$: angular velocity,
        - $V_a(t)$: input voltage,
        - $L_a$: inductance,
        - $R_a$: resistance,
        - $k_f$: feedback factor.

## Torque Equation
- The torque $T_m$ developed by the motor is given by:
$$
    T_m(t) = k_m i_a(t),
    $$

    where $k_m$ is the motor constant.

## Net Torque Equation
- The model for the net torque $T_{\text{net}}$ is:
$$
    T_{\text{net}}(t) = J \frac{d\omega(t)}{dt} = T_m(t) - r \omega(t) - T_d(t),
    $$

    where:
        - $J$: moment of inertia,
        - $r$: damping coefficient,
        - $T_d(t)$: disturbance torque.

## Circuit Equation in the s-Domain
- The Laplace transform of the DC motor circuit is given by:
$$
    L_a s I_a(s) + R_a I_a(s) + k_f \Omega(s) = V_a(s),
    $$

    where:
        - $I_a(s)$, $\Omega(s)$, and $V_a(s)$ are the Laplace transforms of $i_a(t)$, $\omega(t)$, and $V_a(t)$, respectively.

- Using the relation between $T_m(t)$ and $i_a(t)$:
$$
    \frac{1}{k_m} \left( s L_a + R_a \right) T_m(s) + k_f \Omega(s) = V_a(s).
    $$

## Net Torque Equation in the s-Domain
- The Laplace transform of the net torque (with $T_d = 0$) is:
$$
    T_m(s) = (J s^2 + r s) \Theta(s) = (J s + r) \Omega(s).
    $$

## Final Combined Equation
- By joining the equations above:
$$
    (s L_a + R_a)(J s + r) \Omega(s) + k_f \Omega(s) = k_m V_a(s).
    $$


## Transfer Function
- The transfer function of the DC motor is given by:
$$
    H(s) = \frac{\Omega(s)}{V_a(s)} = \frac{k_m}{L_a J s^2 + [R_a J + L_a r] s + [R_a r + k_m k_f]}.
    $$

## Poles of the System
- The poles of the system are given by the roots of the denominator. Using the quadratic formula, the poles are:
$$
    s_{1,2} = \frac{-[R_a J + L_a r] \pm \sqrt{[R_a J + L_a r]^2 - 4 L_a J [R_a r + k_m k_f]}}{2 L_a J}.
    $$

## Question
- **What are the relations between the parameters of the DC motor for the system to be stable?**
    - For stability, all poles must have negative real parts, meaning the real parts of $s_{1,2}$ must be less than 0.

![[Pasted image 20250114142240.png]]

# In closing

in z-domain(discrete) poles should be within the unit circle
s-domain(continuous) here the poles should be negative. 
this is the main different between the s- and z-domain

# Practice Questions

## Topics for the Final Exam
1. Prove the following properties of the Laplace Transform:
    - Linearity
    - Time Shifting
    - Frequency Shifting

2. Consider the following system:
$$
    4 \frac{d^2 y(t)}{dt^2} + 3 \frac{dy(t)}{dt} + 2y(t) = \frac{dx(t)}{dt} + 2x(t),
    $$

    where:
        - $x(t)$ is the input,
        - $y(t)$ is the output,
        - Initial conditions: 
            - $x(0)$, $y(0)$, and $\frac{dy(t)}{dt} \big|_{t=0} = 0$.

## Tasks
- Find the transfer function of the system, $H(s) = \frac{Y(s)}{X(s)}$.
- Find the poles and zeroes of the system.
- Determine if the system is stable. Justify your answer.
