import math

def get_input_data():
    input_1, input_2, input_3 = map(int, input().split())
    return input_1, input_2, input_3

def print_output_data(output_data):
    print("{:.2f}".format(output_data))
    pass

def print_output_list(output_list):
    for output_data in output_list:
        print(output_data)
    pass


def cartesian_to_polar(x,y) -> tuple:
    """
    Convert cartesian coordinates to polar coordinates.
    
    Args:
        - x (float) : x-coordinate
        - y (float) : y-coordinate

    Returns:
        - r (float) : radius
    - phi (float) : angle in radians
    """
    # transform coordinates
    r = float(math.sqrt( (x*x) + (y*y) ))
    
    if y >= 0 and r != 0:
        phi = float(math.acos(x/r))
    elif y < 0:
        phi = float(-math.acos(x/r))
    else:
        # r == 0, from x == 0 & y == 0
        raise ValueError("r = 0 : undefined")
    
    # make into doubles
    r = round(phi,2)
    phi = round(phi,2)
    
    # return polar
    return r, phi

def polar_to_cartesian(r, phi) -> tuple:
    """
    Convert polar coordinates to cartesian coordinates.

    Args:
    - r (float) : radius
    - phi (float) : angle in radians

    Returns:
    - x (float) : x-coordinate
    - y (float) : y-coordinate
    """
    # transform coordinates
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    
    # make into doubles
    x = round(x,2)
    y = round(y,2)
    
    #return cartesian
    return x, y