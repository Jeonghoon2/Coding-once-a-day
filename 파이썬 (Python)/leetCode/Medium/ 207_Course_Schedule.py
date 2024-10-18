# numCourcse 수강해야 할 총 과목 수

# prerequisites의 값이  =  [[1,0]] 일 경우
# 1과목을 듣기 위해서는 0과목을 먼저 들어야 한다.
# 단방향의 성질을 가지므로 조건이 성립하므로 True를 반환

# prerequisites의 값이  =  [[1,0],[0,1]] 일 경우
# 1과목을 듣기 위해서는 0과목을 먼저 들어야 하고 0과목을 듣기 위해서는 1과목을 먼저 들어야 한다.
# 양방향의 성질을 가지기 때문에 조건의 성립 하지 못하므로 False를 반환

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        visit = set()

        def dfs(crs):
            # 현재 과목이 이미 방문한 과목이 라면 양방향 조건이 되므로 False
            if crs in visit:
                return False

            # 현재 과목의 선행 과목이 없다면 True
            if len(graph[crs]) == 0:
                return True

            visit.add(crs)

            # 현재 과목의 선행 과목에 대해 DFS 수행
            for pre in graph[crs]:
                # 만약 선행 과목이 False를 반환하면 양방향 조건이 되므로 False
                if not dfs(pre):
                    return False

            # 동작이 끝났기 때문에 visit에서 제거
            visit.remove(crs)

            # 해당 과목은 모든 선행 과목을 체크 했기 때문에 중복을 방지 하기 위해
            graph[crs] = []

            # 현재 과목에 대한 모든 DFS 탐색이 성공했으므로 True 반환
            return True

        # 모든 과목에 대해 DFS 탐색 수행
        for crs in range(numCourses):
            # 각 과목에 대해 DFS를 수행하고, 사이클이 있으면 False 반환
            if not dfs(crs):
                return False

        # 모든 과목을 수강할 수 있으면 True
        return True


numCourses = 2
prerequisites = [[1, 0]]

print(Solution().canFinish(numCourses, prerequisites))
