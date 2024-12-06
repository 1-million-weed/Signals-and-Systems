import itertools

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

class ProductsOfSinoids(ThemisInterface):

    def get_input_data(self):
        # list to store the frequencies
        frequencies = []
        # get the frequency
        while True:
            freq = int(input())
            if freq == 0:
                break
            frequencies.append(freq)

        self.frequencies = frequencies

    def run(self):
        frequencies = self.frequencies
        # next we calculate all the possible combination of frequencies
        # and store them in a set to only allow distinct values
        freq_set = set()

        # we first get a list of all the sign combinations
        sign_combinations = itertools.product([-1, 1], repeat=len(frequencies))
        
        # then loop over all the sign combinations
        for combi in sign_combinations:
            # calculate the result frequency of that sign combination
            result_frequency = sum(sign * freq for sign, freq in zip(combi, frequencies))
            if result_frequency >= 0:
                freq_set.add(result_frequency)

        # we sort the set and return the values
        freq_set = sorted(list(freq_set))

        self.frec_set = freq_set

    def print_output_data(self):
        for freq in self.frec_set:
            print(freq)

if __name__ == "__main__":
    ProductsOfSinoids()