import numpy as np
from ..utils.operations import amplitude_squared
    
def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.
    
    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.
        
    Returns:
        array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """

    # Create a normalized state vector psi based on alpha and beta
    psi = np.array([alpha, beta])
    norm = np.sqrt(1/amplitude_squared(psi))

    # Return the normalized vector
    return norm * psi