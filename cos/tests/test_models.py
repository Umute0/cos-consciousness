import unittest
from cos.models import create_f_k_model, create_g_model

class TestModels(unittest.TestCase):
    def test_f_k_model(self):
        model = create_f_k_model()
        self.assertEqual(len(model.layers), 3)

    def test_g_model(self):
        model = create_g_model()
        self.assertEqual(len(model.layers), 2)

if __name__ == '__main__':
    unittest.main()
