"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: 
    This class is used to implement FIR filter.
    The class is a subclass of the ThemisInterface class.
    The class applies a FIR filter to a signal.
"""

from interface import ThemisInterface

class FIRFilter(ThemisInterface):
    """A class used to implement a FIR filter."""
    
    def get_input_data(self):
        """Get input data from Themis."""
        # Read the kernel and signal
        self.kernel, self.kernel_length = self.readSignal()
        self.signal, self.signal_length = self.readSignal()

    def run(self):
        """Run the specified fuction."""
        # we want to convolve the kernel with the signal
        # we can do this by iterating over the signal and
        # multiplying the kernel with the signal at the
        # current index and finally summing the results

        # Length of the output signal
        output_length = self.signal_length + self.kernel_length - 1
        # Initialize the output signal
        self.output = [0] * output_length
        # Iterate over the output signal
        for i in range(output_length):
            result = 0
            for j in range(self.kernel_length):
                signal_index = i - j
                # Stay in bounds of the signal
                if 0 <= signal_index < self.signal_length:
                    # Multiply the kernel with the signal
                    result += self.signal[signal_index] * self.kernel[j]
            # Set that value in the output signal
            self.output[i] = result
        return self.output

    def print_output_data(self):
        """Print the output data."""
        self.printSignal(self.output)

if __name__ == "__main__":
    FIRFilter()