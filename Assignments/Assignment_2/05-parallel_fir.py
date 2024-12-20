"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: 
    This class is used to implement a FIR filter.
    The class is a subclass of the ThemisInterface class.
    The class finds the frequency response of a system with 
    two inputs.
"""
import math
from interface import ThemisInterface

class ParallelFIR(ThemisInterface):
    """A class used to implement a parallel FIR filter."""

    def get_input_data(self):
        """Get input data from Themis."""	
        self.h1, self.n_h1 = self.readSignal()
        self.h2, self.n_h2 = self.readSignal()
        self.A, self.w, self.phi = self.readInputSignal()
        
        self.verbose = False

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
        # Compute the amplitude and phase of the first frequency response
        h1_amp = self.compute_amplitude(self.h1, self.A, self.w)
        h1_phase = self.compute_phase(self.h1, self.w, self.phi)
        # Compute the amplitude and phase of the second frequency response
        h2_amp = self.compute_amplitude(self.h2, self.A, self.w)
        h2_phase = self.compute_phase(self.h2, self.w, self.phi)

        # Convert amplitude and phase to real and imaginary parts
        h1_real = h1_amp * math.cos(h1_phase)
        h1_imaginary = h1_amp * math.sin(h1_phase)
        h2_real = h2_amp * math.cos(h2_phase)
        h2_imaginary = h2_amp * math.sin(h2_phase)

        # Combine the real and imaginary parts
        real = h1_real + h2_real
        imaginary = h1_imaginary + h2_imaginary

        # Combine resulting amplitude and phase
        self.amplitude = math.sqrt(real**2 + imaginary**2)
        self.phase = math.atan2(imaginary, real)

        if self.verbose:
            # Debug prints
            print(f"h1 amp: {h1_amp}")
            print(f"h1 phase: {h1_phase}")
            print(f"h2 amp: {h2_amp}")
            print(f"h2 phase: {h2_phase}")
            print(f"total real: {real}")
            print(f"total imag: {imaginary}")

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
    ParallelFIR()