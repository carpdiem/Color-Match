# Color-Match

This package contains utility functions for creating perceptually equivalent colors to those of a known spectrum when only having access to certain, fixed-wavelength sources.

In other words, if you've ever wondered "how do I make 1900K light with RGB LEDs?", then this package is for you.

## Installation

This package is on PyPI, so installation should be simple!

```
pip install Color_Match
```

## Use

Once you've installed it, go look up the emission wavelengths of your RGB LEDs on their datasheet. If you can't find them, you can try starting with something like 623nm, 528nm, and 470nm (some example wavelength values from some RGB LEDs I happen to have on hand right now), but your results may be a little off and require some tuning of the specific wavelengths.

Then, let's say that you're trying to generate the equivalent of 1900K light (roughly candle-light), you would use the following code.

```

import Color_Match as cm

# first, generate the expected sense vector for the color temperature in question
sv = cm.sense_vector(cm.planck_spectrum(1900))

# using the sample wavelength values from above, converted into units of meters
relative_intensities = cm.rgb_composition(623e-9, 528e-9, 470e-9, sv)

# full_brightness_limit is whatever value corresponds to a maximum output on an
#   individual RGB channel, typically this is 255
full_brightness_limit = 255

# desired_brightness is a value between 0.0 and 1.0 that represents how bright you
#   want your LEDs to be running; e.g., use 0.5 for 50% brightness
desired_brightness = 0.5

# since the values stored in relative_intensities are... relative intensities, we
#   need to scale them to produce the correct absolute settings for your RGB channels
absolute_rgb_levels = (desired_brightness * full_brightness_limit) * relative_intensities

```
