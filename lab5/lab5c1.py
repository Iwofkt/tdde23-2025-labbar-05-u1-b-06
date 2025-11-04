
from lab5.lab5b2 import generator_from_image
from lab5.lab5b4 import combine_images, gradient_condition
from lab5b1 import pixel_constraint


def test_is_black():
    """
    This test verifies that the function, returned from the
    image constraint function, correctly identifies
    whether pixels fall within specified HSV ranges by testing:
    - Pixels within all ranges
    - Pixels at boundary values
    - Pixels outside each individual HSV component range
    """

    is_black = pixel_constraint(
        100, 200, 50, 150, 75, 225)

    # Test 1: Valid pixel cases
    edge_tests = [
        ((150, 100, 150), 1,
         "Pixel within all ranges should return 1"),
        ((100, 50, 75), 0,
         "Pixel at lower bounds should return 0 (exclusive bounds)"),
        ((200, 150, 225), 0,
         "Pixel at upper bounds should return 0 (exclusive bounds)"),
        ((101, 51, 76), 1,
         "Pixel just above lower bounds should return 1"),
        ((199, 149, 224), 1,
         "Pixel just below upper bounds should return 1"),
        ((99, 50, 75), 0,
         "Pixel with H=99 (below range 100-200) should return 0"),
        ((150, 25, 150), 0,
         "Pixel with S=25 (below range 50-150) should return 0"),
        ((150, 100, 50), 0,
         "Pixel with V=50 (below range 75-225) should return 0"),
    ]

    for pixel, expected, desc in edge_tests:
        result = is_black(pixel)
        assert result == expected, f"{desc}. Got {result} for pixel {pixel}"

    # Test 2: Invalid inputs using test list
    invalid_inputs = [
        ("not_a_tuple", "Non-tuple input should raise ValueError"),
        ((1, 2), "2-tuple (too short) should raise ValueError"),
        ((1, 2, 3, 4), "4-tuple (too long) should raise ValueError"),
        (("a", "b", "c"), "Non-numeric values should raise ValueError"),
        ((150.5, 100.2, 150.8), "Float values should raise ValueError"),
    ]

    for input_val, description in invalid_inputs:
        try:
            is_black(input_val)
            assert False, description
        except (ValueError, TypeError):
            pass

    print("is_black passed all tests.")


def test_generator_from_image():
    """
    Test the function returned by generator_from_image for both valid
    behavior
    and proper exception handling when index is out of bounds.
    """
    # Create a simple test image list
    test_image_list = [
        (0, 0, 0),
        (255, 255, 255),
        (128, 128, 128),
        (200, 110, 50)
    ]

    generator = generator_from_image(test_image_list)

    # Test 1: Valid indices using test list
    valid_tests = [
        (0, (0, 0, 0), "Index 0 should return first pixel"),
        (1, (255, 255, 255), "Index 1 should return second pixel"),
        (2, (128, 128, 128), "Index 2 should return third pixel"),
        (3, (200, 110, 50), "Index 3 should return fourth pixel")
    ]

    for index, expected, descr in valid_tests:
        result = generator(index)
        assert result == expected, f"{descr}. Got {result} for index {index}"

    # Test 2: Invalid indices - should raise IndexError
    invalid_tests = [
        (4, "Index 4 (out of bounds) should raise IndexError"),
        (-1, "Index -1 (negative index) should raise IndexError")
    ]

    for index, description in invalid_tests:
        try:
            generator(index)
            assert False, description
        except IndexError:
            pass

    # Test 3: Empty image list
    empty_generator = generator_from_image([])
    try:
        empty_generator(0)
        assert False, "Index 0 on empty list should raise IndexError"
    except IndexError:
        pass

    print("generator_from_image passed all tests.")


def test_combine_images():
    """
    Test combine_images function for both valid behavior and exception
    handling when inner functions raise exceptions.
    """
    # Test data
    condition_list = [
        (100, 100, 100),
        (150, 150, 150),
        (200, 200, 200),
        (10, 55, 200)
        ]
    img1_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (250, 101, 239)]
    img2_list = [(0, 0, 0), (128, 128, 128), (255, 255, 255), (222, 245, 100)]

    generator1 = generator_from_image(img1_list)
    generator2 = generator_from_image(img2_list)

    # Test 1: Normal operation
    try:
        result = combine_images(
            condition_list, gradient_condition, generator1, generator2)
        assert (
            len(result) == len(condition_list)
            ), "Result should have same length as condition_list"
        assert result == (
            [(100, 0, 0), (52, 202, 52), (55, 55, 255), (231, 195, 148)]
        ), (
            "Unexpected output, got:", result, "expected:",
            [(100, 0, 0), (52, 202, 52), (55, 55, 255), (231, 195, 148)]
        )
    except ValueError:
        raise AssertionError(
            "Normal operation should not raise ValueError")

    # Test 2: Generator raises IndexError
    def bad_generator(index):
        if index == 1:
            raise IndexError("Index out of bounds")
        return 255, 0, 0

    try:
        combine_images(
            condition_list, gradient_condition, bad_generator, generator2)
        raise AssertionError(
            "Should raise ValueError when generator raises IndexError")
    except ValueError:
        pass

    # Test 3: Condition function raises ValueError
    def bad_condition(pixel):
        raise ValueError(f"Invalid pixel {pixel}")

    try:
        combine_images(
            condition_list, bad_condition, generator1, generator2)
        raise AssertionError(
            "Should raise ValueError when condition function raises ValueError"
            )
    except ValueError:
        pass

    # Test 4: Condition function raises TypeError
    def bad_condition_type(pixel):
        raise TypeError(f"Type error{pixel}")

    try:
        combine_images(
            condition_list, bad_condition_type, generator1, generator2)
        raise AssertionError(
            "Should raise ValueError when condition function raises TypeError"
            )
    except ValueError:
        pass

    # Test 5: Empty condition list
    try:
        result = combine_images(
            [], gradient_condition, generator1, generator2)
        assert result == [], "Empty condition list should return empty list"
    except ValueError:
        raise AssertionError(
            "Empty condition list should not raise ValueError"
        )

    # Test 6: Test to see if pixels are combine correctly

    print("combine_images passed all tests.")


if __name__ == '__main__':
    test_is_black()
    test_generator_from_image()
    test_combine_images()
