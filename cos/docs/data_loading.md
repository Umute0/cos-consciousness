# Loading Real EEG Data

Use MNE-Python to load real EEG data (e.g., PhysioNet):

```python
import mne
def load_eeg(file_path):
    raw = mne.io.read_raw_edf(file_path, preload=True)
    data, times = raw.get_data(picks=['C3'], return_times=True)
    return np.clip(data[0], -1, 1)

Download EEG data from PhysioNet.
