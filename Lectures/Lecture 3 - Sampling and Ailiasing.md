---
tags:
  - _FirstPass
  - Lectures
  - Marinus
---
# Recap
- periodic functions can be expressed as possible infinite sum of harmonically related sinusoids
- $a_k$ coefficient is not easy to obtain.

# Spectrum
- Amplitude Modulation(AM) and Frequency Modulation (FM)b 

## Amplitude modulation

- Beat notes are combinations of two sinusoids  (product)
- A lot of math using Euliers formula 
- expressing the sum in terms of averages and differences
- Basically, everything uses the Euliers formula
- we go from complex to real, 
- ![[Pasted image 20241126132116.png]]
- Red is carrier signal, Blue is information

- AM Radio
	- $x(t)=v(t)\cos(s\pi f_c t)$
- ![[Pasted image 20241126132300.png]]
- The beam (line) is the information we want to carry
- the Red signal is the carrier wave
- Here is a better expression ![[Pasted image 20241126132356.png]]
- The carrier wave is a certain frequency that avoids interference 
	- that way we can have multiple carrier waves in the same area but with no interference

## Time frequency spectrum
> A `spectogram` shows variation in the spectrum over time
- Similar to sheet music 
	- Horizontal axis represents time 
	- Vertical axis represents frequency

- can be converted in the following way:![[Pasted image 20241126132722.png]]
- In music, each note represents a range of frequencies
- at changes in notes, we can a wider range of frequencies, this is considered noise from the instrument![[Pasted image 20241126132820.png]]
- each song you have has a unique spectrogram Shazam
	- get spectrogram of each song

## Chirp signals
> A chirp signal changes frequency over time
- the change in frequency is linear
- represented as a quadratic angle formula 
$$
x(t) = A \cos(\psi(t)) = A \cos(2\pi \mu t^2 + 2\pi f_0 t + \phi)
$$
## Instantaneous frequency
- Frequency measures the rate of change of angle $\theta$
$$
\omega_i(t) = \frac{d}{dt} \psi(t) = \frac{d}{dt} \left( 2\pi \mu t^2 + 2\pi f_0 t + \phi \right) = 4\pi \mu t + 2\pi f_0
$$

$$
f_i(t) = \frac{1}{2\pi} \omega_i(t) = 2\mu t + f_0
$$
- normally looks like a line

- Synthetic Vowel

---
# Break
---
# UG Impact Challenge

innovation challenge 
business for impact
ideas to business solutions
- bs i give up on these notes
- back to the lecture

# Sampling

-  continious discrete converter system
	- System: some sort of transformation of a signal
	- encoding decoding
	- could be a physical component that makes these signal changes
	- manipulate signal on continous time
- Applications are computer based
	- manipulations are done on discrete signals 
	- continious signals have to be discretized
	- Digital signals have to be made continuous
- ![[Pasted image 20241126140650.png]]
- ![[Transformations Lec 3.canvas]]
- Analog to Digital 
	- n is an integer number. (equation 5)
- common sampling rate for audio is 44100 Hz
- $\hat\omega$ is not the same as $\omega$
- if the sample rate is too long, we cannot reproduce the continuous signal (undersampling)![[Pasted image 20241126141503.png]]
- sampling rate/period gives ground ot recover continuous signals
- next is under sampling and antiailiasing

# Aliasing

- used in computer graphics and games
- next week tutorial is about antialiasing
- Suppose we sample \( \cos(2\pi(100)t) \) at \( f_s = 500 \)

  $$
  x_1[n] = \cos\left(2\pi(100)n / 500\right) = \cos(0.4\pi)
  $$

- Suppose we also sample \( \cos(2\pi(600)t) \) at \( f_s = 500 \)

  $$
  x_1[n] = \cos\left(2\pi(600)n / 500\right) = \cos(2.4\pi) = \cos(0.4\pi)
  $$

- Suppose we also sample \( \cos(2\pi(400)t) \) at \( f_s = 500 \)

  $$
  x_1[n] = \cos\left(2\pi(600)n / 500\right) = \cos(1.6\pi) = \cos(-0.4\pi) = \cos(0.4\pi)
  $$
- same discrete time signals with different sinusoids.
- prime example of under sampling and the issues of trying to reconstruct the continuous signal

- Shannon sampling theorym
	- wasnt concentrating

- Nyquist rate is what we call the best sampling rate 
	- $f_s>2f_{max}$
- sample human hearing two times
	- not sure what his point was here

- We always want to oversample our signals. practical

## Reconstruction
![[Pasted image 20241126142733.png]]
- Analog to Digital converter
- we can restrict our conversion to the range of $[-\pi;\pi]$
- need to make sure we are not under sampling/extreme aliasing
- 4KHz of difference (from 44KHz or something)
	- we love over sampling
	- reconstruction will not be precise
	- compensates for noise in electrical components
- Frames per seconnddddd!!! 30, 60, 120, 240 or 360

## Interpolation Pulses

- go to the lecture slides bitch and look at the formula
- multiply output of discrete signal with pulse function and interpolate it 
- now we talk about zero hold interpolation
- can we do it better? the answer is yes... haha 
- get me outta here
- i am low on sleep and wanna play some squash
- and beat matthijs's ass
- jk, im gonna get smashed

- ooooh, we can do it better
	- we use linear interpolation
	- instead of pulses, we do linear lines
	- called triangular pulses
	- now we need to fill the gaps 
	- the higher our sampling rate the smaller the gaps
- can we do it perfectly?
	- Cube spline?
	- smoothness into reconstruction
	- third order plynomials
	- avoid edges
	- perfect reconstruction
	- fourier series in continuous time (sinc function)