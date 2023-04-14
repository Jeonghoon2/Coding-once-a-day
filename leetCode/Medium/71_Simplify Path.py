
class Solution:
    def simplifyPath(self, path):
        path = list(path.split('/'))

        while True:
            if '' not in path and '.' not in path:
                break
            if '' in path:
                path.remove('')
            if '.' in path:
                path.remove('.')


        while '..' in path:
            idx = path.index('..')
            del path[idx]
            if idx >0:
                del path[idx - 1]

        path = '/'.join(path)

        return '/' + path


path = "/home//foo/"
print(Solution().simplifyPath(path))
