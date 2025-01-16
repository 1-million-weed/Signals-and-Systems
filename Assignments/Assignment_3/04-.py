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

    def run(self):
        self.combined = self.recursive_fft(self.x, self.x_len)
        
    def recursive_fft(self, x:list[int], x_len:int)->list[complex]:

        if self.verbose:
            print(f"x: {x}")
            print(f"x_len: {x_len}")
        
        # base case: list has 1 element
        if x_len == 1:
            return x[0]
        
        # check if x is None: first iterations - Why???
#        if self.x is None:
#            # get input data
#            self.get_input_data()

        # check length of x is power of 2
        if x_len // 2 == 1:
            # pad x with zeros
                x.append(0)
                x_len += 1

        # split x into even and odd indeces
        x_even, x_odd = x[0::2], x[1::2]
        if self.verbose:
            print(f"x_even: {x_even}")
            print(f"x_odd: {x_odd}")
        
        # recursively calculate the FFT of the even and odd parts
        ye = self.recursive_fft(x_even, len(x_even))
        yo = self.recursive_fft(x_odd, len(x_odd)) # why len(x_even) and not len(x_odd)?
        
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

    def print_output_data(self):
        for i in range(len(self.combined)):
            real = self.cln(self.combined[i].real)
            imag = self.cln(self.combined[i].imag, j=True)
            print(f"{real}{imag}")

if __name__ == "__main__":
    FastFourierTransform(verbose=True)