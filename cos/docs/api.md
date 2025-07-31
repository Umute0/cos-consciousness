# COS API Documentation

## COSSimulator
Main class for running the Consciousness Simulation Protocol.

### `__init__(N, agent_ids, num_time_steps)`
- `N`: Number of layers (default: 3).
- `agent_ids`: List of agent IDs (default: ["AI_001", "AI_002"]).
- `num_time_steps`: Number of simulation steps (default: 100).

### `train_models(X_f_k, y_f_k, X_g, y_g, epochs, batch_size)`
Train f_k and g models with synthetic or real EEG data.

### `run(output_file)`
Run simulation and save results to a JSON file.

Full details in `cos/core.py`.
