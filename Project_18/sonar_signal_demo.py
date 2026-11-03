import numpy as np, matplotlib.pyplot as plt
from pathlib import Path
out=Path(__file__).resolve().parent/'results'; out.mkdir(exist_ok=True)
fs=12000; t=np.arange(0,1,1/fs); rng=np.random.default_rng(18)
signals=[]
for label,freq in [('class_A',1200),('class_B',2800)]:
    x=np.sin(2*np.pi*freq*t)*np.exp(-2*t)+0.15*rng.normal(size=len(t))
    signals.append((label,x))
fig,ax=plt.subplots(2,1,figsize=(9,6))
for label,x in signals:
    ax[0].plot(t[:1000],x[:1000],label=label)
    spec=np.abs(np.fft.rfft(x)); f=np.fft.rfftfreq(len(x),1/fs); ax[1].plot(f,spec,label=label)
ax[0].set_title('Synthetic sonar-like echo waveform'); ax[0].set_xlabel('Time (s)'); ax[0].legend()
ax[1].set_title('FFT magnitude spectrum'); ax[1].set_xlabel('Frequency (Hz)'); ax[1].legend()
fig.tight_layout(); fig.savefig(out/'sonar_waveform_fft.png',dpi=150)
print('Saved synthetic waveform and FFT plot to',out)
