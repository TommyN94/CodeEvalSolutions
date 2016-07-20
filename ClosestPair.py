# Closest Pair
#
# https://www.codeeval.com/open_challenges/51/
#
# You will be given the x/y co-ordinates of several locations. You will be
# laying out 1 cable between two of these locations. In order to minimise the
# cost, your task is to find the shortest distance between a pair of locations,
# so that pair can be chosen for the cable installation.
import math;
import sys;


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist_from(self, other_point):
        x_distance = self.x - other_point.x
        y_distance = self.y - other_point.y
        return math.sqrt(x_distance**2 + y_distance**2)
        
    @staticmethod
    def parse_string(string, delim = ' '):
        numbers = string.split(delim)
        x = int(numbers[0])
        y = int(numbers[1])
        return Point(x, y)
        
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


input_file = sys.argv[1]
test_cases = open(input_file, 'r')
n_test_cases = int(test_cases.readline().rstrip())

list_of_points = []
for i in range(n_test_cases):
    point = Point.parse_string(test_cases.readline().rstrip())
    list_of_points.append(point)
test_cases.close()

min_distance = float('inf')
for point in list_of_points:
    for other_point in list_of_points:
        if point is not other_point:
            distance = point.dist_from(other_point)
            if distance < min_distance:
                min_distance = distance

if min_distance < 10000:
    print(round(min_distance, 4))
else:
    print('INFINITY')

sys.exit(0)
