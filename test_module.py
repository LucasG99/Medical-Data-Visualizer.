import unittest
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_cat_plot(self):
        try:
            draw_cat_plot()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Cat plot failed with exception {e}")

    def test_heat_map(self):
        try:
            draw_heat_map()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Heat map failed with exception {e}")

if __name__ == "__main__":
    unittest.main()