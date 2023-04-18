import json
import os
# Opening JSON file
try:
  file = open('Input.json')  
  employee_data = json.load(file) #json object--> dictionary

  group_by_occupation={}

  for employee in employee_data:    
      #print(employee)
      occupation=employee['occupation']
      #print(occupation)
      if occupation not in group_by_occupation:
          group_by_occupation[occupation]=[]
          
        # print(group_by_occupation)
      else:
          group_by_occupation[occupation].append(employee)
        #  print(group_by_occupation)

  #print(group_by_occupation)
  # Closing file
  file.close()

  json_data = json.dumps(group_by_occupation, indent=4)
  # Check if the file exists
  if os.path.exists("EMPLOYEE_OUTPUT_FILE.json"):
      # If it exists, delete the file
      os.remove("EMPLOYEE_OUTPUT_FILE.json")
      print(" COPY OF EMPLOYEE_OUTPUT_FILE.json deleted.")

    # Writing to sample.json
  with open("EMPLOYEE_OUTPUT_FILE.json", "w") as outfile:
          outfile.write(json_data)
except OSError:
    print ("Could not read file")
    
 
