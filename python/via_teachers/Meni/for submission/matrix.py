#סט תרכילים מטריצות
#===================

#1
def is_symmetric(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=mat[j][i]:
                return False
    return True

#2
def is_anti_symmetric(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=-(mat[j][i]):
                return False
    return True   
במטריצה אנטי-סימטרית כל איבר הופך למינוס של התא שמולו כאשר מחליפים שורה ועמודה; באיברי האלכסון התא נמצא מול עצמו ולכן חייב להתקיים 
, והמספר היחיד ששווה למינוס של עצמו הוא 0.

#3
def is_lower_triangular(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j > i and mat[i][j]!=0:
                    return False
    return True
    
#4
def is_upper_triangular(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j < i and mat[i][j]!=0:
                    return False
    return True
    
#5
def is_diagonal(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j != i and mat[i][j]!=0:
                    return False
    return True
    
#6
def is_scalar(mat):
    d=mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j != i and mat[i][j]!=0 :
                    return False
            if j==i and mat[i][j]!=d : 
                return False
    return True

#7
def is_zero(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=0 :
                return False
    return True

#8
def is_identity(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j != i and mat[i][j]!=0 :
                    return False
            if j==i and mat[i][j]!=1 : 
                return False
    return True
    
#9
def count_rectangle(mat):
    count = 0
    for i in range(1, len(mat)):             
        for j in range(1, len(mat[0])):     
            if mat[i][j] == 0:               
                if mat[i-1][j] == 1 and mat[i][j-1] == 1:
                    count += 1
    return count
     
#10
def neighbor_sum_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            s = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0 <= x < rows and 0 <= y < cols and not (x == i and y == j):
                        s += mat[x][y]
            new_row.append(s)
        result.append(new_row)
    
    return result

    
