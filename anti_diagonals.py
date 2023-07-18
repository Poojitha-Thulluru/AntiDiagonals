
def get_anti_diagonals(input_matrix: list, n_rows: int, n_columns: int) -> list:
    anti_diagonal: list = []
    for val in range(n_columns):
        lst: list = []
        i, j = 0, val
        while i < n_rows and j >= 0:
            lst.append(input_matrix[i][j])
            i += 1
            j -= 1
        anti_diagonal.append(lst)
    for val in range(n_rows - 1):
        lst: list = []
        i, j = val + 1, n_columns - 1
        while i < n_rows and j >= 0:
            lst.append(input_matrix[i][j])
            i += 1
            j -= 1
        anti_diagonal.append(lst)
    max_length = max(len(diagonal) for diagonal in anti_diagonal)
    for diagonal in anti_diagonal:
        diagonal.extend([0] * (max_length - len(diagonal)))
    return anti_diagonal


try:
    rows = int(input("Enter number of rows : "))
    columns = int(input("Enter number of columns : "))
    matrix = [[int(input(f"Enter element ({y},{x}) to insert into matrix : ")) for x in range(columns)]
              for y in range(rows)]
    anti_diagonals = get_anti_diagonals(matrix, rows, columns)
    print("The Anti Diagonals of the given matrix is : ")
    for diagonal in anti_diagonals:
        print(' '.join(str(num) for num in diagonal))
except ValueError:
    print("Invalid Input. Please enter only integers")
