class MinStack:
    #O(1)
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack == []:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# O(n) - finding minimum
# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val):
#         self.stack.append(val)

#     def pop(self):
#         self.stack.pop()

#     def top(self):
#         return self.stack[-1]

#     def getMin(self):
#         return min(self.stack)
