# TASK1
Write a python script that finds numbers in range (2000-3600) that are divisible by 7 and not divisible by 5 and print a list of numbers on a single line in comma separated format.

# TASK2
Write a python script that display the following parameters:
-Byte order
-Core
-Model name
-CPU max Frequency
-CPU min frequency
-Virtualization
-L1i cache size
-L1d cache size
-L2 cache size
-L3 cache size
-Thread(s) per core
-Distributor ID
-Distributor Description
-Distributor codename

# TASK3
Write a Python script that reads from a Json File (json file) containing data about a group of people. The JSON file should contain a list of dictionaries, with each dictionary representing a person and their attributes (e.g. name, age, occupation). The script should then create a new dictionary that groups the people by their occupation. The keys of the new dictionary should be the occupation names, and the values should be lists of dictionaries representing the people in that occupation. Finally, the script should write the new dictionary to a new JSON file.

>Example Input:  
 [  {    "name": "Alice",    "age": 25,    "occupation": "teacher"  }, {    "name": "Bob",    "age": 30,    "occupation": "programmer"  },  {    "name": "Charlie",    "age": 35,    "occupation": "teacher"  }]
Example OUTPUT: 
{  "teacher": [   {      "name": "Alice",      "age": 25,      "occupation": "teacher"    },    {      "name": "Charlie",      "age": 35,      "occupation": "teacher"    }  ], "programmer": [    {      "name": "Bob",      "age": 30,      "occupation": "programmer"    }  ]}


# TASK4
Write a python script that takes two coordinates (x1,y1) , (x2, y2) as command line arguments and calculates distance between these points. (use python module math, argparser)

# TASK5
Write a python script that perform following steps: 
Take Path to a file (/home/user/Desktop/my_dummy_file.txt) and make sure this file exists in the directory if not create it.
Add some text in file and run this bash command from python script `chmod a=- my_dummy_file.txt`
Try to write/read to that file, identify the issues in read/write and resolve these issue using another python script.

# TASK6
Create a dummy text file and add the following line to it: 1,2,3,4,5,6,7,8,9,10. write a python script that perform the following task:
Use Virtual Environment for this task
Read the file and convert the comma separated text into a python list
Create another python file with two method/function that calculate the square and cube of that list and return square and cube list
Import that python module in first script and call these function and plot graph between square and cube lists as x and y axis respectively using matplotlib

# TASK7
write a python script that perform the following tasks:
Write a method name find_divisibles that finds the total divisible number in range from 1-range by a divisor. Example: (20,3) find numbers divisible by 3 in range 1-20 which is [3, 6, 9, 12, 15, 18].
Write a python script that call this method synchronously and run for all these ranges  
(50800000, 34113)  
(100052,3210)  
(20000,5)  
Write another python script that call this method asynchronously and create three different task for each pair: ( There should be context switching after each division)   
(50800000, 34113)  
(100052,3210)  
(20000,5)  
Also do logging and calculate total time take by the script to complete its task

# TASK8
write a python script that takes path to a file (text file) as a command line argument and and calculate the following parameters using numpy module:  
-Mean  
-Median  
-Max  
-Min  
-Standard Deviation  
-99th Percentile  
-99.9th Percentile  
-99.99th Percentile  
-99.999th Percentile   

# TASK9
Write a python based client server application using websockets with following features:  
  
**Client side:** Read a json data file (json file), send messages from client to server one by one using json data format. Make sure you connect with the server using websocket before sending a message.  
  
**Server side:** Server will open a websocket connection and wait to receive the query/message sent by client and append current timestamp in the received message and send response message back to client. 
Client will also Display the response received and time taken by websocket  from send message to response receive. Also store all the messages received in a file. (Do logging on both side)





