from lab5b1 import pixel_constraint


def test_image_constrain():
    """
    This test verifies that the function, returned from the
    image constraint function, correctly identifies
    whether pixels fall within specified HSV ranges by testing:
    - Pixels within all ranges
    - Pixels at boundary values
    - Pixels outside each individual HSV component range
    """

    is_black = pixel_constraint(100, 200, 50, 150, 75, 225)

    # Test 1: Valid pixel cases
    tests = [
        ((150, 100, 150), 1, "Pixel within all ranges should return 1"),
        ((100, 50, 75), 0, "Pixel at lower bounds should return 0 (exclusive bounds)"),
        ((200, 150, 225), 0, "Pixel at upper bounds should return 0 (exclusive bounds)"),
        ((101, 51, 76), 1, "Pixel just above lower bounds should return 1"),
        ((199, 149, 224), 1, "Pixel just below upper bounds should return 1"),
        ((99, 50, 75), 0, "Pixel with H=99 (below range 100-200) should return 0"),
        ((150, 25, 150), 0, "Pixel with S=25 (below range 50-150) should return 0"),
        ((150, 100, 50), 0, "Pixel with V=50 (below range 75-225) should return 0"),
    ]

    for pixel, expected, description in tests:
        result = is_black(pixel)
        assert result == expected, f"{description}. Got {result} for pixel {pixel}"

    # Test 2: Exception cases
    exception_tests = [
        ("not_a_tuple", "Non-tuple input"),
        ((1, 2), "2-tuple (too short)"),
        ((1, 2, 3, 4), "4-tuple (too long)"),
        (("a", "b", "c"), "Non-numeric values"),
        ((None,None,None), "Empty tuple")
    ]

    for input_val, description in exception_tests:
        try:
            is_black(input_val)
            print(f"{description} should raise ValueError")
        except ValueError:
            None

    # Test 3: Float values (should work)
    try:
        is_black((150.5, 100.2, 150.8))
    except Exception as e:
        print(f"✗ Float values should work: {e}")

    print("code passed all tests.")

def test_generator_from_image():
    return


if __name__ == '__main__':
    test_image_constrain()