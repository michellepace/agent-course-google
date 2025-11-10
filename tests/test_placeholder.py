"""Tests for placeholder module."""

from agent_course_google.placeholder import add


def test_add_two_positive_numbers() -> None:
    """Test adding two positive numbers."""
    result = add(2, 3)
    assert result == 5
