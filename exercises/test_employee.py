import unittest

from employee import employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setup(self):
        """Make an employee to use in tests."""
        self.eric = Employee('eric', 'munoz', 65_000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 7000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.eric.give_raise(1000)
        self.assertEqual(self.eric.salary, 75000)

if __name__ == '__main__':
    unittest.main()