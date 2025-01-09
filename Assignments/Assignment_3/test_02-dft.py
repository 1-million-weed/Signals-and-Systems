
import unittest
from dft import DFTVandermonde
import numpy as np

class TestDFTVandermonde(unittest.TestCase):
    def test_build_vandermonde(self):
        print("test_build_vandermonde")
        dft = DFTVandermonde(themis=False)
        W = dft.build_vandermonde(4)
        self.assertEqual(len(W), 4)
        self.assertEqual(len(W[0]), 4)

    def test_dot_product(self):
        print("test_dot_product")
        dft = DFTVandermonde(themis=False) # ThemisInterface atrubute
        x = [1, 2, 3, 4]
        W = [
            [1,1,1,1],
            [1,2,4,8],
            [1,3,9,27],
            [1,4,16,64]
        ]
        result = dft.dot_product(x, W)
        solution = list(map(int, np.dot(W, x))) # numpy dot product
        self.assertEqual(result, solution)

    def test_vandermonde_dot_product(self):
        print("test_vandermonde_dot_product")
        dft = DFTVandermonde(themis=False)
        x= [1, 2, 3, 4]
        W = dft.build_vandermonde(len(x))
        result = dft.dot_product(x, W)
        solution = list(map(int, np.dot(W, x)))
        self.assertEqual(result, solution)

if __name__ == "__main__":
    unittest.main()