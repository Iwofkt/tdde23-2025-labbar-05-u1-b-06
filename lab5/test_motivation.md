# Test Motivation

## test_is_black

**Constraints Range design:**

The values `100, 200, 50, 150, 75, 225` were chosen to create comprehensive
test coverage for the `pixel_constraint` function testing a multitude of valid values:

- ***Hue:*** 100-200 (100 unit range)
- ***Saturation:*** 50-150 (100 unit range)  
- ***Value:*** 75-225 (150 unit range)

**Valid Pixel Tests:**

Testing pixel within constraints with margin, within constraints by one unit at
both upper and lower bounds (all these should pass), and on the exclusive constraints
(should fail). The last tests are for individual components ensuring all three values
(HSV) are handled correctly.

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

The test image list `[(0, 0, 0), (255, 255, 255), (128, 128, 128), (200,110,50)]` was chosen to:
Cover extreme values like black (0,0,0) and white (255,255,255). Include mid-range values like 
gray (128,128,128) and colored pixels like (200,110,50) making sure all three values are different.

**Valid Index Tests:**
Tests all valid indices (0-3) to ensure the generator correctly returns the expected pixel
Verifies that the generator maintains the original order and values from the input list.

**Boundary Testing:**
- **Index 4** - Tests upper bound violation (just beyond last valid index)
- **Index -1** - Tests negative index handling (I decided negative index isn't allowed)
- **Empty list** - Test with no elements to ensure proper error handling

## test_combine_images

### Test Strategy Explanation:

** Valid Test Data Design:**
- **Condition list:** `[(100, 100, 100), (150, 150, 150), (200, 200, 200), (10,55,200)]`
- **Image 1:** `[(255, 0, 0), (0, 255, 0), (0, 0, 255), (250,101,239)]`
- **Image 2:** `[(0, 0, 0), (128, 128, 128), (255, 255, 255), (222, 245, 100)]`

Differing values from image 1 and image 2 while still testing a variety of values
similar to the blend file given in the assignment with condition list.
Color variety and differing BRG value testing given in image 1 with extrem values for B, R and G.
Testing values when B, R and B are the same and at min and max extremes and a perfect middle value
with image 2.

All three variables (Condition list, Image 1 and Image 2) End with a tuple containing random no min
or max values, all different to as last reasurent of correct functionality


**Invalid Test Data Design**

Bad generator miss function throws index error at index 1 to test exception handling for generators.
Bad condition allways raises a value error to tests exception handling of condition functions.
Empty condition list verifies graceful handling of case with no pixels to process.

**Operation Verification:**

First test ensures the functionality of combine images. That it returns a correct result list both to
length and content and validates that no exceptions are raised during normal operation.

Thereafter, testing individual Invalid components ensuring correct handling of every individual
component.