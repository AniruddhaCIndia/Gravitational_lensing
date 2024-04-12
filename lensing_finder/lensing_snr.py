import numpy as np

def SNR_calculator(cross, cross_noise, time, s):
  s=int(s)
  snr=[]
  snr_time=[]
  length= len(cross)
  k=int(length/s)
  for j in range(s):
    a=1/(k) * np.sum(cross[int(j*k) : int(j*k+k)])
    b=1/(k) * np.sum(cross_noise[int(j*k) : int(j*k+k)])
    c=np.std(cross_noise[int(j*k) : int(j*k+k)])
    d=(a-b)**2 /c**2
    snr.append(d)
  snr=np.array(snr)
  snr_time=(time[int(k/2):len(time):k]+time[int(k/2)+1:len(time):k])/2
  return snr_time, snr
