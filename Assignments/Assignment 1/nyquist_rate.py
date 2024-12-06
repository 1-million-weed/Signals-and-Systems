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

class NyquistRate(ThemisInterface):
    def get_input_data(self):
        # get input list of frequencies
        freqs = []
        while True:
            freq = int(input().strip())
            if freq == 0:
                break
            freqs.append(freq)

        self.freqs = freqs

    def run(self):
        freqs = self.freqs

        # sum the frequencies
        freq_sum = sum(freqs)

        # find the nyquist rate
        self.nyquist_rate = 2 * freq_sum

    def print_output_data(self):
        print(self.nyquist_rate)

if __name__ == "__main__":
    NyquistRate()