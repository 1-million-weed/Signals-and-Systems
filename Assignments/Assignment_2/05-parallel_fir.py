"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: 
    This class is used to implement a cascade FIR filter.
    The class is a subclass of the ThemisInterface class.
    The class finds the frequency response of a system.
"""
import math
from interface import ThemisInterface

class FrequencyResponse(ThemisInterface):

    def get_input_data(self):
        """Get input data from Themis."""	
        self.impulse_response, self.n_impulse_response = self.readSignal()
        self.A, self.w, self.phi = self.readInputSignal()

    def real_and_imaginary(self, impulse_response: list[int], w: int) -> tuple[float, float]:
        """
        Compute the real and imaginary parts of the frequency response.

        Args:
            impulse_response (list of ints): The impulse response of the system.
            w (int): The radian frequency.
        
        Returns:
            tuple of floats: The real and imaginary parts of the frequency response.
        """
        # Initialize the real and imaginary parts of the frequency response
        real = 0.0
        imaginary = 0.0

        # Iterate over the impulse response
        for i in range(len(impulse_response)):
            # Compute the frequency response of the real and imaginary parts
            real += impulse_response[i] * math.cos(w * i)
            imaginary += impulse_response[i] * math.sin(w * i) # so we dont use j to keep it real
        
        return real, imaginary

    def compute_amplitude(self, impulse_response: list[int], A: int, w: int) -> float:
        """
        Compute the amplitude of the frequency response.

        Args:
            impulse_response (list of ints): The impulse response of the system.
            A (int): The amplitude of signal x.
            w (int): The radian frequency.
            phi (int): The phase.
        
        Returns:
            float: The amplitude of the frequency response.
        """
        # Compute the real and imaginary parts of the frequency response
        real, imaginary = self.real_and_imaginary(impulse_response, w)

        # Compute the magnitude of the frequency response
        magnitude = math.sqrt(real**2 + imaginary**2)

        # Scale the amplitude with the magnitude and return the result
        return A * magnitude
    
    def compute_phase(self, impulse_response: list[int], w: float, phi: float) -> float:
        """
        Compute the phase of the frequency response.

        Args:
            impulse_response (list of ints): The impulse response of the system.
            A (int): The amplitude of signal x.
            w (int): The radian frequency.
            phi (int): The phase.
        
        Returns:
            float: The phase of the frequency response.
        """
        # Compute the real and imaginary parts of the frequency response
        real, imaginary = self.real_and_imaginary(impulse_response, w)

        # Compute the phase change of the frequency response
        # atan2 correctly handles signs and returns the phase in range [-pi, pi]
        phase = -math.atan2(imaginary, real) 

        # Apply the phase change to the original phase
        phase += phi

        # Normalize the phase to the range [-pi, pi]
        while phase > math.pi:
            phase -= 2 * math.pi

        # Return the result
        return phase

    def run(self):
        """Run the specified fuction."""
        # Compute the amplitude of the frequency response
        self.amplitude = self.compute_amplitude(self.impulse_response, self.A, self.w)
        # Compute the phase of the frequency response
        self.phase = self.compute_phase(self.impulse_response, self.w, self.phi)

    def print_output_data(self):
        """Print the output data."""
        # round values to 2 decimal places
        amp = round(self.amplitude, 2)
        phase = round(self.phase, 2)
        w = round(self.w, 2)
        # check if amplitude is 0
        if round(self.amplitude, 2) == 0:
            print("y[n]=0.00")
        else:
            # funky sign handling
            if phase >= 0:
                phase = abs(phase)
                print(f"y[n]={amp:.2f}cos({w:.2f}*n+{phase:.2f})")
            else:
                phase = abs(phase)
                print(f"y[n]={amp:.2f}cos({w:.2f}*n-{phase:.2f})")

if __name__ == "__main__":
    FrequencyResponse()