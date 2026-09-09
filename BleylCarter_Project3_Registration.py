#Name: Carter Bleyl
#Class: INFO 1200
#Section: X02
#Professor: Noah Say
#Date: Insert date submitted
#Project #: Insert project number
'''
By submitting this assignment, I declare that the source code contained in this assignment was written
solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
instructions, nor obtained from a subscription service. I understand that copying any source code,
in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
I will receive a zero on this project if I am found in violation of this policy.
'''



print("Carter Bleyl Registration App") #introduce app
print()

firstName = (input("Please enter your first name: ")) #input first name 
lastName = (input("Please enter your last name: "))#input last name
birthYear = (input("Please enter your birth year: "))#input birth year
print()

print("Welcome", firstName, lastName, "!") #welcome based off name input
print("Your registration is complete")  #display text

tempPassword = (firstName + "*" + birthYear) #concat password
print("Your temporary password is: ", tempPassword) #display temp password
