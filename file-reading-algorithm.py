'''
Version 1.0
Khadeeja Rizwan
June 7, 2023
'''
#import statements
import csv
import calendar
from datetime import date
import numpy as np
import random 

#functions
def readData(file_name):
  '''
  This function reads the inputted csv file and sorts it
   Args
       file_name: String
   Returns
       data: dictionary
       locations: set
  '''
  #reading files
  csv_file = open(file_name)
  csv_reader = csv.DictReader(csv_file)
  line_count = 0
  data = {}
  locations = set()
  #looping through data
  for row in csv_reader:
    data[row['name']] = [float(row['prep time'])]
    line_count += 1
    #checks if row has a location then adds to set
    if row['locations'] != None:
      locations.add(row['locations'])
  csv_file.close()
  return data, locations

def findLocation(mini_schedule, date, locations, x):
  '''
  This function checks whether a viable location is chosen
   Args
       mini_schedule: dictionary
       date: String
       locations: set
       x: list
   Returns
       new_location: String
  '''
  #create temporary placeholder for the schedule
  temp = mini_schedule[date]
  #randomly picks location
  new_location = random.sample(locations, 1)[0]
  #if the date has multiple locations need to check same location isnt being reused
  location = []
  if len(temp) >= 1:
    for i in temp:
      location.append(i[1])
   #checks if there are more people than locations, then chooses a random location
    if len(locations) <= len(temp):
      new_location = random.sample(locations, 1)[0]
    else:
       #checks if randomly picked location is the same as the current location
      while new_location in location:
        new_location = random.sample(locations, 1)[0]
  return new_location

  
def createSchedule(data, locations):
  '''
  This function creates the schedule
   Args
       data: dictionary
       locations: set
   Returns
       mini_schedule: dictionary
  '''
  #creating the dictionary to store the schedule
  mini_schedule = {}
  for i in range(4):
    mini_schedule['day ' + str(i + 1)] = []

  #loop through all teachers
  for i in data:
    #x = list of values corresponding to each teacher
    x = data[i]
    #if fulltime teacher then must supervise on all days
    if x[0] == 1.0:
      for j in range(4):
        loc = findLocation(mini_schedule, 'day '+ str(j + 1), locations, x)
        mini_schedule['day ' + str(j + 1)].append([i, loc])
    
    #only needs to be added in 2/4 days of the schedule
    elif x[0] == 0.5:
      num = 1
      days = 0
      stored_days = []
      while days < 2 or num < 4:
        if len(mini_schedule['day ' + str(num)]) <= len(locations):
          #checks if more teachers have been sent to this day than locations present (managing overflow)
          loc = findLocation(mini_schedule, 'day ' + str((days % 4) + 1), locations, x)
          mini_schedule['day ' + str((days % 4) + 1)].append([i, loc])
          days += 1
          stored_days.append(num)
        num += 1

      while days < 2:
        #if days still has not reached two (all days have full locations) random location picked
        day = (days % 4) + 1
        #other possibility: day = random.randint(1, 4)
        if day not in stored_days:
          loc = findLocation(mini_schedule, 'day ' + str(day), locations, x)
          mini_schedule['day ' + str(day)].append([i, loc])
          day += 1
        days += 1
    
    #only needs to be added in 1/4 days of the schedule
    elif x[0] <= 0.3:
      chosen = 0
      while chosen != 1:
        for j in range(4):
          #checks if there are no people in that day, to automatically add (first choice)
          if chosen != 1:
            if len(mini_schedule['day ' + str(j + 1)]) == 0:
              loc = findLocation(mini_schedule, 'day ' + str(j + 1), locations, x)
              mini_schedule['day ' + str(j + 1)].append([i, loc])
              chosen = 1
            #checks if there are unfilled schedules (second choice)
            elif len(mini_schedule['day ' + str(j + 1)]) < len(locations):
              loc = findLocation(mini_schedule, 'day ' + str(j + 1), locations, x)
              mini_schedule['day ' + str(j + 1)].append([i, loc])
              chosen = 1
        #if none of the previous options were viable randomly picks a day to add the person
        if chosen != 1:
          day = random.randint(1, 4)
          loc = findLocation(mini_schedule, 'day ' + str(day), locations, x)
          mini_schedule['day ' + str(day)].append([i, loc])
          chosen = 1
  return mini_schedule

def writeData(schedule):
  '''
  This function writes data into a csv file
   Args
       schedule: dictionary
   Returns
       None
  '''
  #setting the variables
  f = open('output.csv', 'w')
  writer = csv.writer(f)
  headers = []
  data = []
  #looping through schedule and adding the keys as headers and the values as data for the rows
  for i in schedule:
    headers.append(i)
    data.append(schedule[i])
  #writing the information
  writer.writerow(headers)
  writer.writerow(data)

  f.close()



#mimicing the questions the form on the website would ask
date1 = input('enter the start date (YYYY/MM/DD): ')
date1 = date1.split('/')
date1 = [int(x) for x in date1]

date2 = input('Enter the end date (YYYY/MM/DD): ')
date2 = date2.split('/')
date2 = [int(x) for x in date2]

#not used in this program
semester = input('is your school semestered (write True) or non-semestered (write False)? ')
board = input('What is the the school board (enter either OCDSB or OCSB)')

#finding timespan
cal = calendar.Calendar(firstweekday=0)
#d0 = date(date1[0], date1[1], date1[2])
#d1 = date(date2[0], date2[1], date2[2])
d0 = date(2022,9,6)
d1 = date(2023,6,23)
days = np.busday_count(d0, d1)
delta = d1 - d0

#calling functions
data, locations = readData('practice.csv')
sched = (createSchedule(data, locations))
writeData(sched)
