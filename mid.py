class A:
    def show_a(self):
        print("A")


class B(A):
    def show_b(self):
        print("B")


class C(A):
    def show_c(self):
        print("C")


class D(B, C):
    def show_d(self):
        print("D")


d = D()

d.show_a()
d.show_b()
d.show_c()
d.show_d()