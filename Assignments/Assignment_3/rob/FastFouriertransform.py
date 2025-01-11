import math
 
class Fast_Fourier_transform():
    def __init__(self) -> None:
        """Initialize the FFT with the input signal."""
        self._signal, self._length_signal = self.readSignal()
        if not self.is_power_of_2(self._length_signal):
            new_lenght = self.next_power_of_2(self._length_signal)
            for _ in range(new_lenght - self._length_signal):
                self._signal.append(0)
                self._length_signal = new_lenght

    def is_power_of_2(self, n: int) -> bool:
        """Check if n is a power of 2."""
        return n > 0 and (n & (n - 1)) == 0

    def next_power_of_2(self, n: int) -> int:
        """Find the next power of 2 greater than or equal to n."""
        power = 1
        while power < n:
            power *= 2
        return power

    def readSignal(self) -> tuple[list[int], int]:
        """Read the input signal from the user."""
        input_line = input().strip()
        length = int(input_line.split(':')[0])
        signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
        return signal, length
    
    def calculate(self) -> None:
        """Calculate the FFT of the signal."""
        self._results = self._calculate_recursive(self._signal)

    def _calculate_recursive(self, signal: list[int]) -> list[complex]:
        """Recursively calculate the FFT."""
        n = len(signal)
        if n <= 1:
            return signal
        even = self._calculate_recursive(signal[0::2])
        odd = self._calculate_recursive(signal[1::2])
        y = [0] * n
        theta = -2 * math.pi /n
        for x in range(n //2):
            cos_result = math.cos(theta * x)
            sin_result = math.sin(theta * x)
            omega = complex(cos_result, sin_result)


            y[x] = even[x] + omega * odd[x]
            y[x + n //2] = even[x] - omega * odd[x]
        return y
    
    def display(self) -> None:
        """Display the FFT results."""
        for result in self._results:
            real_part = f"{result.real:.2f}"
            imag_part = f"{abs(result.imag):.2f}"
            sign = '+' if result.imag >= 0 else '-'
            formatted_result = f"{real_part}{sign}j{imag_part}"
            print(formatted_result)


if __name__ == "__main__":
    fft = Fast_Fourier_transform()
    fft.calculate()
    fft.display()
