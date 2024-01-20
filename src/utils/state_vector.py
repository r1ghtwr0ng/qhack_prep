import numpy as np

# Return the amplitude squared of a complex vector
def amplitude_squared(c):
    return (c.conjugate() @ c).real