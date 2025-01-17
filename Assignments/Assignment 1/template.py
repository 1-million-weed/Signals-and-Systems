import math, cmath, itertools

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

    r = √(x2 + y2) (Length) (A.5a) \n
    θ = arctan(y/x) (Direction) (A.5b) \n

    z = re^(jθ) = |z|e^(j arg z)
    where |z| = r = √(x2 + y2) is called the magnitude of the vector 
    and arg z = θ is its phase in radians (not degrees)

    TODO: However, we generally specify the principal value of the angle 
    so that −180◦ < θ ≤ 180◦. This requires that integer multiples 
    of 360◦ be subtracted from or added to the angle until the result 
    is between −180◦ and +180◦. Thus, the vector 3∠−80◦ is the principal 
    value of 3∠280◦.
    
    Args:
        x (float) x-coordinate.
        y (float) y-coordinate.

    Returns:
        r (float): radius
        phi (float): angle in radians
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

    x = r cos θ (A.3a) \n
    y = r sin θ (A.3b) \n
    z = r cos θ + j r sin θ (A.4)

    Euler’s Formula: \n
    e^(jθ) = cos θ + j sin θ (A.7)

    Args:
        r (float): The radius.
        phi (float): The angle in radians.

    Returns:
        tuple: A tuple containing the x and y coordinates.
    """
    # transform coordinates
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    
    # make into doubles
    x = round(x,2)
    y = round(y,2)
    
    #return cartesian
    return x, y

def sum_of_sinoids() -> str:
    """
    The sum of n sinusoids with the same frequency.

    Args:
        f (int): The frequency of the sinusoids.
        n (int): The number of sinusoids.
        a_phi (list): A list of amplitudes and phases.
    return:
        str: The resulting sinusoid equation.
    """
    # TODO: change from input to function arguments
    # input: 42 2 
    # 1 1.047198 
    # 1 0.523599 
    # output: x(t)=1.93cos(2*pi*42*t+0.79)
    # get the frequency and number of sinoids
    f, n = map(int, input().split())

    a_sum = 0

    # sum of phasors
    for _ in range(n):
        # get the amplitude and phase
        a, phase = map(float, input().split())
        a_sum += a * cmath.exp(1j * phase)

    # polar form
    amp = round(abs(a_sum), 2)
    phase = round(cmath.phase(a_sum), 2)

    # output
    if a == 0:
        return "x(t)=0.00"
    else:
        return "x(t)={}cos(2*pi*{}*{}*t+{})".format(amp, f, n, phase)

def aliasing():
    """
    The frequency (in Hz) of the reconstructed sinusoid after a sinusoid
    with frequency f0 has been sampled with frequency fs.

    Args:
        f0 (int): The frequency of the sinusoid.
        fs (int): The sampling frequency.
    return:
        int: The frequency of the reconstructed sinusoid.
    """
    # TODO: change from input to function arguments
    # Input: 
    # f0 & fs
    f0, fs = map(int, input().split())
    
    # remainder
    f = f0 % fs

    # check if f is greater than fs/2
    if f > fs/2:
        f = int(fs - f)
    else:
        f = int(f)

    # Output:
    # f integer
    print(f)

def products_of_sinoids():
    """
    The product of n sinusoids.

    Args:
        f (list): A list frequencies of the sinusoids.
    return:
        str: A list of all the non-negative frequencies (in Hz) in the spectrum.
    """
    # So for this question we have to add all possible configurations the frequencies together.
    # For N number of frequencies we have 2^N possible configurations
    # We can use the itertools.product to get all the possible configurations
    # and then we can add them together and store them in a set to only allow distinct values
    # Finally we sort the set and return the values

    # list to store the frequencies
    frequencies = []
    # get the frequency
    while True:
        freq = int(input())
        if freq == 0:
            break
        frequencies.append(freq)

    # next we calculate all the possible combination of frequencies
    # and store them in a set to only allow distinct values
    freq_set = set()

    # we first get a list of all the sign combinations
    sign_combinations = itertools.product([-1, 1], repeat=len(frequencies))
    
    # then loop over all the sign combinations
    for combi in sign_combinations:
        # calculate the result frequency of that sign combination
        result_frequency = sum(sign * freq for sign, freq in zip(combi, frequencies))
        if result_frequency >= 0:
            freq_set.add(result_frequency)

    # we sort the set and return the values
    freq_set = sorted(list(freq_set))
    for freq in freq_set:
        print(freq)

products_of_sinoids()


def nyquist():
    """
    The minimum sampling frequency (in Hz) required to avoid aliasing.

    Args:
        f0 (int): The frequency of the sinusoid.
    return:
        int: The minimum sampling frequency.
    """

def nyquist_rate()->int:
    """
    !!! This does not work
    The minimum sampling frequency (in Hz) required to avoid aliasing.
    """
    # get input list of frequencies
    freqs = []
    while True:
        freq = int(input("Enter a frequency (0 to stop): ").strip())
        if freq == 0:
            break
        freqs.append(freq)
        
    # make list of uniques
    all_freqs = set(freqs)
    
    # calculate sums and differences
    for i in range(len(freqs)):
        for j in range(i + 1, len(freqs)):
            f1, f2 = freqs[i], freqs[j]
            diff = abs(f1 - f2)  # Difference frequency
            if diff > 0:  # Ignore zero differences
                all_freqs.add(diff)
            all_freqs.add(f1 + f2)  # Sum frequency
    
    # find the maximum frequency
    max_freq = max(all_freqs)
    
    # find and return nyquist rate
    nyquist_rate = 2 * max_freq
    return nyquist_rate

def reflected_amplitude(dr,dt,x)->float:
    #init frequency & light speeeeeed
    c = 3 * 10**8
    f = 150 * 10**6
    
    #find distance 1 & 2
    dist_reciever = x
    dist_reflector = math.sqrt(dr**2 + dt**2) + math.sqrt((x - dr)**2 + dt**2)
    
    #calculate time delay
    time_direct = dist_reciever/c
    time_indirect = dist_reflector/c
    delta_time = abs(time_direct - time_indirect)
    
    #calculate phase difference
    delta_phi = 2 * math.pi * f * delta_time
    
    #compute the amplitude
    amplitude = abs(2 * math.cos(delta_phi/2))
    
    return round(amplitude, 2)
