import unittest
from cos.core import COSSimulator

class TestCOSSimulator(unittest.TestCase):
    def test_initialization(self):
        sim = COSSimulator(N=3, agent_ids=["AI_001"])
        self.assertEqual(sim.N, 3)
        self.assertEqual(len(sim.f_k_models), 3)

    def test_run(self):
        sim = COSSimulator(N=2, agent_ids=["AI_001"], num_time_steps=5)
        C_history, _, _ = sim.run()
        self.assertEqual(len(C_history), 5)

if __name__ == '__main__':
    unittest.main()
