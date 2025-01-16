---
tags:
  - Marinus
  - Lectures
  - LLM
  - _FirstPass
Created: 2025-01-07
---
think about the steps for solving the questions. 
link the theory to the practical
wow... insightful

bring A4 summary sheet
no calcs or other devices allowed 

The most math well do is like sqrt 25
so its more about the theory and the formulas and how you use them instead of the math

Laplace transform are `bonus` questions
# Recap

## Recap: Discrete Fourier Transform

### Discrete Fourier Transform (DFT)
The Discrete Fourier Transform (DFT) of a sequence $x[n]$ is defined as:
$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j(2\pi/N)kn}, \quad \text{for } k = 0, \dots, N-1
$$

#### Key Points:
- **Purpose of DFT**: Transforms $N$ samples from the time domain into $N$ samples in the frequency domain.
- **Convolution Property**:
  - In the time domain: $y[n] = h[n] * x[n]$
  - In the frequency domain: $Y[k] = H[k] X[k]$

---

## Recap: Signal Representation

### L-length Signal Representation
An $L$-length signal $x[n] = \{x[0], x[1], \dots, x[L-1]\}$ can be represented as:
$$
x[n] = \sum_{k=0}^{L-1} x[k] \delta[n - k]
$$
where $\delta[n]$ is the unit impulse.
- we can represent this finite discrete signal as a sum
- z trans to represent this expression into the set domain make it easier?

# z-transform

### Definition of z-transform 
The z-transform of an $L$-length signal $x[n]$ is defined as: $$ X(z) = \sum_{k=0}^{L-1} x[k] z^{-k} $$ This can also be written as: $$ X(z) = \sum_{k=0}^{L-1} x[k] (z^{-1})^k $$ where $z$ is a complex number. 
### Interpretation: 
- The z-transform represents a signal $x[n]$ as a polynomial $X(z)$ of degree $L-1$ in the variable $z^{-1}$. 
- It is a helpful tool for analysing discrete signals and systems.
### Example of z-transform Consider the signal: 
$$ x[n] = \delta[n - n_0] $$ The z-transform of $x[n]$ is: $$ X(z) = z^{-n_0} $$
![[Pasted image 20250107131604.png]]
The z-transform for $x[n]$ is:
$$
X(z) = 2 + 4z^{-1} + 6z^{-2} + 4z^{-3} + 2z^{-4}
$$
- here we can analyse interesting signals and systems and extract properties from those signals
## z-transform of FIR Filter
- z-transform of a discrete system
### Impulse Response
A FIR (Finite Impulse Response) filter is completely characterized by its impulse response:
$$
h[n] = \sum_{k=0}^{M} b_k \delta[n - k]
$$

### System Function
The system function is obtained by taking the z-transform of the impulse response:
$$
H(z) = \sum_{k=0}^{M} b_k z^{-k} = \sum_{k=0}^{M} h[k] z^{-k}
$$

- The system function $H(z)$ also completely characterizes the filter.

- A filter can also be described as a system

## Example: Unit Delay

### Unit Delay Filter
The unit delay filter is described by the difference equation:
$$
y[n] = x[n-1] = \delta[n-1] * x[n] = h[n] * x[n]
$$

### Impulse Response and System Representation
The impulse response function $h[n]$ can be represented as:
$$
H(z) = z^{-1}
$$

For the input signal $x[n]$, the z-transform is:
$$
X(z) = \sum_k x[k] z^{-k}
$$

The output signal $y[n]$ is represented as:
$$
Y(z) = \sum_k x[k] z^{-(k+1)} = z^{-1} \sum_k x[k] z^{-k}
$$
- here we have the z-transform of x
Hence:
$$
Y(z) = H(z) X(z)
$$
- apparently one of the most important results of this lecture

### Convolution in Time and z-Domain
- **In the time domain**: Convolution is represented as:
  $$
  y[n] = h[n] * x[n]
  $$

- **In the z-domain**: Convolution in the time domain becomes multiplication:
  $$
  Y[z] = H[z] X[z]
  $$

## Block Diagrams and $z^{-1}$ Notation

### System Representation
The system is described by the equation:
$$
y[n] = h[n] * x[n] = \sum_k h[k] x[n-k]
$$
Expanding:
$$
y[n] = x[n] - 2x[n-1] + 3x[n-2]
$$

