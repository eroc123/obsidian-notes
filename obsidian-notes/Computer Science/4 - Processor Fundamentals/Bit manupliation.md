---
tags:
  - comsci/chapter-4
---

Each bit in a register can be used as a flag and would need to be checked, set or cleared separately.

**AND** is used to check if the bit has been set
**OR** is used to set the bit
**XOR** is used to toggle a bit

**AND** check all bits to see which ones are on

| Input  | `0` | `1` | `1` | `0` |
| ------ | --- | --- | --- | --- |
| Mask   | `1` | `1` | `1` | `1` |
| Result | `0` | `1` | `1` | `0` |

**OR** turn on bits 1 and 3

| Input  | `0` | `1` | `1` | `0` |
| ------ | --- | --- | --- | --- |
| Mask   | `1`   | `0`   | `1`   | `0`   |
| Result | `1`   | `1`   | `1`   | `0`   |

**XOR** toggle all bits

| Input  | `0` | `1` | `1` | `0` |
| ------ | --- | --- | --- | --- |
| Mask   | `1` | `1` | `1` | `1` |
| Result | `1` | `0` | `0` | `1` |








