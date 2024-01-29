---
tags:
  - comsci/chapter-10
  - "#files"
---

- Mainly discuss about text files (.txt)


##### Pseudocode for opening files

OPEN \<file identifer> FOR \<file mode>

##### File Modes
- READ - reads data from a file
- WRITE - writes data to the file, any existing data will be overwritten
- APPEND - adds data to the end of a file


##### READ MODE

READFILE \<file identifier>, \<variable>

##### WRITE MODE

WRITEFILE \<file identifier>, \<variable>

**Variable must always be a string**

##### END OF FILE IDENTIFIER
EOF(\<file identifier>)

##### CLOSE FILE
CLOSEFILE \<file identifier>