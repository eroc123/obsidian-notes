---
tags:
  - comsci/chapter-4
---

1. MAR <- \[PC\]     // Address stored in [[Registers#^PC|PC]] is copied to [[Registers#^MAR|MAR]]
2. PC <- \[PC\]+1       // PC is incremented by 1
3. MDR <- \[\[MAR\]\]     // Data stored in the address in MAR is copied to [[Registers#^MDR|MDR]]
4. CIR <- \[MDR\]      // Data stored in MDR is copied to [[Registers#^CIR|CIR]]

For exam, just memorise this whole thing. Guaranteed to come up on topic papers by Mr Kerien
![[Instruction Cycle.canvas|Instruction Cycle]]