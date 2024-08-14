import pandas as pd
import numpy as np

number = 17
name = "Ryan"

names_List = ["John", "Jeff", "Jesse", name]

Animals = {
 "Mammals": ["dog", "cat", "horse"],
 "Reptiles":{
   "Snakes": ["python", "cobra", "rattlesnake"]
 },
  "Amphibian": "Frog"
}

def checkBMI(weight, height):
 
  bmi = weight/(height **2)*703
 
if bmi < 18.5:
  return("Your BMI is " + bmi + ". You are underweight.")
elif 18.5<= bmi < 24.9:
  return ("Your BMI is " + bmi + ". You are at a health weight.")
elif 25 <= bmi 29.9:
  return ("Your BMI is " + bmi + ". You are at a overweight.")
else:
  return ("Your BMI is " + bmi + ". You are obese.")


#Test
checkBMI(70, 1.75)
print(result)
