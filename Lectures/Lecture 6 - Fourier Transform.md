---
tags:
  - Marinus
  - _FirstPass
  - Lectures
  - LLM
Date: 2024-12-17
---
The Discrete Fourier Transform (DFT) converts a sequence $x[n]$ from the time domain to the frequency domain.  
- Formula: $$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}kn}$$
- ($k$): Frequency index  
- ($N$): Number of samples in $x[n]$.
- ($X[k]$): Represents the frequency components of $x[n]$.

## DFT and Time/Frequency Domain

The Discrete Fourier Transform (DFT) converts time domain samples into frequency domain samples.  
- Each extra sample $x[n]$ informs one additional frequency component $X[k]$.  
- $X[k]$: Complex terms consisting of amplitude and phase.  
- $x[n]$: Signal in the time domain.  
- $X[k]$: Representation in the frequency domain.  
- Frequency mapping:  $$\hat{\omega} = \frac{2\pi k}{N}, \quad \hat{\omega} \in [0, 2\pi).$$
## Example - Short-length DFT ($X[0]$)

Suppose we have a periodic signal $x[n] = \{1, 1, 0\}$. Let us compute the DFT for $x[n]$:

- Formula:$$X[0] = \sum_{n=0}^{3-1} x[n] \, e^{-j \frac{2\pi}{3} 0 \cdot n}$$
- Substitution:$$X[0] = x[0] e^{-j 0} + x[1] e^{-j 0} + x[2] e^{-j 0}$$
- Simplification:$$X[0] = 1 \cdot 1 + 1 \cdot 1 + 0 \cdot 1 = 2$$![[Pasted image 20241217132755.png]]
> Here we found the DC component, the highest or most prominent frequency
---

## Example - Short-length DFT ($X[1]$)

Suppose we have a periodic signal $x[n] = \{1, 1, 0\}$. Let us compute the DFT for $x[n]$:

- Formula:$$X[1] = \sum_{n=0}^{3-1} x[n] \, e^{-j \frac{2\pi}{3} 1 \cdot n}$$
- Substitution:$$X[1] = x[0] e^{-j 0} + x[1] e^{-j \frac{2\pi}{3} 1} + x[2] e^{-j \frac{2\pi}{3} 2}$$
- Simplification:
  $$\begin{align*}
  X[1] &= 1 \cdot 1 + 1 \cdot e^{-j \frac{2\pi}{3}} + 0 \cdot e^{-j \frac{4\pi}{3}} \\
  &= 1 + \left( -\tfrac{1}{2} - j \tfrac{\sqrt{3}}{2} \right) + 0 \\
  &= \left( 1 - \tfrac{1}{2} \right) - j \tfrac{\sqrt{3}}{2} \\
  &= \tfrac{1}{2} - j \tfrac{\sqrt{3}}{2}
  \end{align*}$$
![[Pasted image 20241217132812.png]]
---

## Example - Short-length DFT ($X[2]$)

Suppose we have a periodic signal $x[n] = \{1, 1, 0\}$. Let us compute the DFT for $x[n]$:

- Formula:$$X[2] = \sum_{n=0}^{3-1} x[n] \, e^{-j \frac{2\pi}{3} 2 \cdot n}$$
- Substitution:$$X[2] = x[0] e^{-j 0} + x[1] e^{-j \frac{4\pi}{3}} + x[2] e^{-j \frac{8\pi}{3}}$$
- Simplification:
  $$\begin{align*}
  X[2] &= 1 \cdot 1 + 1 \cdot e^{-j \frac{4\pi}{3}} + 0 \cdot e^{-j \frac{8\pi}{3}} \\
  &= 1 + \left( -\tfrac{1}{2} + j \tfrac{\sqrt{3}}{2} \right) + 0 \\
  &= \left( 1 - \tfrac{1}{2} \right) + j \tfrac{\sqrt{3}}{2} \\
  &= \tfrac{1}{2} + j \tfrac{\sqrt{3}}{2}
  \end{align*}$$
![[Pasted image 20241217132831.png]]
- Here we dont have any negative frequencies.
- i dont know why i struggle so much to follow these lectures

## Time and Frequency

- The DFT $X[k]$ represents input $x[n]$ in the frequency domain.  
- The original input $x[n]$ can be recovered by sampling these frequencies.

## Inverse Discrete Fourier Transform (IDFT)

