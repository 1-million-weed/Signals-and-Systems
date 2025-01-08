"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 08/01/2025
Description: 
    
"""
from interface import ThemisInterface
from math import sqrt

class PearsonCorrelator(ThemisInterface):
    
    def get_input_data(self):
        self.h, self.h_len = self.readSignal()
        self.x, self.x_len = self.readSignal()

    def run(self):

        # Initialize the list of pearson correlation values
        pearsons = []

        # Lets start the first for loop for n
        for n in range(self.x_len - self.h_len + 1):
            if self.verbose:
                print(f"n: {n}")
            # Initialize the sums
            sum, sum1, sum2 = 0, 0, 0
            # First the top half of the equation
            for k in range(self.h_len):
                sum += self.x[n + k] * self.h[k]
                sum1 += self.x[n + k]
                sum2 += self.h[k]
            top = (self.h_len * sum) - (sum1 * sum2)
            if self.verbose:
                print(f"Top: {top}")
            # Clean the sums
            sum, sum1, sum2, sum3 = 0, 0, 0, 0
            # Next the bottom half of the equation
            for k in range(self.h_len):
                sum += self.x[n + k] ** 2 # remember L * sum
                sum1 += self.x[n + k] # square sum1
                sum2 += self.h[k] ** 2 # remember L * sum2
                sum3 += self.h[k] # square sum3
            bottom = sqrt((self.h_len * sum) - (sum1 ** 2)) * sqrt((self.h_len * sum2) - (sum3 ** 2))
            if self.verbose:
                print(f"Bottom: {bottom}")
            # Calculate the correlation
            correlation = top / bottom
            if self.verbose:
                print(f"Correlation: {correlation}")
            pearsons.append(correlation)
        
        self.pearsons = pearsons
        
    
    def print_output_data(self):
        print(len(self.pearsons), end = ": ")
        formatted_pearsons = "["+','.join(f"{p:.5f}" for p in self.pearsons)+"]"
        print(formatted_pearsons)


if __name__ == "__main__":
    PearsonCorrelator()