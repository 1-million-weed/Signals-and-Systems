# Recap
signals: amplitude frequency and phase

Sinusoidal signal 
$$x(t)=Acos(w_0t+\phi)$$
Magnitude:
$$A=\frac{top-bottom}{2}$$

Units of periods is `time`

period
$$w_0=\frac{2\pi}{T}$$
Phase $\Phi$
$$150\pi(0.045)+\phi=2\pi(3.5)->\phi=0.25\pi$$

> Next comes euliers formula

Now we can add sinusoids with the same frequency:
$$x(t)=\sum$$


1. get the polar phaser
2. polar to cartesian coordinates. radius is amplitude, 
3. calculate sum of phasors 
4. convert cartesian to polar coords
5. obtain sinusoid

# Spectrum

Signal:
$$x(t)=Acos(2\pi f_0t+phi)$$

Inverse the eulier relation:
$${(f_0, \frac{A}{2}e^{j\phi})(f_0, \frac{A}{2}e^{-j\phi})}$$
We will then get a set of two numbers that describes our signal {($math$),($math$)}
- this frequency domain is `independent of time`
- conjugates of each other 
- representation of frequency 
- the amplitude would then be in terms of euliers formula ($\frac{A}{2}+\frac{A}{2}$)
- the radian is equal to two times pi times t
- if you have multiple additions of these, just add their individual results to the set
- if you have multiple, this could be seen as the amount of power the frequencies have

We can read signals from the spectram domain as well
- its basically just a read and put in type of thing.

# Harmonics

## Synthetic Vowel

![[Pasted image 20241119133536.png]]
You can easily guess the period of the cyclic motion from this signal. 
- this is for when you say "Ah"
- the period here is 0.01
- fundamental frequency is 100hz

> A signal $x(t)$ is periodic with a period $T_0 > 0$ if it satisfies: $$x(t+T_0)=x(t),\ for\ all\ t$$

### Non-periodic signal
![[Pasted image 20241119134306.png]]

# Fourier Series

## Change in notation

![[Pasted image 20241119140430.png]]

- when k is 0 this DC Component is closely related to the frequency and harmonics
- a way to represent any complex periodical signal as a sum of harmonically related sinusoids

Fourier synthesis summation
$$x(t)=\sum^{\infty}_{k=-\infty}a_ke^{j2\pi f_0kt}$$
$$x(t)=\sum^{\infty}_{k=-\infty}a_ke^{j\frac{2\pi}{T_0}kt}$$
- if $a_k$ and $F_0$ are known it is easy to generate $x(t)$
- § If $x(t)$ is known, it is not straightforward to determine $a_k$
> For a periodic signal with fundamanental period $T_0=\frac{1}{F_0},\ F_0>0$, the Fourier coefficients are 
> ![[Pasted image 20241119141440.png]]

Looked at a lot of square wave functions

Fourier approxomation
pure fourier signal 
![[Pasted image 20241119141743.png]]

the approximation becomes better the higher number of k's we have
this is useful for 
- lossy compression
- noise filtering 

approximation of signal $x(t)$ by taking finite number of fourier terms
$$x_N(t)=\sum^{N}_{k=-N}a_ke^{j\frac{2\pi}{T_0}kt}, 0 < N < \infty$$


![[Pasted image 20241119142008.png]]