from scipy.integrate import simpson
import numpy as np

def cross_correlator(array1, array2, time, steps, midpoint=True, specific_time=None):
    """
    Computes the cross-correlation of two input arrays over specified time intervals.
    
    Parameters:
    -----------
    array1 : numpy.ndarray
        First input array of time-series data.
    array2 : numpy.ndarray
        Second input array of time-series data.
    time : numpy.ndarray
        Time array corresponding to the data points.
    steps : int
        Number of segments to divide the data into for cross-correlation calculation.
    midpoint : bool, optional (default=True)
        If True, returns the midpoint of each time segment; otherwise, returns the last point of each segment.
    specific_time : float, optional (default=None)
        If provided, returns the cross-correlation value closest to this time.
    
    Returns:
    --------
    time_of_cross_corr : numpy.ndarray
        Time values corresponding to the computed cross-correlation values.
    data_cross_corr : numpy.ndarray
        Computed cross-correlation values.
    specific_value : float (optional)
        If `specific_time` is given, returns the cross-correlation value at the closest matching time.
    
    Raises:
    -------
    ValueError:
        If `array1` and `array2` have different lengths.
    
    Notes:
    -------
    - The function segments the input arrays into `steps` chunks and computes the cross-correlation in each.
    - Uses Simpson's rule for numerical integration over each segment.
    - If `specific_time` is provided, the function finds the closest available time and returns the corresponding value.
    """
    N1 = int(len(array1))
    N2 = int(len(array2))
    s = int(steps)
    p = int(N1 / s)
    data_cross_corr = []
    
    if N1 != N2:
        raise ValueError("Input arrays must have the same length.")
    
    if specific_time is not None:
        idx = (np.abs(time - specific_time)).argmin()
        if time[idx] != specific_time:
            print(f"Closest time found: {time[idx]} (requested: {specific_time})")
        specific_chunk = idx // p 
         
    for i in range(s):
        result = (1 / (p * (time[1] - time[0]))
            * simpson(y=array1[i*p : i*p + p] * array2[i*p : i*p + p],
                      x=time[i*p : i*p + p]))
        data_cross_corr.append(result)
    
    data_cross_corr = np.array(data_cross_corr)
    if midpoint:
        time_of_cross_corr = np.array((time[int(p / 2) - 1 : N1 : p] + time[int(p / 2) : N1 : p]) / 2)
    else:
        time_of_cross_corr = np.array(time[int(p-1) : N1 : p])
    
    if specific_time is not None:
        return time_of_cross_corr, data_cross_corr, data_cross_corr[specific_chunk]

    return time_of_cross_corr, data_cross_corr
