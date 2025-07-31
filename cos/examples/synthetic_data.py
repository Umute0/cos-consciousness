from cos.data import generate_training_data
import numpy as np

# Generate synthetic EEG data
X_f_k, y_f_k, X_g, y_g = generate_training_data(num_samples=1000, N=3)
np.savetxt("data/synthetic_eeg.csv", X_f_k, delimiter=",", header="prev_yank,input")
print("Synthetic EEG data saved to data/synthetic_eeg.csv")
