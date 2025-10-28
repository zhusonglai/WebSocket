# test_websockethub.py
"""
Tests for WebSocketHub module.
"""

import unittest
from websockethub import WebSocketHub

class TestWebSocketHub(unittest.TestCase):
    """Test cases for WebSocketHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WebSocketHub()
        self.assertIsInstance(instance, WebSocketHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WebSocketHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
