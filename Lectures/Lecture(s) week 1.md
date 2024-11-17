---
tags:
  - Marinus
  - Matthijs
  - Lectures
---
# Intro yap
---
Three main topics of the course
- Signals
- Systems {*surprise*}
- Transformers

# Grade
The grade is determined as such:
- 25% Assignments > 5.0
- 75% Final exam > 5.0

# Assignments 
The grade of the assignments is calculated as such:
- 70% Code
- 30% Documentation

## During the assignments
Do **not** use any **predefined functions**. During the course you have to implement these functions {*yes, even the basic shit*} yourself.
Also, make sure that you are writing **clean** code. 

## Late policy
An assignment handed in late will get points deducted as follows:
- For every 24 hours: grade -= 1.0\*
- 72 hours late --> grade = 0
\*if you hand in the code but not the documentation, only that part of the assignment will get deductions.

# Exam

>[!warning] Most of exam questions come form `tutorials`. A minority will be inspired by the `labs`.

> [!note] Q&A Quiz before exam on 17 January 
> A4 Cheat sheet (Double sided)

# Time
Time per week per course element:

| time | type |
|---|---|
| 2h\* | lecture |
| 2h | tutorials |
| 2h | q&a's |
\*except for week 1


# What is SaS?
---
### Intro
#### Why do AI Pros need to study this?

- There is a need to represent information. A better understanding of how signals are encoded can for example help us identify issues originating from noisy signals.
- pre-processing: perform operations on data
	- encoding
	- decoding
	- structuring
	- de-noising
	- store
	- Then adapt data to machine learning model
	- check data fit with model
- Ask questions like: "does it make sense to use this data in a linear system"

> {I did not take any notes of what signals are. Really intuitive}

#### Real life data example

| stage          | size       |
| -------------- | ---------- |
| Continues data | ~110mb/sec |
| Compressed     | ~300kb/sec |

Getting information from a signal can be challenging. {In class we had an example with a finance graph that had a drop in ~2020 --> we had to 'see' the reason: Covid. The example showed that underlying reasons might be hard to spot from just the data}

#### Signal dependent on time 
- types: E.g.: EEGs {ha ha}
- period: Per year, per millisecond, …
- position
#_Err_Mismatch #_Err_Design
### Definition [[Signal]]\*
\* Hint: check the definition with hover + ctrl! 
- *{put the pointer thingy on the purple thingy and press ctrl on the keyboard - do not use the mouse buttons here}*

> Continuous: function ~~f(x)~~ over time t ==\element R==. E.g. Human speech
> --> X(t)

> Discrete: Function x\[n\] that is only defined n ==\element== Z E.g. digital recording of human speech
> --> X\[t]

>[!note] Comment
>~~Note the convention of discrete-time x\[n\] continious time f(x)~~


#### Signals may be multi-dimensional 
- The signal then becomes x(s,t) or x\[x,t]
- Discrete real life example: pics by analogue camera 

> [!info] Weekend millionairs
> which of the following signals is discrete
> 1. temperature
> 2. eeg
> 3. electrocardiogram (ECG)
> 4. digital video

--> answer at bottom of the file
#_Err_Design 
### Definition [[System]]

- continuous-time system transforms continuous-time signals
	- ==y(t)=T{x(t)}==
- discrete-time system transforms discrete-time signals
	- ==Y\[n]=T{x\[n]}==
- sampler: continuous to digital signals
	- ==x\[n]=x(nTs)==
	- where ==Ts== is the sampling period


[[Conversions.canvas|Conversions]]


Complete tutorial exercises

---
Answer: it depends! {yeah, fuck you}