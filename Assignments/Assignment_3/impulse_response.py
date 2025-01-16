"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 11/01/2025
Description:
    This module provides an implementation of the Z-transform of an impulse response.
    It calculates the coefficients of the polynomially expanded form of the Z-transform
    from the roots of the impulse response.
"""

from interface import ThemisInterface
from math import sin, cos

class ZTransformImpulseResponse(ThemisInterface):

    def get_input_data(self):
        self.M = int(input())
        self.angles = list(map(float, input().split()))
    
    def run(self):
        # Okay, after about 3 days of sitting with the math to solve this question
        # I finally figured out the formulas for the coefficients of the polynomially
        # expanded form of the Z-transform from the roots. 
        # I hope i have enough time to write the documentation, else you're just going
        # to get a PDF with my iPad notes. 

        # Right, to solve this, we need three main concepts:
        # 1. The main function
        # 2. The itertools.combinations() python built-in function. OMG, if we dont have this, we're screwed.
        # 3. The product() function to multiply the combinations of roots.

        # Its actually a really elegant solution, I like it.

        # Lets start:
        # Convert the angles to complex numbers
        roots = [complex(cos(angle), sin(angle)) for angle in self.angles]

        n = self.M + 1 # setting the iteration limit
        coefficients: list[complex] = [0] * n # Initializing the coefficients list
        coefficients[0] = 1.0 # setting the first coefficient to 1.0

        # So before, I brute forced the solution by calculating the product of all 
        # combinations of roots. This is a very inefficient solution.
        # Then I found Horner's method, which is a much more efficient solution.

        # Horner's method is considered a dynamic programming approach that calculates
        # the polynomial coefficients in O(n^2) time complexity instead of O(2^n) time complexity.
        for root in roots:
            for i in range(len(coefficients) - 1, 0, -1):
                coefficients[i] -= root * coefficients[i - 1]

        self.coeffs: list[complex] = coefficients

    def old_implementation(self):
        # As the function name says, here is my crazy long brute force solution.
        # placeholder variables so the ide can stop shouting at me.
        n = 0
        combinations = 0
        roots = [0]
        coefficients = [0]
        for i in range(1, n):
            product_sum: float = 0 # Initialize the sum of the product of the combinations of roots
            # Find the combinations of roots with length i
            for comb in combinations(roots, i):
                # Multiply the combinatins of roots
                product_sum += self.product(comb)
            coefficients[i] = (-1)**i * product_sum # every second coefficient is negative

    def product(self, roots: list[complex]) -> complex:
        """
        Multiply the roots together.

        Args:
            roots (list[complex]): The roots to multiply.
        
        Returns:
            complex: The product of the roots.
        """
        # yeah, we dont use this anymore either. Thanks Horner's method.
        result = 1
        for root in roots:
            result *= root
        return result

    def print_output_data(self):
        result = [f"{coeff.real:.2f}" for coeff in self.coeffs]
        print(f"{len(result)}: [{', '.join(result)}]")

if __name__ == "__main__":
    ZTransformImpulseResponse()
