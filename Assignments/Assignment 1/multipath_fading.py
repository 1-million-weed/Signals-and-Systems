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

class MultipathFading(ThemisInterface):
    def get_input_data(self):
        self.dr, self.dt, self.x = map(int, input().split())

    def run(self):
        #init frequency & light speeeeeed
        c = 3 * 10**8
        f = 150 * 10**6
        
        #find distance 1 & 2
        dist_reciever = self.x
        dist_reflector = math.sqrt(self.dr**2 + self.dt**2) + math.sqrt((self.x - self.dr)**2 + self.dt**2)
        
        #calculate time delay
        time_direct = dist_reciever/c
        time_indirect = dist_reflector/c
        delta_time = abs(time_direct - time_indirect)
        
        #calculate phase difference
        phase_diff = 2 * math.pi * f * delta_time
        
        #calculate reflected amplitude
        self.reflected_amp = math.cos(phase_diff)

        #compute the amplitude
        amplitude = abs(2 * math.cos(phase_diff/2))
        
        self.aplitute = round(amplitude, 2)

    def print_output_data(self):
        print(f"{self.aplitute:.2f}")

if __name__ == "__main__":
    MultipathFading()