The inverse DFT of sequence $X[k]$ is:  
- Formula: $$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j \frac{2\pi}{N} k n}$$  
- Range: $k = 0, \dots, N - 1$
- Since $X[k]$ is periodic, the reconstructed $x[n]$ is also periodic

## Example - Short-length DFT ($x[0]$)

Consider the sequence $X[k] = \{2, e^{-j\pi/3}, e^{j\pi/3} \}$. Let us compute the IDFT for $X[k]$:  

- Formula:$$x[0] = \frac{1}{3} \sum_{k=0}^{3-1} X[k] e^{j \frac{2\pi}{3} 0 \cdot k}$$
- Substitution:$$x[0] = \frac{1}{3} \left( X[0] e^{j (2\pi/3) 0 \cdot 0} + X[1] e^{j (2\pi/3) 0 \cdot 1} + X[2] e^{j (2\pi/3) 0 \cdot 2} \right)$$
- Simplification:$$x[0] = \frac{1}{3} \left( 2 + e^{-j\pi/3} + e^{j\pi/3} \right)$$  $$x[0] = \frac{1}{3} \left( 2 + 2 \cos(\pi/3) \right) = 1$$
![[Pasted image 20241217133249.png]]
---
## Example - Short-length DFT ($x[1]$)

Consider the sequence $X[k] = \{2, e^{-j\pi/3}, e^{j\pi/3} \}$. Let us compute the IDFT for $X[k]$:  

- Formula:$$x[1] = \frac{1}{3} \sum_{k=0}^{3-1} X[k] e^{j \frac{2\pi}{3} 1 \cdot k}$$
- Substitution:$$x[1] = \frac{1}{3} \left( X[0] e^{j (2\pi/3) 1 \cdot 0} + X[1] e^{j (2\pi/3) 1 \cdot 1} + X[2] e^{j (2\pi/3) 1 \cdot 2} \right)$$

- Simplification:$$x[1] = \frac{1}{3} \left( 2 + e^{-j\pi/3} e^{j 2\pi/3} + e^{j\pi/3} e^{j 4\pi/3} \right)$$
  $$x[1] = \frac{1}{3} \left( 2 + (\cos(\pi/3) + j \sin(\pi/3)) + (\cos(5\pi/3) + j \sin(5\pi/3)) \right)$$  $$x[1] = \frac{1}{3} \left( 2 + 0.5 + j \frac{\sqrt{3}}{4} + 0.5 - j \frac{\sqrt{3}}{4} \right) = 1$$
  ![[Pasted image 20241217133513.png]]

---
## Example - Short-length DFT ($x[2]$)

Consider the sequence $X[k] = \{2, e^{-j\pi/3}, e^{j\pi/3} \}$. Let us compute the IDFT for $X[k]$:  

- Formula:$$x[2] = \frac{1}{3} \sum_{k=0}^{3-1} X[k] e^{j \frac{2\pi}{3} 2 \cdot k}$$
- Substitution:$$x[2] = \frac{1}{3} \left( X[0] e^{j (2\pi/3) 2 \cdot 0} + X[1] e^{j (2\pi/3) 2 \cdot 1} + X[2] e^{j (2\pi/3) 2 \cdot 2} \right)$$
- Simplification:$$x[2] = \frac{1}{3} \left( 2 + e^{-j\pi/3} e^{j 4\pi/3} + e^{j\pi/3} e^{j 8\pi/3} \right)$$$$x[2] = \frac{1}{3} \left( 2 + (\cos(\pi) + j \sin(\pi)) + (\cos(3\pi) + j \sin(3\pi)) \right)$$$$x[2] = \frac{1}{3} \left( 2 - 1 + 0 - 1 + 0 \right) = 0$$![[Pasted image 20241217133615.png]]
---
## DFT Frequencies

The sequence $X[k]$ represents the (discrete) spectrum of $x[n]$:  

- The values represent one period in samples:  
	- The DFT only makes use of **non-negative indices**.  
	- The values represent frequencies $0 \leq \hat{\omega} < 2\pi$.  
- Remaining frequency components are aliases.  
- The principal frequency interval is $(-\pi < \hat{\omega} \leq \pi)$:  
	- This represents $x[n] = 2 + 2 \cos\left( \frac{2\pi}{3}n - \frac{\pi}{3} \right)$.
