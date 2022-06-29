import math, os


def get_distance_between_points(p1, p2):
	x_diff_sq = math.pow(math.fabs(p1[0] - p2[0]), 2)
	y_diff_sq = math.pow(math.fabs(p1[1] - p2[1]), 2)
	return math.sqrt(x_diff_sq + y_diff_sq)

def get_triangle_area_by_sides(side1, side2, side3):
	p = (side1 + side2 + side3) / 2
	return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))


# change working directory to this script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

f = open("pe_102_triangles.txt")

origin_triangles_count = 0
epsilon = 10e-5

for line in f:
	coords = line.split(",")
	A = int(coords[0]), int(coords[1])
	B = int(coords[2]), int(coords[3])
	C = int(coords[4]), int(coords[5])
	O = (0, 0)

	AB = get_distance_between_points(A, B)
	AC = get_distance_between_points(A, C)
	AO = get_distance_between_points(A, O)

	BC = get_distance_between_points(B, C)
	BO = get_distance_between_points(B, O)

	CO = get_distance_between_points(C, O)

	ABC_area = get_triangle_area_by_sides(AB, BC, AC)
	ABO_area = get_triangle_area_by_sides(AB, AO, BO)
	BCO_area = get_triangle_area_by_sides(BC, BO, CO)
	ACO_area = get_triangle_area_by_sides(AC, AO, CO)

	if math.fabs(ABC_area - (ABO_area + BCO_area + ACO_area)) < epsilon:
		origin_triangles_count += 1


print(origin_triangles_count)
f.close()