# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:38:58 2020

@author: Ma. Angelica Mariano
"""

# Give the user some context.
print("\nTest how much you know about physics by trying our fun physics quiz. \n\nPlease input your name below-")

#ask details about the quiz taker
name = input("Name: ")
print("\nHello, ",name+"! - Lets begin the test!")

###### Functions ######
def checker(cor_ans,input_res,score):
  if cor_ans == input_res:
    score = score + 1
    return score
  else:
    return score

def pass_fail(fin_score):
  a = fin_score/len(questions)
  if a >= .7:
    print ("\nYou passed! Congrats. Thank you!")
  else:
    print("\nYou failed, you may try again. Thank you!")


###### Main ######
questions = ["\nQuestion #1:\nWhen light bends as it enters a different medium the process is known as what? \na. Reflection \nb. Refraction \nc. Diffraction",
             "\nQuestion #2:\nA magnifying glass is what type of lens? \na. convex \nb. concave \nc. meniscus",
             "\nQuestion #3:\nIron is what type of magnetic material? \na. diamagnetic \nb. paramagnetic \nc. ferromagnetic",
             "\nQuestion #4:\nElectric current is typically measured in what units? \na. joules \nb. amperes \nc. megacurie",
             "\nQuestion #5:\nWho is the Hubble Space Telescope named after? \na. Edwin Hubble \nb. Edward Hubble \nc. Galileo Galilei",
             "\nQuestion #6:\nInfrared light has a wavelength that is too long or short to be visible for humans? \na. long \nb. short \nc. 3.14mm",
             "\nQuestion #7:\nWhat kind of eclipse do we have when the moon is between the sun and the earth? \na. Lunar eclipse \nb. Solar eclipse \nc. Twilight",
             "\nQuestion #8:\nThe most recognized model of how the universe begun is known as the? \na. Evolution \nb. Big Bang Theory \nc. Theory of Relativity ",
             "\nQuestion #9:\nMetals expand when heated and do what when cooled? \na. expand \nb. contract \nc. stay the same",
             "\nQuestion #10:\nWhat is the name of the famous scientist who gave us Three Laws of Motion? \na. Isaac Newton \nb. Albert Einstein \nc. John Dalton"] 
cor_ans = ['b','a','c','b','a','a','b','b','b','a']

fin_score = 0
length = len(questions)

for i in range(length): 
  print(questions[i])
  response = input("Input your answer:")
  fin_score = checker(cor_ans[i],response,fin_score)

print("\n\nYour score is " + str(fin_score) + " out of "+ str(length))

pass_fail(fin_score)