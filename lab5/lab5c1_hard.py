from argparse import ArgumentParser
import sys
from importlib.machinery import SourceFileLoader
from traceback import format_exc

def test_pixel_constraints():
    test_inst = pixel_constraint(0, 100, 0, 100, 0, 100)

    assert all((test_inst((50,50,50)), test_inst((100, 100, 100)))) == True
    assert all(test_inst((101, 101, 101)), test_inst((-1, -1, -1))) == False


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
        test_pixel_constraints()
    elif args.test.upper() == "generator_from_image":
        test_generator_from_image()
    elif args.test == "combine_images": 
        test_combine_images()
    else:
        print("Unknown arguemnt for --test: " + args.test)
        exit(2)
    print("The code passed all the tests")