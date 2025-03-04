from functions import calculate_bmi, interpret_bmi

def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.86

def test_interpret_bmi():
    assert interpret_bmi(22.86) == "Normāls svars"
