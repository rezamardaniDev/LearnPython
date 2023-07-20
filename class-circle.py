class Circle:
    number_of_p = 3.14

    def __init__(self, radius) -> None:
        self.redius = radius

    # محاسبه مساحت
    def environment(self):
        print((self.redius**2) * self.number_of_p)
    # محاسبه محیط
    def area(self):
        print((2 * self.redius) * self.number_of_p)

c1 = Circle(2)
c1.area()
