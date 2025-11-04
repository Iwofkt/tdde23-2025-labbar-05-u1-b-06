# Test Motivation

## test_is_black

**Constraints Range design:**
```python
is_black = pixel_constraint(100, 200, 50, 150, 75, 225)
```
The values `100, 200, 50, 150, 75, 225` were chosen to create comprehensive
test coverage for the `pixel_constraint` function testing a multitude of valid values:

- ***Hue:*** 100-200 (100 unit range)
- ***Saturation:*** 50-150 (100 unit range)  
- ***Value:*** 75-225 (150 unit range)

**Pixel Tests:**

Testing pixel within constraints with margin, within constraints by one unit at both upper and lower bounds (all these should pass), and on the exclusive constraints (should fail). The last tests are individual for each component ensuring all three values (HSV) are handled correctly by giving them all different, unrelated, random values.

- **Normal:** `(150, 100, 150)` - Central values in all ranges (should pass)
- **On bounds:** `(100, 50, 75)` - Exactly at lower bounds (should fail due to exclusive bounds)
- **On bounds:** `(200, 150, 225)` - Exactly at upper bounds (should fail due to exclusive bounds)
- **One unit margin:** `(101, 51, 76)` - Just inside all bounds (should pass)
- **One unit margin:** `(199, 149, 224)` - Just inside all bounds (should pass)
- **Individual component testing:** `(99, 50, 75)` - Fails only on Hue (below range)
- **Individual component testing:** `(150, 25, 150)` - Fails only on Saturation (below range)
- **Individual component testing:** `(150, 100, 50)` - Fails only on Value (below range)

## test_generator_from_image

**Image List Design:**
```python
    test_image_list = [
        (0, 0, 0),
        (255, 255, 255),
        (128, 128, 128),
        (200, 110, 50)
    ]
```
was chosen to cover extreme values like black (0,0,0) and white (255,255,255). Include mid-range values like gray (128,128,128) and colored pixels like (200,110,50) making sure all three values are different.

**Valid Index Tests:**
Tests all valid indices (0-3) to ensure the generator correctly returns the expected pixel. Verifies that the generator maintains the original order and values from the input list.

**Boundary Testing:**
- **Index 4** - Tests upper bound violation (just beyond last valid index)
- **Index -1** - Tests negative index handling (I decided negative index isn't allowed)
- **Empty list** - Test with no elements to ensure proper error handling

## test_combine_images

### Valid Test Data Design:

```python
condition_list = [
    (100, 100, 100),
    (150, 150, 150),
    (200, 200, 200),
    (10, 55, 200)
    ]
img1_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (250, 101, 239)]
img2_list = [(0, 0, 0), (128, 128, 128), (255, 255, 255), (222, 245, 100)]
```

I have chosen a variety of values similar to the blend file given in the assignment within condition list. Testing differing BRG value given in image 1 with extrem values for B, R and G. Testing values when B, R and B are the same and at min and max extremes and a perfect middle value with image 2.

All three variables (Condition list, Image 1 and Image 2) End with a tuple containing random non min or max values, all different to as last reasurent of correct functionality.

### Normal test

```python
 try:    try:
        result = combine_images(
            [], gradient_condition, generator1, generator2)
        assert result == [], "Empty condition list should return empty list"
    except ValueError:
        raise AssertionError(
            "Empty condition list should not raise ValueError"
        )
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
```

First test ensures the functionality of combine images. That it returns a correct result list both length and conense and validates that no exceptions are raised during normal operation.

### Invalid Test Data Design

**Generator tests**

```python
def bad_generator(index):
    if index == 1:
        raise IndexError("Index out of bounds")
    return 255, 0, 0
```

Bad generator function throws index error at index 1 to test exception handling for generators. Empty condition list verifies graceful handling of case with no pixels to process.

**Condition function test**

```python
def bad_condition_value(pixel):
    raise ValueError(f"Invalid pixel {pixel}")
```

```python
def bad_condition_type(pixel):
    raise TypeError(f"Type error{pixel}")
```

The bad condition funtions allways raises a value or type error to tests exception handling of condition functions.

**Empty condition list test**

```python
try:
    result = combine_images(
        [], gradient_condition, generator1, generator2)
    assert result == [], "Empty condition list should return empty list"
except ValueError:
    raise AssertionError(
        "Empty condition list should not raise ValueError"
    )
```

Ensures that the combine_images function raises an error is the input condition_list is empty.

# Exception Handling Design

## is_black

```python
if not isinstance(pixel, tuple): raise TypeError("Pixel must be a tuple")
```
This ensures input is proper, pixel like, tuple structure and raises an error for incorrect data types. Raise TypeError because its a question of correct data type.

```python
if len(pixel) != 3: raise ValueError("Pixel must contain exactly 3 numbers")
```
Guarantees exactly 3 (HSV) components also ensuring that the given input follows a piexl like structure. Raises ValueError because the issue is with the structure of the input data.

```python
if not isinstance(color, int): raise TypeError("All HSV parameters must be integers")
if color < 0 or color > 255: raise ValueError("All HSV parameters must be between 0 and 255")
```
These if statements enforce that the contence of the tuples is correct according to the expected pixel format. The first check raises TypeError for incorrect data types, while the second raises ValueError for values outside the valid 0-255 HSV range,


## generator_from_image

```python
if index < 0 or index >= len(image_list):
    raise IndexError(f"Index {index} is out of bounds...")
```
This ensures the requested index exists within the valid range of the image list. Raises IndexError because it's a question of accessing a valid position within a sequence.

## combine_images

```python
except (IndexError, ValueError, TypeError):
    raise ValueError(f"Error in gradient_condition for value {pixel}")
```
This catches exceptions from gradient_condition and converts them to a ValueErrors because within combine_images gradient_condition becomes a faulty value if an error appers within it. It catches IndexError, ValueError, TypeError because these are the errors that can be raised within gradient_condition.


```python
except IndexError:
    raise ValueError("Error in combine_images: generator<i> raised IndexError")
```
Catches IndexError witch is the sole exception generators raise. Converts to ValueError to maintain combine_images' error abstraction.