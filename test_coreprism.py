# test_coreprism.py
"""
Tests for CorePrism module.
"""

import unittest
from coreprism import CorePrism

class TestCorePrism(unittest.TestCase):
    """Test cases for CorePrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CorePrism()
        self.assertIsInstance(instance, CorePrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CorePrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
