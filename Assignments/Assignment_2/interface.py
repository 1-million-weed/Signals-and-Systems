"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: This file contains the interface class for Themis.
"""

class ThemisInterface:
    """
    An abstract class used to run our functions with Themis.
    """
    def __init__(self):
        """Constructor starts program when Themis calls."""
        self.get_input_data()
        self.run()
        self.print_output_data()
    
    def get_input_data(self):
        """Get input data from Themis."""
        pass

    def run(self):
        """Run the specified fuction."""	
        pass

    def print_output_data(self):
        """Print the output data."""
        pass

    def readSignal(self):
        """
        Read a signal from Themis.

        Returns:
            A tuple containing:
            - signal (list of ints): The signal read from Themis as a list of integers.
            - length (int): The length of the signal.
        """
        input_line = input().strip()
        length = int(input_line.split(':')[0])
        signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
        return signal, length
    
    def printSignal(self, signal):
        """
        Print a signal to Themis.
        
        Args:
            signal (list of ints): The signal to print to Themis.
        """
        print(f"{len(signal)}: {signal}")