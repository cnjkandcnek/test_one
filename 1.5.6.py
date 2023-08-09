class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        one_step = 0
        two_step = 0
        # if isinstance(self.a and self.b and self.c, int or float) != True or self.a <= 0 or self.b <= 0 or self.c <= 0:
        if type(self.a) not in (int, float) or self.a <= 0:
            return 1
        if type(self.b) not in (int, float) or self.b <= 0:
            return 1
        if type(self.c) not in (int, float) or self.c <= 0:
            return 1
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 2
        else:
            return 3



a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
result = tr.is_triangle()
print(result)