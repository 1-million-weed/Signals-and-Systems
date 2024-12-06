from interface import ThemisInterface
import math

class CartesianToPolar(ThemisInterface):
    """
    This is the class for Cartesian to Polar conversion.
    """
    def get_input_data(self):
        self.x, self.y = map(int, input().split())

    def run(self):
        # transform coordinates
        x, y = self.x, self.y
        r = float(math.sqrt( (x*x) + (y*y) ))
        
        if y >= 0 and r != 0:
            phi = float(math.acos(x/r))
        elif y < 0:
            phi = float(-math.acos(x/r))
        else:
            # r == 0, from x == 0 & y == 0
            raise ValueError("r = 0 : undefined")
        
        # make into doubles
        self.r = round(r,2)
        self.phi = round(phi,2)
    
    def print_output_data(self):
        r, phi = self.r, self.phi
        print(f"{r:.2f} {phi:.2f}")

if __name__ == "__main__":
    CartesianToPolar()
    