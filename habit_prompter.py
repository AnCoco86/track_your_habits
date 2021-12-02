# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:17:18 2021

@author: ancovell
"""
#//# TODO: Print Start_End Date of Tracking
#Habit Prompter Coded

from datetime import date
import json
#if habits file doesnt exist, prevent an exception;

try:
    with open('habits.txt', 'r') as f:
        skills_dict = json.load(f)
except:
    skills_dict = {}
    with open('habits.txt', 'w') as f:
        content= json.dumps(skills_dict)
        f.write(content)
        f.close()

#create an empty habits skills_dict = {} to finally clause can run

finally:
    if skills_dict:
        open('habits.txt', 'w')

    if skills_dict == {}:
        #create a list of habits as strings
        habits_list = ['skating', 'exercising', 'meditating', 'guitar']
        #iterate over the list to create keys paired with empty dicts
        for habit in habits_list:
            skills_dict[habit] = {}


#print out current skills trackedy
print('Welcome to the Skills Dictionary.\n')
print('Current Skills Encoded: ')
for skill in skills_dict:
    print(skill)
print('\n############################\n CURRENT SKILL DICT :\n', skills_dict, \
      '/n############################')
#way to update the dict with new skills
new= input('do you wish to add a new value to skills dict? [y/n]')
if new == 'y':
    novel_skill= input('please input the skill name: ')
    novel_skill = novel_skill.lower()
    skills_dict[novel_skill]= {}
    print('(Thank you, Skill is now input.) \n')


#input date information for skills, and hours that day
print('### Please enter your practice habits for the day: ###\
      #######################################################')
for skill in skills_dict:
    today= date.today()
    practiceTime= input('How many hours have you practiced ' + skill + ' today? \n\n')
    #skills_dict[skill]['todays_date'] = practiceTime
    skills_dict[skill][str(today)] = practiceTime

#creates a dict of skill totals, where the values are list objects
totals= {}
for skill in skills_dict:
    totals[skill] = []
#converts the dict strings to ints, adds them to totals; sums totals
for key in skills_dict:
    for date in skills_dict[key]:
        value=float((skills_dict[key][date]))
        #and adds the values to the totals list
        totals[key].append(value)

        #sums the list values stored in each dict key of totals
    totals[key] = sum(totals[key])

print('(Total Hours Invested in Skill)\n-----------------------------')
for skill in totals:
    print("the skill of : " + skill + ':' , totals[skill])
    print("data collected since 11/29/2021")

#convert skills dict to json object
json_object = json.dumps(skills_dict, indent = 4)
#write the json object to habits.txt
with open('habits.txt', 'w+') as FILE:
    FILE.write(json_object)

close= input('Press Enter to Exit Program')
