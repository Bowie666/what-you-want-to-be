"""chain of responsibility pattern 责任链模式

知道怎么肥事就行 先别挣扎了

在这种模式中，通常每个接收者都包含对另一个接收者的引用。如果一个对象不能处理该请求，那么它会把相同的请求传给下一个接收者，依此类推。
"""











"""我自己写的 总归是差点什么
class Stram:
    def leave(self, day):
        pass

class Boss(Stram):
    def leave(self, day):
        if day > 10:
            print("滚(ノ｀Д)ノ")

class Depart(Stram):
    def __init__(self):
        self.next = Boss()
    def leave(self, day):
        if day < 10:
            print("部门经理准假")
        else:
            print("部门经理准假权限不够")
            self.next.leave(day)

class Leader(Stram):
    def __init__(self):
        self.next = Depart()
    def leave(self, day):
        if day < 5:
            print("直属领导请假")
        else:
            print("直属领导请假权限不够")
            self.next.leave(day)

day = 11
l = Leader()
l.leave(day)
"""