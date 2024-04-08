---
tags:
  - comsci/chapter-1
---

Bitmap images are made up of **pixels**, which are the smallest picture element that can be drawn. 
- It is a small square with a specific color. 

Each pixel has a color, and the amount of bits that the color of each pixel takes up is the **color depth (bit depth).**
- Usually 3 bytes (24 bits) used per pixel, as it can represent over a million color combinations

The amount of pixels that makes up an image depends on the **image resolution**, which is represented by the amount of pixels horizontally by the amount of pixels vertically. 
- To calculate how many pixels in an image, multiply the number of horizontal pixels by number of vertical pixels, (e.g. 300 height 400 width it would be 300x400 = 12,000px)

Each image file has a **file header**, which stores the metadata, including file size, image solution, color depth, type of compression etc. 

The file size of an image is a combination of its **image data** and its **metadata**. 
- Calculated by multiplying the number of pixels by each pixel's bit depth. e.g. the image size of an image with bit depth of 24 bits and 12,000 pixels would be 12,000 x 24 = 288,000 bits 
- This number will be combined with the size of the metadata to get the total file size.

File formats are usually:
- .png, .jpg, .bpm

Images are displayed on a screen. The **screen resolution** is the amount of pixels that the screen can display, represented by the amount of pixels horizontally by the amount of pixels vertically.
![[Bitmap.png]]