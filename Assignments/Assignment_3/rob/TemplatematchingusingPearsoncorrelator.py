import math

class Template_matching_using_Pearson_correlator:
    def __init__(self) -> None:
        """Initialize the template and signal."""
        self._length_template, self._template = input().split(": ")
        self._length_signal, self._signal = input().split(": ")
        self._length_template = int(self._length_template)
        self._length_signal = int(self._length_signal)
        self._template = list(map(int, self._template.strip('[]').split(',')))
        self._signal = list(map(int, self._signal.strip('[]').split(',')))

    def calculate(self) -> None:
        """Calculate the sequence of Pearson correlations"""
        results = []
        
        for n in range(self._length_signal - self._length_template + 1):
            signal_window = self._signal[n:n + self._length_template]
            
            numerator1 = self._length_template * sum([signal_window[i] * self._template[i] for i in range(self._length_template)])
            numerator2 = sum(signal_window) * sum(self._template)
            numerator = numerator1 - numerator2
            
            denominator1 = math.sqrt(self._length_template * sum([x**2 for x in signal_window]) - (sum(signal_window)**2))
            denominator2 = math.sqrt(self._length_template * sum([x**2 for x in self._template]) - (sum(self._template)**2))
            denominator = denominator1 * denominator2
            
            if denominator == 0:
                results.append(0.00000)
            else:
                results.append(numerator / denominator)
        
        self.results = results

    def display(self) -> None:
        """Display the results."""
        formatted_results = [f"{result:.5f}" for result in self.results]
        print(f"{len(formatted_results)}: [{', '.join(formatted_results)}]")

if __name__ == "__main__":
    tmpc = Template_matching_using_Pearson_correlator()
    tmpc.calculate()
    tmpc.display()
