import argparse
import math

try:
    parser = argparse.ArgumentParser(description="Finding ditance between two coordinate pairs in cm ")
    parser.add_argument("pair1", nargs=2,type=float,
                        help="first coordinate pair",)
    parser.add_argument("pair2",nargs=2, type=float ,help="second coordinate pair",)
    #parser.add_argument("x2", type=float ,help="X cooridnate of second ordered pair in cm",)
    #parser.add_argument("y2", type=float ,help="y cooridnate of second ordered pair in cm",)
    args = parser.parse_args()

    pair1=args.pair1
    pair2=args.pair2
  
    distance =math.dist(pair1,pair2)
    print(round(distance,3) , "cm")

except ValueError:
    print("invalid argument entered ")