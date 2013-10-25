import sys, os
import re

def vectorize(points, angle_rotation):
    vectors = []
    step = 3
    for i in range(0, len(points), step):
        try: 
            x1, y1, z1 = points[i:i+step]
            x2, y2, z2 = points[i+step:i+step+step]
            v = [p * angle_rotation for p in [x2 - x1, y2 - y1, z2- z1]]
            v[2] = -max([abs(c) for c in v])
            v.append(0)
            v.append("-")
            vectors += v
        except ValueError:
            break
    return vectors

def clean(file_name, output_name, angle_rotation):
    f = file(file_name, 'r')
    txt = f.read()
    result = re.findall('\-?\d*\.\d*', txt)
    points = [round(float(degree),2) for degree in result]
    vectors = vectorize(points, angle_rotation)
    lines = ["%s\n" % v for v in vectors]    
    directory, x = os.path.split(output_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    o = file(output_name, 'w')
    o.writelines(lines)

if __name__ == "__main__":

    #usage: python vectorize_dxf.py
    sys.stdout.write("dxf input file: ")
    dxf_file = raw_input()
    sys.stdout.write("output file: ")
    output_file = raw_input()
    sys.stdout.write("rotation angle: ")
    angle_rotation = float(raw_input())
    clean(dxf_file, output_file, angle_rotation)
