import argparse
import math

try:
    parser = argparse.ArgumentParser(description="Finding ditance between two coordinate pairs in cm ")
    parser.add_argument("x1", nargs=2,type=float,
                        help="X cooridnate of first ordered pair in cm",)
    parser.add_argument("y1",nargs=2, type=float ,help="y cooridnate of first ordered pair in cm",)
    #parser.add_argument("x2", type=float ,help="X cooridnate of second ordered pair in cm",)
    #parser.add_argument("y2", type=float ,help="y cooridnate of second ordered pair in cm",)
    args = parser.parse_args()

    pair1=args.x1
    pair2=args.y1
  
    distance =math.dist(pair1,pair2)
    print(distance , "cm")

except ValueError:
    print("invalid argument entered ")