# 109titration - Derivatives and preservatives

[![Build Status](https://travis-ci.org/mrlizzard/PSU_minishell2_2017.svg?branch=master)](https://travis-ci.org/mrlizzard/PSU_minishell2_2017)

- **Binary name:** 109titration
- **Repository name:** 109titration_2017
- **Repository rigths:** ramassage-tek
- **Language:** Python 3

# Subject

The benzoic acid (whom molecule is hereby represented) is used in industry as a food preservative under the E220 code. It is a white silky-looking solid.
To dertermine the concentration of this additive in a solution, one can realize a pH titration: soda is progressivly added to the solution, and pH is then read.
The generated curve is typical, and has an area where pH brutally increases: it is the pH-jump.
To find the volume of preservative of the initial solution, the volume of added soda at the equivalent point (ie at the middle of the pH-jump) must be read.

There are two main approaches to do so :
- the derivative method, which consists in calculating the derivative of the curve ; the equivalent point matches with the maximum of this derivative,
- the parallel tangents method, which consists in drawing two parallel tangents from one part and another of the pH-jump, then to draw a third straight line quidistant from the two first. The equivalent point is at the intersection between this last line and the curve.

Lucky you, only the first approach is to be coded here.
Your program has to read pH and soda volume (in ml) couples from a csv file, and output :
- the derivative values for each given volume,
- the closest point from the equivalent point amongst those given points,
- the second derivative values for each given volume,
- an approximation of the second derivative values every 0.1ml around the above closest point from the equivalent point,
- the proper equivalent point, estimaed from the second derivative.

> :bulb: To approximate the derivative, the centered rate is defined in the course as the mean of the forward and backward rates. Since abscissas are not equidistant here, coefficients must be cleverly put in front of the rates when computing the mean.
> **Beware the coefficients have a sum of 1 !**

```
∼/B-MAT-200> ./109titration -h
USAGE
	./109titration file

DESCRIPTION
	file	a csv file containing "vol;ph" lines
```

> :exclamation: Your program output has to be strictly identical to the one below

```
∼/B-MAT-200> cat values.csv
1;2
2;3
3;4
5;4.4
6;4.6
7;6
7.5;6.8
8;8
9;10
12;11.3
14;11.46
16;11.6
20;11.8
```

```
∼/B-MAT-200> ./109titration values.csv
Derivative:
volume: 2 ml -> 1.00
volume: 3 ml -> 0.47
volume: 5 ml -> 0.20
volume: 6 ml -> 0.80
volume: 7 ml -> 1.47
volume: 7.5 ml -> 2.00
volume: 8 ml -> 2.13
volume: 9 ml -> 0.83
volume: 12 ml -> 0.29
volume: 14 ml -> 0.07
volume: 16 ml -> 0.06

Equivalent point at 8 ml

Second derivative:
volume: 3 ml -> -0.27
volume: 5 ml -> 0.11
volume: 6 ml -> 0.63
volume: 7 ml -> 0.80
volume: 7.5 ml -> 0.67
volume: 8 ml -> -0.78
volume: 9 ml -> -0.46
volume: 12 ml -> -0.15
volume: 14 ml -> -0.06

Second derivative estimated:
volume: 7.5 ml -> 0.67
volume: 7.6 ml -> 0.38
volume: 7.7 ml -> 0.09
volume: 7.8 ml -> -0.20
volume: 7.9 ml -> -0.49
volume: 8 ml -> -0.78
volume: 8.1 ml -> -0.75
volume: 8.2 ml -> -0.72
volume: 8.3 ml -> -0.69
volume: 8.4 ml -> -0.65
volume: 8.5 ml -> -0.62
volume: 8.6 ml -> -0.59
volume: 8.7 ml -> -0.56
volume: 8.8 ml -> -0.52
volume: 8.9 ml -> -0.49
volume: 9 ml -> -0.46

Equivalent point at 7.7 ml
```