### Block Diagram
- The block diagram illustrates the system structure using $z^{-1}$ blocks to represent unit delays.
- ![[Pasted image 20250107132305.png]]
- Operations:
    - $x[n]$ passes through the first unit delay ($z^{-1}$) to produce $x[n-1]$.
    - Coefficients such as $-2$ and $3$ are applied after delays.
    - Outputs are summed to form $y[n]$.

### z-Domain Representation
A unit delay is represented as multiplication by $z^{-1}$.

The z-domain equation for the system:
$$
Y(z) = \sum_k h[k] (z^{-k} X(z))
$$
Simplifying:
$$
Y(z) = \left( \sum_k h[k] z^{-k} \right) X(z)
$$
Therefore:
$$
Y(z) = H(z) X(z)
$$

## Cascaded LTI Systems

### Key Points
- **LTI Cascades**: Multiple Linear Time-Invariant (LTI) systems can be connected in series:
  - The output of one system becomes the input for the next system.
  - The order of systems does not affect the overall result.

### System Representations
1. **Cascade of Two Systems**:
   - First system: $H_1(z)$
   - Second system: $H_2(z)$
   - Output: 
     $$
     Y(z) = H_2(z) \cdot \left(H_1(z) \cdot X(z)\right)
     $$

2. **Equivalent Single System**:
   - The cascaded system is equivalent to a single LTI system with:
     $$
     H_{\text{eq}}(z) = H_1(z) \cdot H_2(z)
     $$
   - Output:
     $$
     Y(z) = H_{\text{eq}}(z) \cdot X(z)
     $$

3. **Order Independence**:
   - Swapping the order of systems ($H_1(z)$ and $H_2(z)$) does not change the result:
     $$
     Y(z) = H_1(z) \cdot \left(H_2(z) \cdot X(z)\right)
     $$
![[Pasted image 20250107132614.png]]

## Example: Cascade of Two LTI Systems

### Problem Statement
Consider the cascade of two LTI systems:
1. First system:
   $$
   w[n] = 3x[n] - x[n-1]
   $$
2. Second system:
   $$
   y[n] = 2w[n] - w[n-1]
   $$
### Objective
Find the equivalent LTI system in the time domain.

### Solution: Equivalent System
1. Substituting $w[n]$ into $y[n]$:
   $$
   y[n] = 2w[n] - w[n-1]
   $$
   Expanding:
   $$
   y[n] = 2(3x[n] - x[n-1]) - (3x[n-1] - x[n-2])
   $$

2. Simplify:
   $$
   y[n] = 6x[n] - 5x[n-1] + x[n-2]
   $$

### Impulse Response
The impulse response $h[n]$ of the equivalent system is:
$$
h[n] = 6\delta[n] - 5\delta[n-1] + \delta[n-2]
$$

## Example: Cascade of Two LTI Systems (Using z-transform)

### Problem Statement
Consider the cascade of two LTI systems:
1. First system:
   $$
   w[n] = 3x[n] - x[n-1]
   $$
2. Second system:
   $$
   y[n] = 2w[n] - w[n-1]
   $$

### Objective
Find the equivalent LTI system using the z-transform.

### Solution: Using z-transform
1. Transfer functions of the two systems:
   - For the first system:
     $$
     H_1(z) = 3 - z^{-1}
     $$
   - For the second system:
     $$
     H_2(z) = 2 - z^{-1}
     $$

2. Equivalent transfer function:
   $$
   H(z) = H_1(z) \cdot H_2(z)
   $$
   Substituting:
   $$
   H(z) = (3 - z^{-1})(2 - z^{-1})
   $$

3. Simplify:
   $$
   H(z) = 6 - 5z^{-1} + z^{-2}
   $$

# Domains

![[Pasted image 20250107132935.png]]

## Relationship Between Time, Frequency, and z-Domain

### FIR Filter Representation in Three Domains
An FIR filter can be fully described in three domains:

1. **Time Domain**:
   $$
   h[n] = \sum_k b_k \delta[n-k]
   $$

