from functions import calculate_monthly_payment

def test_calculate_monthly_payment():
    # Test case 1: Monthly payment calculation
    assert calculate_monthly_payment(100000, 5, 30) == 536.82
