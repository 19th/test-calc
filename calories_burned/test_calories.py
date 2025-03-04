from functions import calculate_calories_burned

def test_calculate_calories_burned_running():
    assert calculate_calories_burned("running", 30, 70) == 350

def test_calculate_calories_burned_invalid_activity():
    assert calculate_calories_burned("walking", 60, 75) == "Activity not found. Please choose from: running, cycling, swimming"
