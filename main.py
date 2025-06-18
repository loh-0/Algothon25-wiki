import numpy as np

def getMyPosition(priceMat: np.ndarray) -> np.ndarray:
    """
    Required function to return daily positions for each instrument.

    Parameters:
    -----------
    priceMat : np.ndarray
        Array of shape (50, T) with prices for each instrument up to day T.

    Returns:
    --------
    np.ndarray
        Integer vector of length 50 with desired positions for each instrument.
    """
    nInst = priceMat.shape[0]
    return np.zeros(nInst, dtype=int)  # Start with all zero positions