![[Pasted image 20241217133744.png]]
---
## Time and Frequency

- DFT $X[k]$ (in blue) represents the input $x[n]$ (in red) as frequencies.  
- DFT is periodic.  
- DFT technically models a periodic signal $x[n]$:  
	- We know where to end the signal through the number of components in $X[k]$.
![[Pasted image 20241217133834.png]]
---
## Time Delay

A **time delay** $\delta[n - n_0]$ postpones a signal:  
- For periodic signals, this time delay is equivalent to a phase shift $e^{-j \hat{\omega} n_0}$.  
- For the DFT, the result of applying this phase shift may be unexpected.
![[Pasted image 20241217133929.png]]
---
## Applying Phase Shift $e^{-j \hat{\omega} n_0}$ to the DFT

- Applying a phase shift does not change the length of the DFT:  
	- DFT turns $N$ input samples into $N$ frequency components.  

- Instead, **the signal is interpreted as being periodic**.  
- The signal is 'wrapped around' due to the circular shift.  
- This is a problem: the goal was to delay the signal.
![[Pasted image 20241217134023.png]]
---
## Zero Padding

- The intended time delay adds four zeroes to the front.  
- These zeroes should already be in the signal $x[n]$.  
- We have to pad the original signal with zeroes.  
- The delay now coincides with a phase shift:  
	- *This zero padding accounts for periodicity.*
![[Pasted image 20241217134121.png]]
---
# Fast Fourier Transform

## Computing Fourier Transform

The DFT is calculated by:  
- Formula:$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n} \quad \text{for } k = 0, \dots, N-1$$
- Alternatively, in matrix form:  $$
  \begin{bmatrix}
  X[0] \\
  X[1] \\
  X[2] \\
  \vdots \\
  X[N-1]
  \end{bmatrix}
  =
  \begin{bmatrix}
  1 & 1 & 1 & \dots & 1 \\
  1 & e^{-j\frac{2\pi}{N}} & e^{-j\frac{4\pi}{N}} & \dots & e^{-j\frac{2(N-1)\pi}{N}} \\
  1 & e^{-j\frac{4\pi}{N}} & e^{-j\frac{8\pi}{N}} & \dots & e^{-j\frac{4(N-1)\pi}{N}} \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  1 & e^{-j\frac{2(N-1)\pi}{N}} & e^{-j\frac{4(N-1)\pi}{N}} & \dots & e^{-j\frac{(N-1)(N-1)\pi}{N}}
  \end{bmatrix}
  \begin{bmatrix}
  x[0] \\
  x[1] \\
  x[2] \\
  \vdots \\
  x[N-1]
  \end{bmatrix}
  $$
- first row extracts DC component
- **Time complexity** of naive implementation is $O(N^2)$. Can we improve on this?
- more intelligent ways than simply inversing these
## Deriving Fast Fourier Transform

We assume that $N$ is a power of 2.  
- Formula:$$X[k] = \text{DFT}_N\{x[n]\} = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n}$$
- Expanding the summation:$$X[k] = x[0] e^{-j 0} + x[1] e^{-j \frac{2\pi}{N} k} + x[2] e^{-j \frac{4\pi}{N} k} + \dots + x[N-1] e^{-j \frac{2(N-1)\pi}{N} k}$$
- Splitting the sum into even and odd terms:$$
  X[k] = \sum_{m=0}^{N/2-1} x[2m] e^{-j \frac{2\pi}{N} (2m)k} + e^{-j \frac{2\pi}{N} k} \sum_{m=0}^{N/2-1} x[2m+1] e^{-j \frac{2\pi}{N} (2m)k}
  $$
- we can extract that first term for the odd terms.
  $$X[k] = e^{-j \frac{2\pi}{N} k} \sum_{m=0}^{N/2-1} x[2m+1] e^{-j \frac{2\pi}{N} (2m)k} $$
## Deriving Fast Fourier Transform (Continued)

Since $N$ is a power of 2, $M = N/2$ is also a power of 2:  
- Splitting the DFT further:$$
  X[k] = \left( \sum_{m=0}^{N/2-1} x[2m] e^{-j \frac{2\pi}{N} (2m)k} \right) + e^{-j \frac{2\pi}{N} k} \left( \sum_{m=0}^{N/2-1} x[2m+1] e^{-j \frac{2\pi}{N} (2m)k} \right)
  $$
