class Stack(object):
    def __init__(self,limit=10):
        self.stk = []
        self.limit = limit
    def isEmpty(self):
        return len(self.stk) <=0
    def push(self,item):
        if len(self.stk)>=self.limit:
            print('Stack Overflow!')
        else:
            self.stk.append(item)
        print('Stack after push',self.stk)
    def pop(sclf):
        if len(sclf.stk) <= 0:
            print ('Stack Underflow!')
            return 0
        else:
            return sclf.stk.pop()
    def peek(self):
        if len(self.stk)<=-0:
            print('stack underflow! ')
            return 0
        else:
            return self.stk[-1]
    def size(self):
        return len(self.stk)