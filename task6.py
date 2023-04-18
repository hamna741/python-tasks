import os
import square_cube
import matplotlib.pyplot as plt
if os.path.exists("dummy_file.txt"):
    # If it exists, delete the file
    os.remove("dummy_file.txt")
    print(" COPY OF dummy file deleted.")
f = open("dummy_file.txt", "a")
f.write('1,2,3,4,5,6,7,8,9,10')
f = open("dummy_file.txt", "r")
values=list(f.read().split(","))
int_list = [int(value) for value in values]
#print(type(int_list))
f.close()
squres=square_cube.squared(int_list)
cubes=square_cube.cubed(int_list)
plt.plot(int_list, squres, 'r--', int_list, cubes ,'bs')
plt.xticks(int_list)
plt.title("SQUARE & CUBE GRAPH")
plt.xlabel('numbers')
plt.ylabel('squares and cubes')
plt.legend( ['square', 'cube'], loc ="upper right")
plt.show()