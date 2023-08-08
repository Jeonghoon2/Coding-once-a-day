class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage)

    def visit(self, url):
        # current.next를 새로운 node로 변경해준다.
        # 요구 조건에 back 함수를 사용 해서 current가 제일 끝이 아니고 뒤에 node가 남아 있으면
        # 모두 지워라는 조건이 있다.
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        pass

    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val


browserHistory = BrowserHistory("leetcode.com")

print(browserHistory)
