from unit_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    cm_to_inches,
    miles_to_km
)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40

def test_cm_to_inches():
    assert cm_to_inches(0) == 0
    assert cm_to_inches(100) == 39.3701
    assert cm_to_inches(50) == 19.68505

def test_miles_to_km():
    assert miles_to_km(0) == 0
    assert miles_to_km(10) == 16.0934
    assert miles_to_km(5) == 8.0467

if __name__ == "__main__":
    test_celsius_to_fahrenheit()
    test_fahrenheit_to_celsius()
    test_cm_to_inches()
    test_miles_to_km()

    print("All tests passed!")
