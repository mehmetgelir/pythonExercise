from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon, box
import matplotlib.pyplot as plt

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)

multi_point = MultiPoint([point1, point2, point3])
multi_point2 = MultiPoint([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

line1 = LineString([point1, point2])
line2 = LineString([point2, point3])

multi_line = MultiLineString([line1, line2])

west_exterior = [(-180, 90), (-180, -90), (0, -90), (0, 90)]
west_hole = [[(-170, 80), (-170, -80), (-10, -80), (-10, 80)]]
west_poly = Polygon(shell=west_exterior, holes=west_hole)

min_x, min_y = 0, -90
max_x, max_y = 180, 90

east_poly_box = box(minx=min_x, miny=min_y, maxx=max_x, maxy=max_y)
multi_poly = MultiPolygon([west_poly, east_poly_box])

print("MultiPoint:", multi_point)
print("MultiLine: ", multi_line)
print("Bounding box: ", east_poly_box)
print("MultiPoly: ", multi_poly)