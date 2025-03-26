from scipy.integrate import simpson

def cross_correlator(array1, array2, time, steps, midpoint=True, specific_time=None):
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
