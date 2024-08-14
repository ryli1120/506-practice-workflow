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
 
    bmi = (weight/(height ** 2))*703
 
    if bmi < 18.5:
     return f"Your BMI is {bmi:.2f}. You are underweight."
    elif 18.5 <= bmi < 24.9:
     return f"Your BMI is {bmi:.2f}. You are at a healthy weight."
    elif 25 <= bmi < 29.9:
     return f"Your BMI is {bmi:.2f}. You are at a overweight."
    else:
      return f"Your BMI is {bmi:.2f}. You are obese."


#Test
underweight = checkBMI(110, 68)
healthy_weight = checkBMI(154,69)
overweight = checkBMI(200, 70)
obese = checkBMI(250,66)

print(underweight)
print(healthy_weight)
print(overweight)
print(obese)
