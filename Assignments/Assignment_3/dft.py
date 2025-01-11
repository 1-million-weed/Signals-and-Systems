"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 08/01/2025
Description: 
    This module provides an implementation of the Discrete Fourier Transform (DFT) 
    using the Vandermonde matrix approach.
"""

from interface import ThemisInterface
from cmath import pi, exp

class DFTVandermonde(ThemisInterface):

    def get_input_data(self):
        self.x, self.L = self.readSignal()
    
    def run(self):
        # First we need to create the Vandermonde matrix
        W = self.build_vandermonde(self.L)
        if self.verbose: # this is a ThemisInterface attribute
            print(W)
        # Next we need to compute the dot product
        self.X = self.dot_product(self.x, W)
        if self.verbose:
            print(self.X)

    def build_vandermonde(self, length: int) -> list[list[float]]:
        # Calculate omega
        omega = exp(-(2j*pi) / length)
        # Use list comprehension to create the Vandermonde matrix
        # Honestly, list comprehension is at this point just so much easier to use
        # than loops. It might not be more readable, but it is more concise.
        # And i like it. I wrote tests for all these functions, if you want them, 
        # please email me.
        return [[omega ** (i * j) for j in range(length)] for i in range(length)]
    
    def dot_product(self, x: list[int], W: list[list[float]]) -> list[float]:
        # list comprehension for dot product of matrix and vector
        return [sum(W[j][i] * x[i] for i in range(len(x))) for j in range(len(W))]
    
    def print_output_data(self):
        # Finally, we can print the output data
        for i in range(len(self.X)):
            real = self.cln(self.X[i].real)
            imag = self.cln(self.X[i].imag, j=True)
            print(f"{real}{imag}")

if __name__ == "__main__":
    DFTVandermonde()
        