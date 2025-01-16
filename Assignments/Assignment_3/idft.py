"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 11/01/2025
Description: 
    This module provides an implementation of the Inverse Discrete Fourier Transform 
    (IDFT) using the Vandermonde matrix approach.
"""

from interface import ThemisInterface
from math import pi, sin, cos

class IDFTVandermonde(ThemisInterface):

    def get_input_data(self):
        self.x, self.L = self.readSignal()
    
    def run(self):
        # First we need to create the Vandermonde matrix
        W = self.build_vandermonde(self.L)
        if self.verbose: # this is a ThemisInterface attribute
            print(f"W: {W}")
        # Next we need to compute the dot product
        self.X = self.dot_product(self.x, W)
        if self.verbose:
            print(f"X: {self.X}")

    def build_vandermonde(self, length: int) -> list[list[tuple[float, float]]]:
        # Let me make clear that I am not a fan of this matrix or question 
        # Our complexity is O(2n^2) which is horrible. 
        # Were first making the matrix with two for loops then we are 
        # multiplying it with a vector again with two for loops. 
        # This is very inefficient.
        vandermonde = []
        for n in range(length): # 
            row = []
            for k in range(length):
                # Calculate omega
                omega = 2*pi*n*k/length
                # Calculate the real and imaginary parts of the omega
                real = cos(omega) / length # normalize by length
                imag = sin(omega) / length # normalize by length
                # make the row of the matrix
                row.append((real, imag))
            # append the row to the matrix
            vandermonde.append(row)
        # return the matrix
        return vandermonde
        
    
    def dot_product(self, x: list[int], W: list[list[tuple[float, float]]]) -> list[tuple[float, float]]:
        # Initialize the result list
        self.X = []
        # Loop over the rows of the Vandermonde matrix (W)
        for row in W:
            # Initialize the real and imaginary parts of the dot product
            real_sum = 0.0
            imag_sum = 0.0
            if self.verbose:
                print(f"Row: {row}")
            # Loop over the columns of the Vandermonde matrix
            for k, (real, imag) in enumerate(row):
                # Compute the dot product of the real and imaginary parts
                real_sum += real * x[k]
                imag_sum += imag * x[k]
            self.X.append((real_sum, imag_sum))
        return self.X
    
    def print_output_data(self):
        # Finally, we can print the output data
        for i in range(len(self.X)):
            real = self.cln(self.X[i][0])
            imag = self.cln(self.X[i][1], j=True)
            print(f"{real}{imag}")

if __name__ == "__main__":
    IDFTVandermonde()
        

