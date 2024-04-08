
- Used in order to easily find a matrix raised to the power of n
- Written in form $A = PDP^{-1}$ - if a matrix can be written in this form its diagonalizable 

##### Method
- Find eigenvectors and eigenvalues of a given matrix
	- e.g. $\text A = \begin {pmatrix} -3 & -1 \\ 8 & 6 \end {pmatrix}$ eigenvalues are $\lambda = -2,5$ and eigenvectors are $\begin {pmatrix} 1  \\  -1 \end {pmatrix}$ ($\lambda = -2)$ and $\begin {pmatrix} 1  \\  -8 \end {pmatrix}$ ($\lambda = 5)$
	- $\text P = \begin {pmatrix} 1 & 1 \\ -1 & -8 \end {pmatrix}$ - combine the two eigenvectors together
	- $\text D = \begin {pmatrix} -2 & 0 \\ 0 & -5 \end {pmatrix}$ - put the two **respective** eigenvalues in the **same order** together like a diagonal
- An identity will be found where AP = PD
- Rearrange and you get $A = P^{-1} D P$
	- if you want to find e.g. $A^{20}$ you raise both sides to that power
	- $A^{20} = (P^{-1}DP)^{20}$
	- since $P * P^{-1} = I$ ,  $(P * P^{-1})^{20} = I$
	- hence $A^{20} = P^{-1}D^{20}P$ 
	- since D is a diagonal, it is easy to raise to an exponent 
		- if D is raised to n, each non zero value is also raised to n
