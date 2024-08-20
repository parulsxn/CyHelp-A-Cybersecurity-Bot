#CyHelp Starter Code
cyberSecurityBirthYear = 1970

#Greets user
print("Hello! I'm CyHelp.\n")
userName = input("What is your name?\n")
print("\nNice to meet you " + userName + "!\n")

#Recounts start of Cybersecurity
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - cyberSecurityBirthYear
print("\nWow! That means it has been " + str(timePassed) + " years since Cybersecurity began!\n")
 


print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!\n")

input("Press enter to continue.\n")


#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.These people can be government, nations, companies, community, organizations, individuals and hackers.\n")


#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for Confedentiality, Integrity and Availabilty.\n")

print("Would you like to learn about the CIA Triad?")
giveInfo = input("Type 'yes' or 'no'\n")


#Explains pillars of CIA Triad
while giveInfo.lower() == "yes" : 
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options:\n (a) confidentiality, (b) integrity, (c) availability or (d) none")
  topic = input("")
  if topic.lower() == "a":
    print("\nConfidentiality makes sure data is private.\n")
  
  elif topic.lower() == "b":
    print("\nIntegrity makes sure data has not been tampered with and can be trusted.\n")
  
  elif topic.lower() == "c":
    print("\nAvailability makes sure authorized people can access the data.\n")
  
  elif topic.lower() == "d":
    print("\nOkay.\n")
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  # input("Press enter to continue.\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")