2. **Frequency Domain**:
   $$
   H(e^{j\omega}) = \sum_k h[n] e^{-j\omega k}
   $$
   Equivalent to evaluating $H(z)$ at $z = e^{j\omega}$:
   $$
   H(e^{j\omega}) = H(z)|_{z = e^{j\omega}}
   $$

3. **z-Domain**:
   $$
   H(z) = \sum_k h[n] z^{-k}
   $$

### Summary
- Each domain provides a complete description of the FIR filter.
- Relationships:
   - Time domain $\leftrightarrow$ Frequency domain via $H(e^{j\omega})$.
   - Time domain $\leftrightarrow$ z-domain via $H(z)$.
   - Frequency domain $\leftrightarrow$ z-domain through substitution $z = e^{j\omega}$.
- Remember that z is a complex variable 
- something you do with z is polar coordinates 
- what is the length?
	- amplitude? 
	- omega... 
	- complex number with length one and radius omega
	- in frequency domain
## Comment: Advantage of z-transform

### Key Insight
- The z-transform allows us to **factor polynomials**.
- The **roots** of the polynomial, where $H(z) = 0$, provide critical information about the filter's characteristics.

## Factoring z-transforms

### Polynomial Representation
The z-transform can be factored to analyze the system:
$$
H(z) = 1 - 2z^{-1} + z^{-2} = (1 - z^{-1})^2
$$
- coefficients: 1, -2, 1
- we now have a cascade filter that is the same
- two filters cascade 
- with inputs at n and n-1
- root of filter is at 1
	- output is going to be y offset = h set times x set
	- root at 1
	- result of y is 0
	- interpretation of z in frequency domain = $e^{xj\omega}$
### Key Observations
- The filter $h[n] = \{1, -2, 1\}$ is equivalent to applying the **first-difference filter** $h_1[n] = \{1, -1\}$ twice.
- The filter is **zero** when $z = 1$.

## Roots of z-transforms

### General Form 
The z-transform of a filter can be represented in factored form:
$$
H(z) = G \prod_{k=1}^{M} (1 - z_k z^{-1}) = G \prod_{k=1}^{M} \left(\frac{z - z_k}{z}\right)
$$
where $G$ is a constant.
- generally G in this course is 0
- L-1 roots in the system
### Key Points
- The filter **eliminates inputs** for which $z = z_k$.
- The filter is defined, up to the constant $G$, by the inputs it eliminates:
  - $z_k$ are called the **zeros** of the system function.
  - A FIR filter of length $L$ has $M = L - 1$ roots.

## Zeros of the System Function

### System Function
The system function is represented as:
$$
H(z) = \sum_k b_k z^{-k} = \frac{z - z_0}{z}
$$
- only one zero at z = 0
### Key Points
- The filter has a single zero at $z_0$.
- Applying the filter to the signal $x[n] = z_0^n$, where $z_0 \in \mathbb{R}$, results in:

### Derivation
1. Output signal:
   $$
   y[n] = \sum_k b_k x[n-k] = \sum_k b_k z_0^{n-k}
   $$
2. Factorizing:
   $$
   y[n] = \left(\sum_k b_k z_0^{-k}\right) z_0^n
   $$
3. Substituting $H(z_0) = 0$:
   $$
   y[n] = H(z_0) z_0^n = 0
   $$

### Conclusion
The filter eliminates the input signal $x[n] = z_0^n$ where $z_0$ corresponds to the zero of the system function.

## Example: Roots of z-transforms

### System Function
The given system function is:
$$
H(z) = 1 - z^{-1} + z^{-2} = \frac{1}{z^2}(z^2 - z + 1)
$$

### Finding the Zeros
Using the quadratic formula:
$$
z_k = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
where $a = 1$, $b = -1$, and $c = 1$, the zeros are calculated as:
1. Substitute values:
   $$
   z_k = \frac{1 \pm \sqrt{(-1)^2 - 4 \cdot 1 \cdot 1}}{2 \cdot 1}
   $$
2. Simplify:
   $$
   z_k = \frac{1 \pm \sqrt{1 - 4}}{2} = \frac{1 \pm \sqrt{-3}}{2}
   $$
3. Express in complex form:
   $$
   z_k = \frac{1}{2} \pm \frac{j\sqrt{3}}{2}
   $$
   which corresponds to:
   $$
   z_k = e^{\pm j\pi/3}
   $$
