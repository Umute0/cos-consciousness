import json
import numpy as np
import tensorflow as tf
from datetime import datetime

class COSSimulator:
    """COS v1.0: Consciousness Simulation Protocol"""
    def __init__(self, N=3, agent_ids=["AI_001", "AI_002"], num_time_steps=100):
        self.N = N
        self.agent_ids = agent_ids
        self.num_time_steps = num_time_steps
        self.f_k_models = [self._create_f_k_model() for _ in range(N)]
        self.g_model = self._create_g_model()
        self.C_old = 0.0
        self.history = []

    def _create_f_k_model(self):
        """MLP for f_k function"""
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(32, activation='relu', input_shape=(2,)),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        return model

    def _create_g_model(self):
        """RNN for g function"""
        model = tf.keras.Sequential([
            tf.keras.layers.SimpleRNN(32, activation='tanh', input_shape=(None, 2)),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        return model

    def train_models(self, X_f_k, y_f_k, X_g, y_g, epochs=50, batch_size=32):
        """Train f_k and g models"""
        for i, model in enumerate(self.f_k_models):
            early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
            model.fit(X_f_k, y_f_k, epochs=epochs, batch_size=batch_size, 
                      validation_split=0.2, callbacks=[early_stopping], verbose=1)
            print(f"f_k model {i+1} trained.")
        X_g_reshaped = X_g.reshape(-1, 1, 2)
        early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
        self.g_model.fit(X_g_reshaped, y_g, epochs=epochs, batch_size=batch_size, 
                         validation_split=0.2, callbacks=[early_stopping], verbose=1)
        print("g model trained.")

    def external_input(self, k, t):
        """Synthetic EEG signal (10 Hz alpha wave + noise)"""
        return np.clip(np.sin(2 * np.pi * 10 * t / 1000) + np.random.normal(0, 0.1), -1, 1)

    def create_message(self, agent_id, t, Y, C_old, C_new, eeg_input):
        """Generate JSON message"""
        return {
            "protocol": "COS-v1.0",
            "timestamp": datetime.now().isoformat(),
            "agent_id": agent_id,
            "time_step": t,
            "layer_count": len(Y),
            "layers": [{"layer_id": k + 1, "yank": float(Y[k])} for k in range(len(Y))],
            "central_point": {"C_old": float(C_old), "C_new": float(C_new)},
            "eeg_input": float(eeg_input)
        }

    def agent_update(self, agent_id, t, C_old):
        """Update agent layers"""
        Y = [0.0] * self.N
        eeg_input = self.external_input(1, t)
        for k in range(self.N):
            input_val = self.external_input(k + 1, t)
            prev_yank = Y[k - 1] if k > 0 else C_old
            Y[k] = self.f_k_models[k].predict(np.array([[prev_yank, input_val]]), verbose=0)[0][0]
        return Y, Y[self.N - 1], eeg_input

    def central_server_update(self, Y_N_values, C_old):
        """Update central point C"""
        input_data = np.array([[Y_N_values, C_old]]).reshape(1, 1, 2)
        return self.g_model.predict(input_data, verbose=0)[0][0]

    def run(self, output_file="cos_output.json"):
        """Run simulation"""
        C_history = []
        Y_N_history = {agent_id: [] for agent_id in self.agent_ids}
        eeg_history = []

        for t in range(self.num_time_steps):
            Y_N_values = []
            agent_states = {}
            eeg_input = self.external_input(1, t)

            for agent_id in self.agent_ids:
                Y, Y_N, eeg_input = self.agent_update(agent_id, t, self.C_old)
                Y_N_values.append(Y_N)
                agent_states[agent_id] = Y
                Y_N_history[agent_id].append(Y_N)

            C_new = self.central_server_update(Y_N_values, self.C_old)

            for agent_id in self.agent_ids:
                message = self.create_message(agent_id, t + 1, agent_states[agent_id], self.C_old, C_new, eeg_input)
                self.history.append(message)

            C_history.append(C_new)
            eeg_history.append(eeg_input)
            print(f"Time step {t + 1}: C_new = {C_new:.4f}, EEG_input = {eeg_input:.4f}")
            self.C_old = C_new

        with open(output_file, "w") as f:
            json.dump(self.history, f, indent=2)

        return C_history, Y_N_history, eeg_history
