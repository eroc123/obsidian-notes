---
tags:
  - comsci/chapter-1
---

**Sound in nature is analogue and consist of pressure variations that can be detected by the human ear**.



- A sound encoder consists of two parts:
	- a band-limiting filter (filters sound below 20 Hz and 20,000 Hz out as they are inaudible to the human ear)
	- Analogue to digital converter (to convert the sound waves into bits that can be processed by a computer)
- **Sound quality factors**
	- **Sampling rate:** The amount of samples taken per second (x axis on a graph)
	- **Sampling resolution:** The amount of bits used to represent each sample (y axis on a graph)
		- The higher the resolution, the less distortion there is and **quantization error** there is.
		- Quantization error is the difference between the analog signal and the closest digital value to the analog signal. Think of it as a rounding off the analogue signal. The higher the resolution, the less "rounding" has to occur to match a digital value, thus reducing noise.
		- Usually 8 bit, 16 bit, 24 bit or 32 bit (1,2,3 or 4 bytes)
![[Sound wave.png]]
