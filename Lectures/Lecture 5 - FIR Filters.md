---
tags:
  - Marinus
  - Lectures
  - _FirstPass
Created: 2024-12-10
---
# recap

- the FIR filters is closely related to time series and linear regression
- relationship is linear
- convolution between discrete signal x and filter h

- CNN and RNN
	- IRR filters and RNNs are similar. 
	- they use the IIR filters 
	- simple feed forward network, remove the activation function and you are left with a IIR filter

# Frequency reponse

- discrete signals 
- grouping coefficients with the complex association of the delays
- x and y have the same frequency

- amplitude modiefies signal
- he modifies the left hand side signal into the real and complex parts
- then in the third line he goes from cartesian to polar
- NOTE: Magnitude is never negative (equation inside abs)
- do not mix discrete and continuous

- time domain: n and k
- frequency domain: complex exponential
- make connections between time and frequency equations. 
	- we can see in the time we have n, n-1, n-2
	- in the frequency, we have the exponents of 0, -j, and -2j
- resulting in the magnitude and angle 
- $\hat{w}$ is form $-\pi$ to $\pi$
	- hence the jump n the slides 
- multiply amplitude and magnitude
- we shift the phase with the amplitude of the signal

## First-difference filter

- we can remove the bias on a signal
- combine real with real and complex with complex

- played some chess. didn't takes notes tilll cascaded LTI systems

- a convolution in the time domain in a multiplication of the frequency domain

---

BREAK

---

# Running sum filter

- Analyze in frequency domain
- time domain response for this filter is more interesting
- here we have some parts of the magnitude that are negative. we need to compensate for this somehow.
- we need to remove them somehow
- compensate those negative parts with the angle
- multiply it by a complex excponentional with pi
- This is like taking the absolute value but you also have to do this with the angle so you multiply it by the exponential
- angle of the filter should always be between -pi and pi
- it behaves as a **low pass filter**
	- remove high frequencies
	- low f are multiplied by high magnitude
	- high f are multiplied by a low magnitude
- any angle out of -pi and pi cannot be reconstructed
- in slide continuous to discrete signals (33)
	- we are oversampling. f > 2\*250
- (11-1)/2 gets us the 5 in the exponent of e
- this is used to calculate moving or running averages in stocks to pick up trends 
	- can use more than 40 points in practice 

# Smoothing Images
- causes a shift to the right. blurs it quite a bit as well.
	- but you can shift the moving average back by a couple of points to line it up again
- removes frequences with the multiple of L
- transient effect at end and start caused by the cosine filters

# Remarks

- take home
- a convolution in the time domain is a multiplication in the frequency domain.
- 