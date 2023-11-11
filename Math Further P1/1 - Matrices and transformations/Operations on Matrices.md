

### Addition and Subtraction 

- Ensure both matrices are the same [[Matrix fundamentals|dimensions]]
$$ \begin{pmatrix} 1&3&-7\\4&0&5\end{pmatrix} + \begin{pmatrix} 6& -2 & 9 \\2&1&0  \end{pmatrix} = \begin{pmatrix} 7&1&2\\2&1&0 \end{pmatrix}$$
### Multiplication (scalar)

$$3 \begin{pmatrix} 1&3&-7\\4&0&5 \end{pmatrix} = \begin{pmatrix} 3&9&-21\\12&0&15 \end{pmatrix}$$
Each element is multiplied by the scalar

### Multiplication (matrix)

$$\begin{pmatrix} 1&0&3&-1\\ 2&8&4&3 \\ 7&-1&0&2 \end{pmatrix}_{3\times 4} \times 
\begin{pmatrix}
5&1\\1&7\\0&3\\8&-3
\end{pmatrix}_{4\times2} = 
\begin{pmatrix} -11 & 16\\42&61\\50&-6 \end{pmatrix}$$

For each row in the first matrix, multiply each element by the column in the second matrix

$1\times5 + 0\times1 + 3\times0 + -1\times8$ gives you the result of the first element in the resultant matrix

**NOTE:** it is only possible to multiply matrices when the number of columns in the first matrix is the same as the number of rows in the second matrix

### Identity matrix

a matrix multiplied by an [[Special Matricies|identity matrix]] will always be equal to itself

**NOTE:** $AB \not= BA$ most of the times. 

Even if $AB$ exist, it is not guaranteed that $BA$ exists



