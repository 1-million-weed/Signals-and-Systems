---
tags:
  - Marinus
  - Assignment
  - Matthijs
Created: 2024-12-17
---
# Topics 
- [[Lecture 5 - FIR Filters]]
- Frequency Response

## Documentation
Needs to be similar to this:
- [pytorch](https://pytorch.org/docs/stable/generated/torch.optim.SGD.html)
  [Source code](https://pytorch.org/docs/stable/_modules/torch/optim/sgd.html#SGD)
- [**Keras**](https://keras.io/api/optimizers/sgd/)
  [Source code](https://github.com/keras-team/keras/blob/v2.14.0/keras/optimizers/sgd.py#L26)
  
"The requested documentation for this lab assignment is a high-level description of your code using the criteria above." [[lab2-main.pdf#page=1&offset=56.693,447.51|lab2-main, About the Documentation]]
## Style

For tips on type hinting and pep8 style recommendations:
- [Type Hinting](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [PEP8](https://peps.python.org/pep-0008/)

## Grade 
- 70% code
- 30% documentation
- look at [[lab2-main.pdf#page=2&offset=56.693,344.944|lab2-main, Grading Criteria]] for more info

# 2. Problems - Notes
## General notes:
look at [[formula-sheet - Copy.pdf]] for formulas and mathematical coefficient defs 
look at [[Sigsys_cheatsheets - Copy.pdf]] for concepts
## 2.1
This function will be used in following exercises
- *Sliding the filter through the signal* = Convolution of $h[n]$ and $x[n-k]$
- [[lec4-main1.pdf]] slide 36 on *convolutions*
- math to do:
1. **Input**: Kernel $h[n]$, discrete input signal $x[n]$
   Parse the input h\[n] into an array
2. Calculate the sum of rows in matrix with columns $h[n]*x[n-k]$ like: 
   {$h[0]*x[n-0]$, $h[1]*x[n-1]$ , $h[2]*x[n-2]$ }
3. **output**: vector with results

## 2.2
- FIR filter: a kernel used to modify a signal. 
- Cascade: we apply the signals one by one
1. **Input**: 
   number of filters $i$ 
   \[filters 1:$i$\]  
   signal
   The **layout** of the input is as follows:
   $j$: \[elements 1:$j$ ]
2. Run the signal through the filters
	For any filter $i$ the next filter is $i+1$
	
*notepad is the goat*
k number of filter
h_k filter kernel (1 through k)
input signal x\[n]

output signal y\[n]

Formatting examples:
\[examples]

method: Run it through code from 2.1 k times

## 2.3
**"Write the documentation for this problem."**
FIR filter checker
- ~for the inverse of a filter, we take the inverse of the matrix


1. **Input**: 
   discrete input signal x\[n]
   output signal y\[n]
2. Calculate:
   ~Find the filter that transforms signal x\[n] into y\[n]
   ~we can do the inverse math of before:
   Get h_1 from first value of the output signal
   calculate h_2 by subtracting h_1 from second value of output signal
   repeat until we have a signal
   !make 'Try:' with NO FIR as exception 
3. **output**: The newly constructed filter

## 2.4
- Frequency response: In the *frequency domain*, the **frequency response** of a system is the quantitative measure of the **magnitude** and **phase** of the output as a function of input frequency.
- coefficients: 
  (Rounded to two (2) decimal points)
	- A_x: The amplitude of input signal x
	  if =0 --> the output signals should be y\[n]=0.00
	- ˆω: The radian frequency
	- ϕx: the phase
	  -pi<ϕy<=pi
x\[n] = Ax cos(ˆωn+ϕx)
y\[n] = h\[n]∗x\[n]  = Ay cos(ˆωn + ϕy)
1. **Input**:
   two lines:
   Impulse response h\[n] of the FIR filter
   Three floats: A_x, ˆω, ϕx  (defined above)
2. For the math be sure to check out the sheets marked under [[#General notes]] 
   ~ we have the components of a signal x, and a filter. We want to make the resulting signal y's components
   ! firstly make an exception check for A = 0
   Example:
Input:
- h[n]=[1,2,1]h[n] = [1, 2, 1]h[n]=[1,2,1]
- $Ax=3A_x = 3Ax​=3, ω^=1.0472\hat{\omega} = 1.0472ω^=1.0472, ϕx=−1.5708\phi_x = -1.5708ϕx​=−1.5708$

Steps:
Compute $H(\hat{\omega})$:
    
    $$H(ω^)=1⋅e−j⋅0+2⋅e−j⋅1.0472⋅1+1⋅e−j⋅1.0472⋅2H(\hat{\omega}) = 1 \cdot e^{-j \cdot 0} + 2 \cdot e^{-j \cdot 1.0472 \cdot 1} + 1 \cdot e^{-j \cdot 1.0472 \cdot 2}H(ω^)=1⋅e−j⋅0+2⋅e−j⋅1.0472⋅1+1⋅e−j⋅1.0472⋅2$$
    
    
Compute $Ay$​:
    
    $Ay=Ax⋅∣H(ω^)∣A_y = A_x \cdot |H(\hat{\omega})|Ay​=Ax​⋅∣H(ω^)∣$
Compute $ϕy\phi_yϕy$​:
    
    $$ϕy=ϕx+∠H(ω^)\phi_y = \phi_x + \angle H(\hat{\omega})ϕy​=ϕx​+∠H(ω^)$$
Normalize $ϕy\phi_yϕy$​, round values, and output.
3. **Output**: y\[n] = A_y cos( ˆωn - ϕy) 

## 2.5
**Write the documentation for this problem.**
- Similar to 2.4, but here we add two outputs to form y\[n]
- PICTURE TIME
  ![[Pasted image 20241219123027.png]]
- Adding signals: as simple as x\[n]=x1​\[n]+x2\[n]
- Reuse function from 2.1 for finding filtered vectors
1. **Input**: 
   Three lines:
   Impulse response h_1\[n]
   Impulse response h_2\[n]
   Three floats: A_x, ˆω, ϕx  (defined above in 2.4)
$x[n] = Ax cos(ˆωn + ϕx)$
2. ~The program should calculate the output signal y\[n] = Ay cos(ˆωn + ϕy)
   - Again, if A = 0, output = y\[n]=0.00
   - $\phi_y$ should be between -pi and pi : −π < ϕy ≤ π
	Method:
~Calculate both filtered signals separately
	For this we can use the code from 2.1
~add signals
	use formula x\[n]=x1​\[n]+x2\[n] to add signals per time index

3. **Output**:
   (rounded to two digits (e.g.: 4.20))
   y\[n]= A_y cos( ˆωn - ϕy) 

## 2.6
Edge detection on black and white images.
- slide \[65 / 85] of [[lec4-main1.pdf]] 

Using two kernels:
![[Pasted image 20241219130757.png]]

How to find Y\[n,m]
![[Pasted image 20241219131006.png]]
(we ignore edge effects: the output image will be 2 pixels narrower, 2 pixels shorter than input image)

- name of function: performSobelEdgeDetection
- produces: 
	  a grayscale image that is exactly 2 pixels narrower and 2 pixels shorter than the input, 
	  and that represents the result of performing Sobel edge detection on the input image.
Files (images) can be found on themis

1. **Input**:
   An image of size height H x length L (e.g.: 100 pixels x 200 pixels)
2. **Steps**:
   !we can combine filters with convolution formula $hc​[n]=h1​[n]∗h2[n]$
   
   ~calculate the value of each pixel
   ![[Pasted image 20241219132609.png]]
   Math:
   for a pixel x\[n,m] we look at 9 pixels: y\[n-1,m-1] till y\[n+1,m+1]
   (this is why the border gets smaller, we can't calculate the border as we need the values from all around the pixel)
3. **Output**:
   An image of size H-2 x L-2 (1 pixel smaller on all borders)


---
Done.
Well done.
Good job.
Rest now.
'Till the next time.