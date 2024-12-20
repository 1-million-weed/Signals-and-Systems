"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: 
    This class is used to implement a cascade FIR filter.
    The class is a subclass of the ThemisInterface class.
    The class takes an input signal x[n] and output signal
    y[n] and finds the impulse response h[n] of the system
    if any.
"""

from interface import ThemisInterface

class ReverseFIR(ThemisInterface):
    """A class used to implement a cascade FIR filter."""

    def get_input_data(self):
        """Get input data from Themis."""
        self.input_signal, self.n_input = self.readSignal()
        self.output_signal, self.n_output = self.readSignal()

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
        """Run the reverse FIR function."""
        # Length of FIR Filter
        self.n_kernel = abs(self.n_input - self.n_output) + 1
        # Initialize the kernel
        self.kernel = [0] * self.n_kernel

        # Iterate over the kernel
        for i in range(self.n_kernel):
            # Start at the output signal
            current = self.output_signal[i]
            # Iterate over the input signal till the current index or 
            # the length of the input signal
            for j in range(1, min(i + 1, self.n_input)):
                # Minus the product of the kernel and the input signal
                current -= self.input_signal[j] * self.kernel[i - j]
            # Finally solve for the kernel by dividing the current value 
            # by the first value of the input signal
            self.kernel[i] = current // self.input_signal[0]

    def print_output_data(self):
        """Print the output data."""

        # Check if the calculated kernel coefficients are correct
        # If correct, return the kernel coefficients
        if self.output_signal == self.FIR(self.kernel, self.input_signal):
            self.printSignal(self.kernel)
        else:
            print("NO FIR")

if __name__ == "__main__":
    ReverseFIR()
        
