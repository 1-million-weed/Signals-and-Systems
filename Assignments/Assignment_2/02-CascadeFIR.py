"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: 
    This class is used to implement a cascade FIR filter.
    The class is a subclass of the ThemisInterface class.
    The class applies FIR filters in a cascade configuration
    to a signal.
"""

from interface import ThemisInterface

class CascadeFIR(ThemisInterface):
    
    def get_input_data(self):
        """Get input data from Themis."""
        # Read the number of filters
        self.num_filters = int(input())
        # Read the filters
        self.filters = []
        for _ in range(self.num_filters):
            kernel, _ = self.readSignal()
            self.filters.append(kernel)
        # Read the signal
        self.signal, self.signal_length = self.readSignal()

    def FIR(self, kernel: list[int], signal: list[int]) -> list[int]:
        """
        Compute y[n] from x[n] and h[n]

        Args:
            kernel (list of ints): The kernel to apply to the signal.
            signal (list of ints): The signal to apply the kernel to.
        
        Returns:
            list of ints: The output signal.

        NOTE:
            This function is taken from the FIRFilter class.

            I have a system of running it with Themis and changing that 
            system to be able to create an instance of the FIRFilter class
            and run FIR filter is not in the books for tonight.
        """
        # Length of the output signal
        output_length = len(signal) + len(kernel) - 1
        # Initialize the output signal
        output = [0] * output_length
        # Iterate over the "output" signal
        for i in range(output_length):
            result = 0
            for j in range(len(kernel)):
                signal_index = i - j
                # Stay in bounds of the signal
                if 0 <= signal_index < len(signal):
                    # Multiply the kernel with the signal
                    result += signal[signal_index] * kernel[j]
            # Set that value in the output signal
            output[i] = result
        return output

    def run(self):
        """Compute y[n] from x[n] and all h[n]"""
        # We will utilize the FIR function to apply all filters to the signal.
        for i in range(self.num_filters):
            self.signal = self.FIR(self.filters[i], self.signal)

    def print_output_data(self):
        """Print the output data."""
        self.printSignal(self.signal)

if __name__ == "__main__":
    CascadeFIR()