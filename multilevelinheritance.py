class A:
    def __init__(self):
        print("\n A")

    def f1(self):
        print("f1A")


class B(A):
    def __init__(self):
        super().__init__()
        print("\n B")

    def f1(self):
        super().f1()
        print("\n f1B")


class C(B):
    def __init__(self):
        super().__init__()
        print("\n C")

    def f1(self):
        super().f1()
        print("\n f1 C")
        b1 = B()
        b1.f1()


# Test
c1 = C()
c1.f1()
