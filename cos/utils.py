import matplotlib.pyplot as plt

def plot_simulation(C_history, Y_N_history, eeg_history, agent_ids, output_file="cos_simulation.png"):
    """Plot simulation results"""
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, len(C_history) + 1), C_history, label="C (Central Point)", marker="o")
    for agent_id in agent_ids:
        plt.plot(range(1, len(Y_N_history[agent_id]) + 1), Y_N_history[agent_id], label=f"{agent_id} Y_N", marker="x")
    plt.plot(range(1, len(eeg_history) + 1), eeg_history, label="EEG Input", linestyle="--")
    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.title("COS Protocol EEG Simulation")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()
