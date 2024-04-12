from scipy.integrate import simpson
import numpy as np

def cross_correlator(array1, array2, time, steps): #Input array 1, array 2 and no. of chops
  N1 = int(len(array1))
  N2 = int(len(array2))
  s = int(steps)
  p = int(N1/s)
  data_cross_corr=[]

  if N1==N2:
    for i in range(s):
      result= 1/( p*(time[1]-time[0]) ) *simpson( array1[i*p:i*p+p]*array2[i*p:i*p+p] , time[i*p:i*p+p] )
      data_cross_corr.append(result)
    data_cross_corr = np.array(data_cross_corr)
    time_of_cross_corr = np.array((time[int(p/2):N1:p] +time[int(p/2)+1:N1:p])/2)
    return time_of_cross_corr, data_cross_corr

  else:
    print("Error! The arrays are not equal in length, you may use hp.resize(length)")
