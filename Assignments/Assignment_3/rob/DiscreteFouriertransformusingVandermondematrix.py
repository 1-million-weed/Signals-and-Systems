import math

class Discrete_Fourier_transform_using_Vandermonde_matrix:
    def __init__(self) -> None:
        """Initialize the DFT with the input signal."""
        self._signal, self._length_signal = self.readSignal()

    def readSignal(self) -> tuple[list[int], int]:
        """Read the input signal from the user."""
        input_line = input().strip()
        length = int(input_line.split(':')[0])
        signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
        return signal, length
    
    def calcualte(self) -> None:
        """Calculate the DFT using the Vandermonde matrix."""
        self.output_vector = []
        for row in range(self._length_signal):
            sum_real = 0
            sum_j = 0
            for column in range(self._length_signal):
                theta = (2 * math.pi / self._length_signal) * (row * column)
                cos_result = math.cos(-theta)
                sin_result = math.sin(-theta)
                sum_real += cos_result * self._signal[column]
                sum_j += sin_result * self._signal[column]
                
            self.output_vector.append(f'{sum_real:.2f}{"+" if sum_j >= 0 else "-"}j{abs(sum_j):.2f}')
            
    def display(self) -> None:
        """Display the DFT result."""
        for element in self.output_vector:
            print(element)

if __name__ == "__main__":
    dftvm = Discrete_Fourier_transform_using_Vandermonde_matrix()
    dftvm.calcualte()
    dftvm.display()