"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: This file contains the interface class for Themis.
"""

class ThemisInterface:
    """
    An abstract class used to run our functions with Themis.
    """

    def __init__(self, verbose: bool = False, themis: bool = True):
        """Constructor starts program when Themis calls."""
        # For debugging purposes
        self.verbose = verbose

        # If we are running the program in Themis 
        if themis: # default is True
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

    def readSignal(self) -> tuple[list[int], int]:
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
    
    def readInputSignal(self) -> tuple[int, int, int]:
        """
        Reads three values from Themis.

        Returns:
            A tuple containing:
            - A (int): The amplitude of signal x.
            - w (int): The radian frequency.
            - phi (int): The phase.
        """
        input_1, input_2, input_3 = map(float, input().split())
        return input_1, input_2, input_3
    
    def printSignal(self, signal: list[int]):
        """
        Print a signal to Themis.
        
        Args:
            - signal (list of ints): The signal to print to Themis.
        """
        print(f"{len(signal)}: {signal}")

    def cln(self, n: float, j: bool = False) -> str:
        """
        Cleans and formats a number for display.

        - If the number is very small (between -0.001 and 0.001), it returns "0.00".
        - If the number is imaginary (indicated by the `j` parameter), it returns the 
        number in the format "+j0.00", "-j0.00", or "+jN.NN" depending on the value
        of `n`.

        Parameters:
            - n (float): The number to be formatted.
            - j (bool): A flag indicating if the number is imaginary. Default is False.

        Returns:
            - str: The formatted number as a string.
        """

        # if the number is imaginary we return +j0.00
        # This just makes printing so much easier.
        if self.verbose:
            print(f"Cleaning number {n} complex: {j}")
        if j:
            if n < 1e-3 and n > -1e-3: # if its small
                return "+j0.00"
            if n < 0: # if its negative
                return f"-j{abs(n):.2f}"
            return f"+j{n:.2f}" # else its positive

        # if the number is very small we return 0.00
        if n < 1e-3 and n > -1e-3:
            return "0.00"
        
        return f"{n:.2f}"