- even + complex * odd
- Simplifying:$$
  X[k] = \text{DFT}_{N/2}\{x[0], x[2], \dots, x[N-2]\} + e^{-j \frac{2\pi}{N} k} \cdot \text{DFT}_{N/2}\{x[1], x[3], \dots, x[N-1]\}
  $$
- **Conclusion**: Generating a DFT can be split into generating two smaller DFTs.
## Deriving Fast Fourier Transform (Continued)

Generating a DFT can be split into generating two smaller DFTs:  
- Formula:$$X[k] = \text{DFT}_N\{x[n]\} = \text{DFT}_{N/2}\{x_{\text{even}}[n]\} + e^{-j \frac{2\pi}{N} k} \cdot \text{DFT}_{N/2}\{x_{\text{odd}}[n]\}$$$$X[k] = X_{\text{even}}[k] + e^{-j \frac{2\pi}{N} k} \cdot X_{\text{odd}}[k]$$
### But wait...  
- $X[k]$ consists of $N$ frequency components.  
- $X_{\text{even}}[k]$ only has $N/2$ frequency components.  
- What about $X[k]$ for $k > N/2$?  
- $X[k]$ consists of aliases of $X_{\text{even}}[k]$ and $X_{\text{odd}}[k]$.  

- Formula for $k > N/2$:$$X[k] = X_{\text{even}}[k - N/2] + e^{-j \frac{2\pi}{N} k} \cdot X_{\text{odd}}[k - N/2]$$  
![[Pasted image 20241217135700.png]]

---
## Example - Short-length DFT
![[Pasted image 20241217140950.png]]

Suppose we have a signal $x[n] = \{1, 1, 0, 0\}$:  
- Since the length is not a power of two, we pad $x[n]$ with zeros.
- $X[0] = DFT_4\{1, 1, 0, 0\}[0]$  
- $X[1] = DFT_4\{1, 1, 0, 0\}[1]$  
- $X[2] = DFT_4\{1, 1, 0, 0\}[2]$  
- $X[3] = DFT_4\{1, 1, 0, 0\}[3]$

Here we split it up into even and odds, then just kept doing that.
Suppose we have a signal $x[n] = \{1, 1, 0, 0\}$:  

- $X[0] = \left( DFT_1\{1\}[0] + e^{-j \pi 0} DFT_1\{0\}[0] \right) + e^{-j \pi 0/2} \left( DFT_1\{1\}[0] + e^{-j \pi 0} DFT_1\{0\}[0] \right)$  
- $X[1] = \left( DFT_1\{1\}[0] - e^{-j \pi 0} DFT_1\{0\}[0] \right) + e^{-j \pi 1/2} \left( DFT_1\{1\}[0] - e^{-j \pi 0} DFT_1\{0\}[0] \right)$  
- $X[2] = \left( DFT_1\{1\}[0] + e^{-j \pi 0} DFT_1\{0\}[0] \right) - e^{-j \pi 0/2} \left( DFT_1\{1\}[0] + e^{-j \pi 0} DFT_1\{0\}[0] \right)$  
- $X[3] = \left( DFT_1\{1\}[0] - e^{-j \pi 0} DFT_1\{0\}[0] \right) - e^{-j \pi 1/2} \left( DFT_1\{1\}[0] - e^{-j \pi 0} DFT_1\{0\}[0] \right)$  

Suppose we have a signal $x[n] = \{1, 1, 0, 0\}$:  

- $X[0] = (1 + 1 \cdot 0) + 1(1 + 1 \cdot 0) = 2$  
- $X[1] = (1 - 1 \cdot 0) + e^{-j \pi / 2} (1 - 1 \cdot 0) = 1 - j$  
- $X[2] = (1 + 1 \cdot 0) - 1(1 + 1 \cdot 0) = 0$  
- $X[3] = (1 - 1 \cdot 0) - e^{-j \pi / 2} (1 - 1 \cdot 0) = 1 + j$  
---
## Time Complexity

The DFT is defined as:$$DFT_N\{x[n]\} = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n}$$
- **Naive implementation** has time complexity $O(N^2)$:  
  - We sum over $N$ constant-time operations per component.  

