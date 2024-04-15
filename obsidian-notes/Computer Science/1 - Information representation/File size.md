---
tags:
  - comsci/chapter-1
---

In computers, data is stored in bits. Each bit can be either 1 or 0

There is 8 bits in one byte.

To calculate file size, one simply find how many bits is used, convert it to bytes, and find the correct [[Number prefixes|prefix]] to use.

### Image file

To calculate the file size of an [[Bitmap image|image file]], you take the width $\times$ height, and times color depth. This gives you the minimum file size.

An image file will always be larger than the minimum size as metadata is stored for each file.

### Audio file

To calculate the file size of an [[Representing of sound|audio file]], you take the rate at which data is recorded, e.g. 24 hz, and you times that by the number of bits used to represent the amplitude of the sound. This will also give you the minimum file size as metadata is also present.