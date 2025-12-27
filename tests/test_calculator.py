"""
Test suite for the Calculator class.
"""

import pytest
from calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    "Fixture to create instance test"
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # TODO: Implement
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # TODO: Implement
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # TODO: Implement
        # Arrange
        calc = Calculator()
        a = 10
        b = 2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected


class TestInputValidation:
    """Tests for input validation."""

    def test_add_with_too_large_value(self, calc):
        """Test that add raises InvalidInputException for max_value"""
        # Arrange
        a = 1000000
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_with_too_small_value(self, calc):
        """Test that add raises InvalidInputException for min_value"""
        # Arrange
        a = -1000000
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_subtract_with_too_large_value(self, calc):
        """Test that subtract raises InvalidInputException for max_value"""
        # Arrange
        a = 1000000
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_with_too_small_value(self, calc):
        """Test that subtract raises InvalidInputException for min_value"""
        # Arrange
        a = -1000000
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_multiply_with_too_large_value(self, calc):
        """Test that multiply raises InvalidInputException for max_value"""
        # Arrange
        a = 5
        b = 1000000

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_with_too_small_value(self, calc):
        """Test that multiply raises InvalidInputException for min_value"""
        # Arrange
        a = 5
        b = -1000000

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_divide_with_too_large_value(self, calc):
        """Test that divide raises InvalidInputException for max_value"""
        # Arrange
        a = 1000000
        b = 2

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_with_too_small_value(self, calc):
        """Test that divide raises InvalidInputException for min_value"""
        # Arrange
        a = -1000000
        b = 2

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)
