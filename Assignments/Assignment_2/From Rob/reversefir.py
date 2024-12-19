class InverseFIRFilter():
    """Class to calculate the inverse FIR filter"""
    def __init__(self):
        """Constructor to initialize the inverse FIR filter"""
        self.get_input_data()
    
    def get_input_data(self) -> None:
        """Method to get the input data"""
        input_1 = input().split(": ")
        self.len_1 = int(input_1[0])
        self.kernel = [int(x) for x in input_1[1].strip(" []").split(",")]
        input_2 = input().split(": ")
        self.len_2 = int(input_2[0])
        self.result_signal = list([int(x) for x in input_2[1].strip(" []").split(",")])
    
    def calculate(self) -> list[int] | None:
        """Method to calculate the discrete signal"""
        length = abs(self.len_1 - self.len_2) + 1 # calculate the length of the discrete signal
        discrete_signal_1 = [0] * (length) # reconstructed signal
        for i in range(length):
            current = self.result_signal[i]
            for j in range(1, min(i + 1, self.len_1)):
                current -= self.kernel[j] * discrete_signal_1[i - j] # calculate the current value
            discrete_signal_1[i] = current // self.kernel[0] # set the value
        
        # Check if the calculated signal is correct
        # If correct, return the signal
        check = self.check(discrete_signal_1)
        if check == self.result_signal:
            return discrete_signal_1
        else:
            return None
        
    
    def check(self, discrete_signal: list[int]) -> list[int]:
        """Method to check if the calculated signal is correct"""
        result_signal: list[int] = []
        for i in range(self.len_1 + len(discrete_signal) - 1):
            result_signal.append(0)
            for j in range(self.len_1):
                if i - j >= 0 and i - j < len(discrete_signal):
                    result_signal[i] += self.kernel[j] * discrete_signal[i - j]
        return result_signal
        
        
    def display(self) -> None:
        """Method to display the discrete signal"""
        discrete_signal = self.calculate()
        if not discrete_signal:
            print("NO FIR")
        else:
            length = len(discrete_signal)
            print(str(length) + ": " + str(discrete_signal))

if __name__ == "__main__":
    inverse_fir_filter = InverseFIRFilter()
    inverse_fir_filter.display()
    pass
