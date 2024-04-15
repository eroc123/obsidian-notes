.dll is the extension

- Collection of shared library routines for Windows
- Already compiled
- Separate from .exe files and linked to program during execution (runtime)
- Are made available to several programs at once saving memory.
	- Only one copy of the .dll has to be stored in memory, with each program being able call the same library for use.
- If the DLL is updated, the program that uses it will use the updated version

**Benefit of Dynamic Link Libraries:**
- memory requirements for program are reduced as dynamic link library is loaded only once / when required - they are loaded at runtime
- the executable file size is smaller because the executable does not contain all the library routines
- maintenance not needed to be done by the programmer because the DLL is separate from program 
- no need to recompile the main program when changes are made to DLL because changes / improvements/ error correction to the DLL file code are done independently of the main program
- These libraries reduce the duplication effort as they can be shared between multiple applications.