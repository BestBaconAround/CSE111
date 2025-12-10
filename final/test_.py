from pytest import approx

import proposal


def test_validate_amount_valid():
    is_valid, value = proposal.validate_amount("10")
    assert is_valid is True
    assert value == approx(10.0)

    is_valid, value = proposal.validate_amount("3.5")
    assert is_valid is True
    assert value == approx(3.5)


def test_validate_amount_invalid():
    is_valid, value = proposal.validate_amount("abc")
    assert is_valid is False
    assert value == approx(0.0)

    is_valid, value = proposal.validate_amount("0")
    assert is_valid is False
    assert value == approx(0.0)

    is_valid, value = proposal.validate_amount("-5")
    assert is_valid is False
    assert value == approx(0.0)


def test_add_expense_creates_new_list():
    expenses = []
    new_list = proposal.add_expense(expenses, 10.0, "Food")

    assert expenses == []
    assert len(new_list) == 1
    assert new_list[0]["amount"] == approx(10.0)
    assert new_list[0]["category"] == "Food"


def test_calculate_total():
    expenses = [
        {"amount": 10.0, "category": "Food"},
        {"amount": 5.5, "category": "Travel"},
        {"amount": 4.5, "category": "Snacks"},
    ]
    total = proposal.calculate_total(expenses)
    assert total == approx(20.0)


def test_calculate_remaining_budget():
    remaining = proposal.calculate_remaining_budget(100.0, 40.0)
    assert remaining == approx(60.0)

    remaining = proposal.calculate_remaining_budget(50.0, 80.0)
    assert remaining == approx(-30.0)