conjugate with complex number 
- a sinusoid signal
- with this filter we will cancel any sinusoid associated with this frequency
### Factored Form
The system function can now be expressed as:
$$
H(z) = \left(1 - e^{-j\pi/3}z^{-1}\right)\left(1 - e^{j\pi/3}z^{-1}\right)
$$
separate into H1 and H2
so its H=H1 * H2

## Frequency Response and z-transform
![[Pasted image 20250107140325.png]]
### Zeros Plot
- The zeros of $H(z) = 1 - z^{-1} + z^{-2}$ are represented by **red circles** on the plot.
- Key observations:
  - $z = e^{j\omega}$ defines a **unit circle** in the complex plane.
  - The **frequency response** $H(e^{j\omega})$ is a special case of the z-transform, evaluated on the unit circle.
### Terminology
- The plot shown is called a **zeros plot**.
### Remark
- The zeros indicate which frequencies are **eliminated** from the signal.
- for fir filter we can guarantee that those poles are 0

## Frequency Response and System Function

### Impulse Response
The impulse response $h[n]$ is given as:
$$
h[n] = \delta[n] - \delta[n-1] + \delta[n-2]
$$

### Frequency Response
The frequency response $H(e^{j\omega})$ is:
$$
H(e^{j\omega}) = e^{-j\omega}(2\cos(\omega) - 1)
$$

### z-Domain Representation
The system function $H(z)$ is:
$$
H(z) = (1 - e^{-j\pi/3}z^{-1})(1 - e^{j\pi/3}z^{-1})
$$

### Remark
- $H(e^{j\omega})$ provides the **complex value** of $H(z)$ along the unit circle in the z-plane.

## Example: 11-Point Running Sum
- this is a low-pass filter

### Impulse Response
The impulse response $h[n]$ for the 11-point running sum is:
$$
h[n] = \sum_{k=0}^{10} \delta[n-k]
$$

### Frequency Response
The frequency response $H(e^{j\omega})$ is:
$$
H(e^{j\omega}) = e^{-j5.5\omega} \cdot \frac{\sin(5.5\omega)}{\sin(\omega/2)}
$$
We are eliminating 11 frequencies
### z-Domain Representation
The z-domain representation $H(z)$ is:
$$
H(z) = \sum_{k=0}^{10} z^{-k} = \prod_{k=1}^{10} \left(1 - e^{-j2\pi k/11}z^{-1}\right)
$$
here can see the corresponding 11 zeros in the plot 
![[Pasted image 20250107141239.png]]
### Visualization
- **Zeros Plot**:
  - The zeros are equally spaced around the unit circle.
- **Magnitude Response**:
  - The magnitude plot shows peaks and nulls, with a central lobe around $\omega = 0$.

### Key Insight
- The system is designed to sum 11 consecutive points and introduces specific frequency nulls based on its zero locations.

- If something is difficult in a domain, perhaps move it to another domain and the interpretation can be much easier

