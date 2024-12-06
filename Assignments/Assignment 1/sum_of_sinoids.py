import cmath

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

class SumOfSinoids(ThemisInterface):
    """
    This is the class for the sum of sinoids.
    """
    def get_input_data(self):
        f, n = map(int, input().split())
        sinoids = []
        for _ in range(n):
            a, phase = map(float, input().split())
            sinoids.append((a, phase))

        self.f, self.sinoids = f, sinoids

    def run(self):
        """
        Calculate the sum of sinoids.
        """

        amp_sum = 0
        for amp, phase in self.sinoids:
            amp_sum += amp * cmath.exp(1j * phase)

        amp = round(abs(amp_sum), 2)
        phase = round(cmath.phase(amp_sum), 2)

        self.amp, self.phase = amp, phase
    
    def print_output_data(self):
        if self.amp == 0:
            print("x(t)=0.00")
        else:
            print(f"x(t)={self.amp:.2f}cos(2*pi*{self.f}*t+{self.phase:.2f})")

if __name__ == "__main__":
    SumOfSinoids()