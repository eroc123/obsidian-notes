---
tags:
  - comsci/chapter-1
---

**Run Length Encoding** - A form of lossless compression technique by reducing adjacent identical data to two values, first the run value, which is the repeated data, and the run count, which is the amount of time the data is repeated.

E.g. aaaabbbccccc to 97 4 98 3 99 5 in ASCII

Can also be used for images for color of pixel

**To reduce bitmap image file size:**

- Reduce image resolution
- Reduce color depth
- Crop the image
- RLE

**To reduce text file size:**

- RLE

**To reduce vector graphic image file size:**

- Similar to text as svg stores vector graphic in text format

**To reduce sound file size:**

- Reduce sampling rate
- Reduce sampling resolution
- Perceptual music shaping (remove frequencies outside human hearing range)
- Clip the sound file
- RLE (repeated sections of music identified and indexed)

