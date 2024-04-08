
##### Eigenvectors
- Vector when multipled by a matrix does not change direction only magnitude
e.g. $\text{A} =  \begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$
$\text{A} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$
###### Method to solve
- $Ax = \lambda x$ condition for eigenvector since original vector doesnt change direction
- multiply both sides by identity vector - $IAx = \lambda Ax$
- can be written as $(A-\lambda I)x = 0$
- $(A-\lambda I)$ must be a singular matrix else x can only be the 0 vector
	- **det $(A-\lambda I)$ = 0** 
	- find eigenvalues
- then use original condition $Ax = \lambda x$ to find eigenvector

##### Eigenvalue
- The eigenvalue is the scalar that the original vector is multiplied by to get to the eigenvector after the matrix transformation is done
- e.g. eigenvalue for the eigenvector $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$  is 3 as when the matrix transformation is applied, the answer is $\begin{pmatrix} 3 \\ 3 \end{pmatrix}$

