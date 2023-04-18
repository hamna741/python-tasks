import argparse
import math

try:
    parser = argparse.ArgumentParser(description="Finding ditance between two coordinate pairs in cm ")
    parser.add_argument("x1", type=float ,help="X cooridnate of first ordered pair in cm",)
    parser.add_argument("y1", type=float ,help="y cooridnate of first ordered pair in cm",)
    parser.add_argument("x2", type=float ,help="X cooridnate of first ordered pair in cm",)
    parser.add_argument("y2", type=float ,help="y cooridnate of first ordered pair in cm",)
    args = parser.parse_args()

    x1=args.x1
    y1=args.y1
    x2=args.x2
    y2=args.y2
    distance =math.dist([x1,y1],[x2,y2])
    print(distance , "cm")

except ValueError:
    print("invalid argument entered ")