import math

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

class PolarToCartesian(ThemisInterface):
    """
    This is the class for Polar to Cartesian conversion.
    """

    def get_input_data(self):
        self.r, self.phi = map(float, input().split())

    def run(self):
        """
        Convert polar coordinates to cartesian coordinates.

        Equations: \n
        x = r cos(θ) \n
        y = r sin(θ) \n
        """
        # transform coordinates
        r, phi = self.r, self.phi
        x = r*math.cos(phi)
        y = r*math.sin(phi)
        
        # make into doubles
        self.x = round(x,2)
        self.y = round(y,2)

    def print_output_data(self):
        print(f"{self.x:.2f} {self.y:.2f}")

if __name__ == "__main__":
    PolarToCartesian()