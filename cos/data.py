import numpy as np

def generate_training_data(num_samples=1000, N=3):
    """Generate synthetic EEG training data"""
    X_f_k, y_f_k, X_g, y_g = [], [], [], []
    C_old = 0.0
    Y = [0.0] * N
    for t in range(num_samples):
        for k in range(N):
            input_val = np.clip(np.sin(2 * np.pi * 10 * t / 1000) + np.random.normal(0, 0.1), -1, 1)
            prev_yank = Y[k - 1] if k > 0 else C_old
            Y_k = prev_yank + input_val
            X_f_k.append([prev_yank, input_val])
            y_f_k.append(Y_k)
            Y[k] = Y_k
        Y_N = Y[N - 1]
        C_new = 0.5 * Y_N + 0.5 * C_old
        X_g.append([Y_N, C_old])
        y_g.append(C_new)
        C_old = C_new
    return np.array(X_f_k), np.array(y_f_k), np.array(X_g), np.array(y_g)
