---
tags:
  - Marinus
Created: 2025-01-07
---
# Problems

## 2.1 Template matching using Pearson correlator

Lecture notes on this: [[Lecture 6 - Fourier Transform#Pearson Correlator (1D Representation)]]

>[!note] Simplified Formula
> $$y[n] = \frac{L \left( \sum_k x[n + k] h[k] \right) - \left( \sum_k x[n + k] \right) \left( \sum_k h[k] \right)}{\sqrt{L \sum_k x[n + k]^2 - \left( \sum_k x[n + k] \right)^2} \cdot \sqrt{L \sum_k h[k]^2 - \left( \sum_k h[k] \right)^2}}$$

---
## 2.2 Discrete Fourier transform using Vandermonde matrix

In lecture notes: [[Lecture 6 - Fourier Transform#Computing Fourier Transform]]

The Vandermonde matrix $W$ is defined as:

$$
W =
\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega & \omega^2 & \cdots & \omega^{N-1} \\
1 & \omega^2 & \omega^4 & \cdots & \omega^{2(N-1)} \\
1 & \omega^3 & \omega^6 & \cdots & \omega^{3(N-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega^{N-1} & \omega^{2(N-1)} & \cdots & \omega^{(N-1)(N-1)}
\end{bmatrix},
$$


where $\omega = e^{-2\pi i / N}$ is the $N$th root of unity.

Discrete Fourier transform formula: $$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}kn}$$
- Using the Vandermonde Matrix is a bit of a hassle
- It means we will end up with a complexity of $O(2n^2)$. This is because:
	- We first need to use two nested for loops to construct the Vandermonde Matrix
	- Then we need to do the dot product of the input vector and the matrix. 

Then I figured out another thing to do with `cmath` and `math`
- if we use `cmath`, we can construct the matrix using the normal formula for $\hat{w}$: $$\hat{\omega} = \frac{2\pi k}{N}, \quad \hat{\omega} \in [0, 2\pi).$$
- and simply go
```python
omega = exp(-(2j*pi) / length)
return [[omega ** (i * j) for j in range(length)] for i in range(length)]
```
- `cmath` allows us to raise the `exp` to the product of the row and column $(i\&j)$ properly, shown in the formula as $(n\&k)$  
- For this question we used list comprehension to cut down on lines of code.
	- It should not be too hard to understand.
- We then simply dot product the input vector and the Vandermonde matrix:
```python
return [sum(W[j][i] * x[i] for i in range(len(x))) for j in range(len(W))]
```

- And finally extract the real and imaginary parts and print the results:
```python
for i in range(len(self.X)):
	real = self.cln(self.X[i].real)
	imag = self.cln(self.X[i].imag, j=True)
	print(f"{real}{imag}")
```

---
## 2.3 Inverse Discrete Fourier Transform using Vandermonde Matrix

Lecture notes: [[Lecture 6 - Fourier Transform#Inverse Discrete Fourier Transform (IDFT)]]

IDFT Formula:$$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j \frac{2\pi}{N} k n}$$
- For this question I wanted to knuckle down on the math even more and get rid of cmath to be more involved in the math. 
- This meant that when we construct the **Vandermonde matrix,** we need to use **Euler's formula** to separate the `real` and `imaginary` parts. 

**Euler's Formula:** $$e^{j\theta}=\cos(\theta)+j\sin(\theta)$$
- Since we have $w=e^{j \frac{2\pi}{N} k n}$
- Our $\theta=\frac{2\pi}{N} k n$
- so we can calculate our complex number in two parts and normalise[^1] it at the same time:
```python
omega = 2*pi*n*k/length
real = cos(omega) / length
imag = sin(omega) / length
```
Where:
- `length` is the length of the input signal
- `omega` is the $w$ value of the Vandermonde matrix
- `n` is the rows
- `k` is the columns

Thereafter, the Dot product is simply another nested for loop that calculates the running sum of the `real` and `imaginary` parts of the signals:
```python
real_sum += real * x[k]
imag_sum += imag * x[k]
```


[^1]: We normalise the values by dividing by $N$. Hence the division by `length` in the code.