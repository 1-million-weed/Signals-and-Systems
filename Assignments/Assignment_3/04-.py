"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 11/01/2025    
"""
from interface import ThemisInterface
from math import pi
from cmath import exp

class FastFourierTransform(ThemisInterface):
    
    def get_input_data(self):
        self.x, self.x_len = self.readSignal()

    def run(self, x:list=None, x_len:int=None):
        self.x_len = x_len
        self.x = x
        
        # base case: list has 1 element
        if self.x_len == 1:
            return x[0]
        
        # check if x is None: first iterations
        if self.x is None:
            # get input data
            self.get_input_data()
        
        # check length of x is power of 2
        if self.x_len // 2 == 1:
            # pad x with zeros
                self.x.append(0)
                self.x_len += 1
        
        # split x into even and odd indeces
        x_even = self.x[0::2]
        x_odd = self.x[1::2]
        
        # recursively calculate the FFT of the even and odd parts
        FastFourierTransform.run(self, x_even, len(x_even))
        FastFourierTransform.run(self, x_odd, len(x_even))
        
        # Combine the results of the even and odd parts
        x_new = []
        for k in range(self.x_len // 2):
            x_new.append(exp(-2j * pi * k / self.x_len) * x_odd[k])

        combined = []
        for k in range(self.x_len // 2):
            combined.append(x_even[k] + x_new[k])

        for k in range(self.x_len // 2):
            combined.append(x_even[k] - x_new[k])

        return combined


if __name__ == "__main__":
    FastFourierTransform()