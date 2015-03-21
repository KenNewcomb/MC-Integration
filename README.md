MC-Integration
============

A [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) integral calculator. MC-Integration can provide an approximation any definite integral, given the bounds and the number of random points to sample. The function must be defined using Python's mathematical syntax.

Usage
------	

	python3 mc-integration.py f(x) lower_bound upper_down number_of_points

Example
-------

Let's approximate the integral of x<sup>3</sup>-4 from 0 to 2 using 500 points. (the exact value is -4). 

	python3 mc-integration.py x**3-4 0 2 500

	Integral approxmiation: -4.060910029853514

5000 points?

	python3 mc-integration.py x**3-4 0 2 5000

	Integral approxmiation: -3.994592511499465
