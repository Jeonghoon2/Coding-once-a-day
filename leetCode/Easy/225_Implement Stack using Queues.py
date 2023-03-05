from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()
        self.sub_queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    # pop은 queue가 하나 남을 때 까지 sub_queue에 옮겨 주고 pop의 결과를 저장후 que와 sub큐 역활 변경
    def pop(self) -> int:
        answer = None
        while len(self.queue)> 1:
            tmp = self.queue.popleft()
            self.sub_queue.append(tmp)

        if len(self.queue) == 1:
            answer=self.queue.popleft()
            self.queue,self.sub_queue=self.sub_queue,self.queue
        return answer

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return False if self.queue else True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()