There are some good visual examples here
[[lec7-main4.pdf#page=44&offset=28.346,255.118|lec7-main4, Zeros of the system function]]

## Bandpass Filter Design
### Using the z-transform for Filter Design
- **Starting Point**:
  - The 11-point running sum is a **lowpass filter**:
    $$
    H(z) = \sum_{k=0}^{10} z^{-k}
    $$
- **Creating a Bandpass Filter**:
  - Shift the phase (i.e., `rotate the zeros` on the unit circle) to create a bandpass filter.

### Modified System Function
The modified filter has a system function:
$$
H(z) = \sum_{k=0}^{10} e^{j4\pi k/11} z^{-k}
$$
We are boosting the exponent frequency 4k/11 
and we are now removing the dc component.
### Observations
1. **Zeros Plot**:
   - Zeros are rotated to focus energy on a specific frequency band.
2. **Magnitude Response**:
   - The frequency response shifts to create a peak around the desired passband.

### Key Challenges
- The modified filter has **complex-valued coefficients**:
  - This may introduce issues in systems requiring **real-valued input and output**.

## Bandpass Filter: Taking the Real Part of the Rotation

### System Function with Real Part
The system function is modified by taking the real part of the rotation:
$$
H(z) = \sum_{k=0}^{10} \Re\{e^{j4\pi k/11}\}z^{-k}
$$
This simplifies to:
$$
H(z) = \sum_{k=0}^{10} \cos(4\pi k/11) z^{-k}
$$
Further expressed as:
$$
H(z) = \sum_{k=0}^{10} \left( \frac{1}{2} e^{j4\pi k/11} + \frac{1}{2} e^{-j4\pi k/11} \right) z^{-k}
$$
Which is the average of rotating **clockwise** and **anti-clockwise**.

The system function $H(z)$, after taking the real part of the rotation, can be expressed as: $$ H(z) = \left( \sum_{k=0}^{10} \frac{1}{2} e^{j4\pi k/11} z^{-k} \right) + \left( \sum_{k=0}^{10} \frac{1}{2} e^{-j4\pi k/11} z^{-k} \right) $$ This representation shows the averaging of the clockwise and anti-clockwise rotations in the z-domain.

---

## Bandpass Filter: Observations

### System Behaviour
1. **Zeros Plot**:
   - The roots are symmetrically distributed with an emphasis on real values.
   - The root $z_k = 1$ appears **twice**.

2. **Magnitude Response**:
   - The peaks in the frequency response are slightly **off-target**.

### Final System Function
$$
H(z) = \sum_{k=0}^{10} \cos(4\pi k/11) z^{-k}
$$

## Poles of z-transforms

### General Form
The z-transform of a filter can be written as:
$$
H(z) = G \prod_{k=1}^{M} (1 - z_k z^{-1}) = G \prod_{k=1}^{M} \left(\frac{z - z_k}{z}\right)
$$
where $G$ is a constant.

### Key Points
1. **Zeros of the System Function**:
   - $z_k$ are the **zeros** of the system function.
   - For each zero $z_k$, $H(z_k) = 0$.

2. **Poles of the System Function**:
   - As $z \to 0$, $H(z) \to \infty$.
   - Points where $H(z) = \infty$ are called the **poles** of $H(z)$.

3. **Poles at $z = 0$**:
   - FIR filters of order $M$ have $M$ poles located at $z = 0$.

### Summary
- Zeros describe where the system cancels inputs.
- Poles indicate where the system amplifies inputs to infinity.

# Recall: IIR Filters

### Definition
An IIR (Infinite Impulse Response) filter is a **recursive filter**:
- The output depends on:
  - **Current and previous inputs** (feed-forward terms).
  - **Previous outputs** (feedback terms).

### Difference Equation
The filter is characterized by the following equation:
$$
y[n] = \sum_{k=0}^{N} b_k x[n-k] - \sum_{k=1}^{M} a_k y[n-k]
$$

### Analysis Using z-transform
- The z-transform simplifies the analysis of IIR filters by representing them as a **rational function**.
- **Components**:
  - The **numerator polynomial** corresponds to the feed-forward coefficients $b_k$.
  - The **denominator polynomial** corresponds to the feedback coefficients $a_k$.

### Convolution in Time and z-Domain
In the time domain:
$$
y[n] = x[n] * h[n]
$$
In the z-domain:
$$
Y(z) = X(z) H(z)
$$
## Example: First-Order IIR Filter

### Difference Equation
Consider the first-order IIR filter described by:
$$
y[n] = a_1 y[n-1] + b_0 x[n] + b_1 x[n-1]
$$

### z-Domain Representation
Applying the z-transform:
$$
Y(z) = a_1 z^{-1} Y(z) + b_0 X(z) + b_1 z^{-1} X(z)
$$

### Grouping Terms
Rearrange to group the output ($Y(z)$) and input ($X(z)$) terms:
$$
Y(z)(1 - a_1 z^{-1}) = X(z)(b_0 + b_1 z^{-1})
$$

### System Function
The system function $H(z)$ is:
$$
H(z) = \frac{Y(z)}{X(z)} = \frac{b_0 + b_1 z^{-1}}{1 - a_1 z^{-1}}
$$
## Generalized System Function for IIR Filters

### System Function Representation
The system function for an IIR filter with $N$ feed-forward coefficients and $M$ feedback coefficients is:
$$
H(z) = \frac{\sum_{k=0}^{N} b_k z^{-k}}{1 - \sum_{k=1}^{M} a_k z^{-k}} = \frac{B(z)}{A(z)}
$$

### Cascade Interpretation
The system function can also be written as:
$$
H(z) = B(z) \cdot \left(\frac{1}{A(z)}\right)
$$

### Key Insight
- The last expression explicitly shows the **cascade** of the feed-forward component $B(z)$ and the feedback component $A(z)$.

## Example 1: Poles and Zeros of a First-Order IIR Filter

### System Function
The system function for the first-order IIR filter is:
$$
H(z) = \frac{Y(z)}{X(z)} = \frac{b_0 + b_1 z^{-1}}{1 - a_1 z^{-1}}
$$

### Zeros of the System Function
- The zeros are the roots of the numerator polynomial $B(z) = b_0 + b_1 z^{-1}$:
  $$
  z_0 = -\frac{b_0}{b_1}
  $$
- At $z = z_0$, the system function satisfies:
  $$
  H(z) = 0
  $$

### Poles of the System Function
- The poles are the roots of the denominator polynomial $A(z) = 1 - a_1 z^{-1}$:
  $$
  z_1 = \frac{1}{a_1}
  $$
- At $z = z_1$, the system function satisfies:
  $$
  H(z) \to \infty
  $$

We want a bounded response for a filter!
## Example 2: Analyzing a First-Order IIR Filter

### Recap: First-Order IIR Filter 
The difference equation for the filter is:
$$
y[n] = a_1 y[n-1] + b_0 x[n]
$$

The impulse response is:
$$
h[n] = b_0 a_1^n u[n]
$$
if a1 is between 0 and 1 it is bounded. at 1 it oscillates. above 1 its unbounded
### System Function
The z-domain representation of the system function is:
$$
H(z) = \frac{Y(z)}{X(z)} = \frac{b_0}{1 - a_1 z^{-1}} = b_0 z \left(\frac{1}{z - a_1}\right)
$$
Rather analyse this than the previous equation. 
if a1 < 1 and a1 > 0
a1 controls if the system blows up or stays controlled. 
bound a1.
### Zeros of the System Function
- The zeros are the roots of the numerator polynomial $B(z) = b_0 z$:
  $$
  z_0 = 0
  $$
- At $z = z_0$, the system function satisfies:
  $$
  H(z) = 0
  $$

### Poles of the System Function
- The poles are the roots of the denominator polynomial $A(z) = z - a_1$:
  $$
  z_1 = a_1
  $$
- At $z = z_1$, the system function satisfies:
  $$
  H(z) \to \infty
  $$
## Stability of IIR Filters

### Stability Criteria
- Recall:
  - If $|a_1| < 1$, the filter is **stable**, which is equivalent to $|z_1| < 1$.
  - Conversely, if $|a_1| > 1$, the filter is **unstable**, which is equivalent to  (poles) $|z_1| > 1$.

### Pole Location and Stability
- The stability of the filter is determined by the location of the **poles** in the z-plane:
  - **Stable**: Poles are **inside the unit circle** in the z-plane.
  - **Unstable**: Poles are **outside the unit circle**.

### Generalization
- For any IIR filter, stability is directly related to pole locations:
  - **An IIR filter is stable if and only if all poles are inside the unit circle in the z-plane.**
by just looking at the poles of the system. 
## Example 2: First-Order IIR Filter in the Frequency Domain

### System Function
The system function for the first-order IIR filter is:
$$
H(z) = \frac{Y(z)}{X(z)} = \frac{b_0}{1 - a_1 z^{-1}}
$$

### Frequency Response
When $a_1 < 1$, the frequency response of the filter is:
$$
H(e^{j\omega}) = \frac{b_0}{1 - a_1 e^{-j\omega}}
$$

### Output for a Sinusoidal Input
Consider an input signal:
$$
x[n] = e^{j\omega_0 n}
$$
The output signal is:
$$
y[n] = H(e^{j\omega_0}) e^{j\omega_0 n}
$$
Substitute the frequency response:
$$
y[n] = \frac{b_0}{1 - a_1 e^{-j\omega_0}} e^{j\omega_0 n}
$$