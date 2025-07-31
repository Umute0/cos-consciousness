# Getting Started with COS-Consciousness

1. Clone the repository:
```bash
git clone https://github.com/Umute0/cos-consciousness.git
cd cos-consciousness

Inastall dependencies
pip install -r requirements.txt

run example
from cos.core import COSSimulator
simulator = COSSimulator(N=3, agent_ids=["AI_001", "AI_002"])
simulator.run(output_file="cos_output.json")

See examples/eeg_simulation.py for a full example with visualization.
