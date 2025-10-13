from lab5.lab5b1 import pixel_constraint


def test_pixel_constraint():
    hlow, slow, vlow = 0, 0, 0
    hhigh, shigh, vhigh = 100, 100, 100

    test_inst = pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh)

    test_values = [
        hlow + 1,
        (hlow + hhigh) // 2,
        hhigh - 1
    ]

    passed = True
    for h in test_values:
        for s in test_values:
            for v in test_values:
                result = test_inst((h, s, v))
                assert result == 1, f"Failed on: {(h, s, v)}"

    out_of_range = [
        (hlow - 1, 50, 50),
        (hhigh + 1, 50, 50),
        (50, slow - 1, 50),
        (50, shigh + 1, 50),
        (50, 50, vlow - 1),
        (50, 50, vhigh + 1),
    ]

    for pixel in out_of_range:
        result = test_inst(pixel)
        assert result == 0, f"Out-of-range test failed on: {pixel}"

    if passed:
        print("Code passed all tests.")

test_pixel_constraint()