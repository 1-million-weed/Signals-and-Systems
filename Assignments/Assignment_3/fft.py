"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 11/01/2025    
"""
from interface import ThemisInterface
from math import pi, cos, sin

class FastFourierTransform(ThemisInterface):
    
    def get_input_data(self):
        x, x_len = self.readSignal()
        self.x, self.x_len = self.pad_to_power_of_two(x, x_len)
    
    def pad_to_power_of_two(self, x:list[int], x_len:int)->tuple[list[int], int]:
        """Pad the input signal with zeros to the next power of 2."""
        if not self.power_of_two(x_len): # if x_len is not a power of 2
            length = self.next_power_of_two(x_len) # find the next power of 2
            for _ in range(length - x_len): # pad x with zeros
                x.append(0)
            x_len = length # update x_len
        return x, x_len

    def next_power_of_two(self, n:int)->int:
        """Find the next power of 2 greater than or equal to n."""
        power = 1
        while power < n:
            power *= 2
        return power

    def power_of_two(self, n:int)->bool:
        """Check if n is a power of 2."""	
        return n > 0 and (n & (n - 1)) == 0

    def run(self):
        self.combined = self.recursive_fft(self.x, self.x_len)
        
    def recursive_fft(self, x:list[int], x_len:int)->list[complex]:
        """Recursively calculate the FFT."""
        if self.verbose:
            print(f"x: {x}")
            print(f"x_len: {x_len}")
        
        # base case: list has 1 element
        if x_len <= 1:
            return x
        
        # split x into even and odd indeces
        x_even, x_odd = x[0::2], x[1::2]

        if self.verbose:
            print(f"x_even: {x_even}")
            print(f"x_odd: {x_odd}")
        
        # recursively calculate the FFT of the even and odd parts
        y_even = self.recursive_fft(x_even, len(x_even))
        y_odd = self.recursive_fft(x_odd, len(x_odd))
        
        # Combine the results of the even and odd parts
        y = [0] * x_len
        theta = -2 * pi / x_len
        for k in range(x_len // 2):
            # generate the complex number omega
            real = cos(theta * k)
            imag = sin(theta * k)
            omega = complex(real, imag)
            # calculate the combined values
            y[k] = y_even[k] + omega * y_odd[k]
            y[k + x_len // 2] = y_even[k] - omega * y_odd[k]

        return y

    def print_output_data(self):
        for i in range(len(self.combined)):
            real = self.cln(self.combined[i].real)
            imag = self.cln(self.combined[i].imag, j=True)
            print(f"{real}{imag}")

if __name__ == "__main__":
    FastFourierTransform()