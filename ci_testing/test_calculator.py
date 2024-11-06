# test_calculator.py

import pytest
from calculator import add, subtract

class TestCalculator:
    """Unit tests for the calculator module's add and subtract functions."""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test."""
        # Initialization before each test
        self.x = 10
        self.y = 5
        yield  # Code after this yield will be executed after each test method

        # Cleanup after each test
        del self.x
        del self.y

    def test_add_positive(self):
        """Test the add function with positive numbers."""
        result = add(self.x, self.y)
        assert result == 15, f"Expected 15, but got {result}"

    def test_add_negative(self):
        """Test the add function with negative numbers."""
        result = add(-self.x, -self.y)
        assert result == -15, f"Expected -15, but got {result}"

    def test_subtract_positive(self):
        """Test the subtract function with positive numbers."""
        result = subtract(self.x, self.y)
        assert result == 5, f"Expected 5, but got {result}"

    def test_subtract_negative(self):
        """Test the subtract function with negative numbers."""
        result = subtract(-self.x, -self.y)
        assert result == -5, f"Expected -5, but got {result}"

    def test_add_edge_case(self):
        """Test the add function with edge cases like 0."""
        result = add(0, 0)
        assert result == 0, f"Expected 0, but got {result}"

    def test_subtract_edge_case(self):
        """Test the subtract function with edge cases like subtracting a number from itself."""
        result = subtract(self.x, self.x)
        assert result == 0, f"Expected 0, but got {result}"

    def test_add_large_numbers(self):
        """Test the add function with large numbers."""
        result = add(10**6, 10**6)
        assert result == 2 * 10**6, f"Expected {2 * 10**6}, but got {result}"

    def test_subtract_large_numbers(self):
        """Test the subtract function with large numbers."""
        result = subtract(10**6, 10**5)
        assert result == 9 * 10**5, f"Expected {9 * 10**5}, but got {result}"

    def test_add_float(self):
        """Test the add function with float values."""
        result = add(1.5, 2.5)
        assert result == 4.0, f"Expected 4.0, but got {result}"

    def test_subtract_float(self):
        """Test the subtract function with float values."""
        result = subtract(5.5, 2.5)
        assert result == 3.0, f"Expected 3.0, but got {result}"
