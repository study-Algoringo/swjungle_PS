class Stack:
    def __init__(self):
       self.stack = []
       
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.stack:
            return
        else:
            return self.stack.pop() 