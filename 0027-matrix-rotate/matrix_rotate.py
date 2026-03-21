"""
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. 
For instance, given [[1, 2], [3, 4]], which looks like this:

You should return [[3, 1], [4, 2]], which looks like this:
"""
def rotate(matrix):
    """
    Rotates the matrix 90 degrees clockwise in-place and returns it.
    
    Args:
        matrix: A list to be rotated.
        
    Returns:
        matrix: The rotated matrix 
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

    return matrix
