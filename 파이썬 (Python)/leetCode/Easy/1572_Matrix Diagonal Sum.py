class Solution:
    def diagonalSum(mat):
        answer = 0
        visit = []
        left_f, left_s, l_i, l_j = 0, 0, 0, 0
        right_f, right_l, r_i, r_j = 0, 0, 0, len(mat)-1

        while True:
            visit.append([l_i, l_j])
            l_i += 1
            l_j += 1
            visit.append([r_i, r_j])
            r_i += 1
            r_j -= 1
            # Range Over일 때
            if l_i > len(mat[0])-1 and r_i > len(mat[0])-1:
                break

        # change Tuple
        tuple_visit = set([tuple(i) for i in visit])


        for i in tuple_visit:
            i = list(i)
            k = i[0]
            v = i[1]
            answer += (mat[k][v])

        return answer


print(Solution.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
