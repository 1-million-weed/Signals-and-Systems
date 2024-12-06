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

class Aliasing(ThemisInterface):
    def get_input_data(self):
        # Input: 
        # f0 & fs
        self.f0, self.fs = map(int, input().split())

    def run(self):
        f0, fs = self.f0, self.fs

        # remainder
        f = f0 % fs

        # check if f is greater than fs/2
        if f > fs/2:
            f = int(fs - f)
        else:
            f = int(f)

        self.f = f

    def print_output_data(self):
        # Output:
        # f integer
        print(self.f)

if __name__ == "__main__":
    Aliasing()