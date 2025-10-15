from argparse import ArgumentParser
import sys
from importlib.machinery import SourceFileLoader
from traceback import format_exc

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


def test_generator_from_image():
    pass


def test_combine_images():
    pass


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "--test", choices=["pixel_constraint", "generator_from_image", "combine_images"], default="", required=False
    )
    arg_parser.add_argument("file")
    args = arg_parser.parse_args()
    if args.file.rfind("/") != -1:
        sys.path.append(args.file[: args.file.rfind("/")])
        potential_name = args.file[args.file.rfind("/") + 1 :]
    else:
        sys.path.append(".")
        potential_name = args.file
    if potential_name.rfind("."):
        name = potential_name[: potential_name.rfind(".")]
    else:
        name = potential_name
    try:
        lab5 = SourceFileLoader(name, args.file).load_module()
    except FileNotFoundError:
        print("Could not import lab: " + args.file)
        print("See traceback for further information:")
        print()
        stack_trace = format_exc().split("\n")
        importlib_has_started = False
        importlib_has_ended = False
        for line in stack_trace:
            if (
                not importlib_has_ended
                and importlib_has_started
                and line.lstrip().startswith("File")
                and "importlib" not in line
            ):
                importlib_has_ended = True
            if importlib_has_ended:
                print(line)
            elif (
                not importlib_has_started
                and line.lstrip().startswith("File")
                and "importlib" in line
            ):
                importlib_has_started = True
        exit(1)
    if args.test.upper() == "pixel_constraint":
        test_pixel_constraint()
    elif args.test.upper() == "generator_from_image":
        test_generator_from_image()
    elif args.test == "combine_images": 
        test_combine_images()
    else:
        print("Unknown arguemnt for --test: " + args.test)
        exit(2)
    print("The code passed all the tests")