---
$$DFT_N\{x[n]\} = DFT_{N/2}\{x_{\text{even}}[n]\} + e^{-j \frac{2\pi}{N} k} \cdot DFT_{N/2}\{x_{\text{odd}}[n]\}$$
- **Fast Fourier Transform (FFT)** has time complexity $O(N \log(N))$:  
  - Each depth level executes in constant time $O(1)$.  
  - There are at most $\log_2(N)$ levels.  
  - There are $N$ components.  

---
## Convolution

Suppose we have a filter $h[n]$ of length $N$ and want to calculate:  
- Formula:$$y[n] = h[n] * x[n] = \sum_{k=0}^{N} h[n] x[n - k] \quad (8)$$
- **Naive implementation** has time complexity $O(N^2)$.  
- **Time domain convolution** is equivalent to frequency domain multiplication:$$y[n] = IDFT\{DFT\{h[n]\} \cdot DFT\{x[n]\}\} \quad (9)$$
- **FFT** reduces time complexity to $O(N \log(N))$.  

---
### Remark  
**For large filters $h[n]$, it is faster to do convolution through the frequency domain.**

---

## Convolution

![[Pasted image 20241217141736.png]]

- **Convolution** can be performed as multiplication in the frequency domain.  

- **Zero padding** is used to avoid periodicity of the FFT:  
	- Additional padding ensures that the length is a power of 2.  
---

## Pearson Correlator (1D Representation)

A correlator is sensitive to the magnitude of the input:  

- **Solution**: Scale the input.  
- For example, through **Pearson correlation**.  

- Formula:$$y[n] = \frac{\sum_k (x[n + k] - \bar{x})(h[k] - \bar{h})}{\sqrt{\sum_k (x[n + k] - \bar{x})^2} \cdot \sqrt{\sum_k (h[k] - \bar{h})^2}}$$
- Simplified form:$$y[n] = \frac{L \left( \sum_k x[n + k] h[k] \right) - \left( \sum_k x[n + k] \right) \left( \sum_k h[k] \right)}{\sqrt{L \sum_k x[n + k]^2 - \left( \sum_k x[n + k] \right)^2} \cdot \sqrt{L \sum_k h[k]^2 - \left( \sum_k h[k] \right)^2}}$$
where $L$ is the length of the filter.

## Pearson Correlator (2D Representation)

A correlator is sensitive to the magnitude of the input:  

- **Solution**: Scale the input.  
- For example, through **Pearson correlation**.  

- Formula:$$y[n, m] = \frac{\sum_i \sum_j (x[n + i, m + j] - \bar{x})(h[i, j] - \bar{h})}{\sqrt{\sum_i \sum_j (x[n + i, m + j] - \bar{x})^2} \cdot \sqrt{\sum_i \sum_j (h[i, j] - \bar{h})^2}}$$
- Simplified form:$$y[n, m] = \frac{L^2 \sum_i \sum_j x[n + i, m + j] h[i, j] - (\sum_i \sum_j x[n + i, m + j]) (\sum_i \sum_j h[i, j])}{\sqrt{L^2 \sum_i \sum_j x[n + i, m + j]^2 - (\sum_i \sum_j x[n + i, m + j])^2} \cdot \sqrt{L^2 \sum_i \sum_j h[i, j]^2 - (\sum_i \sum_j h[i, j])^2}}$$  

where $L^2$ is the number of elements in the (square) filter.  

**Note**: This **Pearson correlator** is not a linear filter.

---
# Shape Detection

- when searching for patterns, they might not be upright
- how do we account for this?
## (Freeman) Chain Coding

Define objects by their contours:  
- A **contour** is a periodic description.  
- Each point describes the angle of the next point.  
- Objects to recognize can be described by their contour.  

**Figure**: Image by Pavel Torgashov, Code Project  
![[Pasted image 20241217142052.png]]
**Figure**: Image by Pavel Torgashov, Code Project
![[Pasted image 20241217142136.png]]


**Figure**: Image by Shahram Ebadollahi, Columbia University
![[Pasted image 20241217142237.png]]
- Alternatively, take the DFT of contour coordinates
	- interpreting the vertical axis the axis and the vertical one as the real axis

---
## Take-home Messages

- From previous lectures, we have learned that analyzing signals and systems in the frequency domain is easier.  
- The **DFT** is a tool to move signals in the frequency domain.  
- The **IDFT** is the inverse operation, i.e., moving signals back to the time domain.

---
