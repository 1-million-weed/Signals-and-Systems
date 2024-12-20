"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description: 
    This class is used to implement a cascade FIR filter.
    The class is a subclass of the ThemisInterface class.
"""
import math, cmath
from interface import ThemisInterface

class FrequencyResponse(ThemisInterface):

    def get_input_data(self):
        """Get input data from Themis."""	
        self.impulse_response, self.n_impulse_response = self.readSignal()
        self.A, self.w, self.phi = self.readInputSignal()

    def FIR(self, kernel: list[int], signal: list[int]) -> list[int]:
        """
        Compute y[n] from x[n] and h[n]

        Args:
            kernel (list of ints): The kernel to apply to the signal.
            signal (list of ints): The signal to apply the kernel to.
        
        Returns:
            list of ints: The output signal.

        NOTE:
            This function is taken from the FIRFilter class.

            I have a system of running it with Themis and changing that 
            system to be able to create an instance of the FIRFilter class
            and run FIR filter is not in the books for tonight.
        """
        # Length of the output signal
        output_length = len(signal) + len(kernel) - 1
        # Initialize the output signal
        output = [0] * output_length
        # Iterate over the "output" signal
        for i in range(output_length):
            result = 0
            for j in range(len(kernel)):
                signal_index = i - j
                # Stay in bounds of the signal
                if 0 <= signal_index < len(signal):
                    # Multiply the kernel with the signal
                    result += signal[signal_index] * kernel[j]
            # Set that value in the output signal
            output[i] = result
        return output

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
        phase = math.atan2(imaginary, real) 

        # Apply the phase change to the original phase
        phase -= phi

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
        print(self.amplitude)
        print(self.phase)

    def print_output_data(self):
        """Print the output data."""
        pass

if __name__ == "__main__":
    FrequencyResponse()