from cos.core import COSSimulator
from cos.data import generate_training_data
from cos.utils import plot_simulation

# Training data
X_f_k, y_f_k, X_g, y_g = generate_training_data(num_samples=1000, N=3)

# Simulator
simulator = COSSimulator(N=3, agent_ids=["AI_001", "AI_002"], num_time_steps=100)
simulator.train_models(X_f_k, y_f_k, X_g, y_g, epochs=50, batch_size=32)
C_history, Y_N_history, eeg_history = simulator.run(output_file="cos_output.json")

# Plot results
plot_simulation(C_history, Y_N_history, eeg_history, simulator.agent_ids)
