import numpy as np

def SNR_calculator(cross, cross_noise, time, s):
    """
    Computes the signal-to-noise ratio (SNR) over segmented time intervals.
    
    Parameters:
    -----------
    cross : numpy.ndarray
        Array containing the cross-correlation signal values.
    cross_noise : numpy.ndarray
        Array containing the noise values corresponding to the cross-correlation signal.
    time : numpy.ndarray
        Time array corresponding to the data points.
    s : int
        Number of segments into which the data is divided for SNR calculation.
    
    Returns:
    --------
    snr_time : numpy.ndarray
        Time values corresponding to the computed SNR values.
    snr : numpy.ndarray
        Computed signal-to-noise ratio (SNR) values.
    
    Notes:
    -------
    - The function divides the input data into `s` segments.
    - It calculates the mean signal and noise over each segment.
    - The SNR is computed as the squared difference between the mean signal and mean noise, normalized by the noise variance.
    - The time values are assigned based on the midpoint of each segment.
    """
    s = int(s)
    snr = []
    length = len(cross)
    k = int(length / s)
    
    for j in range(s):
        a = 1 / k * np.sum(cross[int(j * k) : int(j * k + k)])
        b = 1 / k * np.sum(cross_noise[int(j * k) : int(j * k + k)])
        c = np.std(cross_noise[int(j * k) : int(j * k + k)])
        d = (a - b) ** 2 / c ** 2
        snr.append(d)
    
    snr = np.array(snr)
    snr_time = (time[int(k / 2) : len(time) : k] + time[int(k / 2) + 1 : len(time) : k]) / 2
    
    return snr_time, snr
