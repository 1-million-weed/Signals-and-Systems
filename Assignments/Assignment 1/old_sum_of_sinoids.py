from itertools import product

def read_frequencies():
    """Reads integer frequencies until a '0' is encountered."""
    freqs = []
    while True:
        line = input().strip()
        if not line:
            continue
        f = int(line)
        if f == 0:
            break
        freqs.append(f)
    return freqs

def generate_spectrum(freqs):
    """
    Given a list of frequencies, generate all possible frequency components 
    appearing in the product of cosines.

    The product of N cosines, each with frequency f_i, can be expanded into 
    a sum of cosines with frequencies formed by all possible sign combinations 
    of f_i. That is, for each subset of frequencies, we add or subtract them 
    together to form a resulting frequency.

    Example:
    cos(2πf1t)*cos(2πf2t) 
    = [cos(2π(f1+f2)t) + cos(2π(f1−f2)t)] / 2

    For multiple frequencies, the pattern extends similarly, leading to 
    frequencies that are all possible sums and differences of the input frequencies.
    """
    if not freqs:
        return []

    # For each frequency fi, we can choose a sign +1 or -1.
    # The final set of frequencies = all sums of the form sum(sign_i * f_i)
    # with sign_i in {+1, -1}.
    # We only consider nonnegative frequencies in the final output (take absolute values).
    spectrum = set()
    for signs in product([-1, 1], repeat=len(freqs)):
        val = sum(s * f for s, f in zip(signs, freqs))
        # Only non-negative frequencies
        if val >= 0:
            spectrum.add(val)

    return sorted(spectrum)

def main():
    freqs = read_frequencies()
    result = generate_spectrum(freqs)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()