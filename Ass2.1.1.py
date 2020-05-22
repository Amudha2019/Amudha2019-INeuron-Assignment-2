class Polygon:

    def __init__(self, n):
        self.number_of_sides = n

    def print_num_sides(self):
        '''a quick, informational print statement'''
        print('There are ' + str(self.number_of_sides) + ' sides.')

class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers

    def get_area(self):
        '''return the area of the triangle using the semi-perimeter method'''
        a, b, c = self.lengths_of_sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

p = Polygon(9)
p.print_num_sides()

tri = Triangle([3, 4, 5])
print(tri.get_area())

tri.print_num_sides()

