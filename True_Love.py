# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1.lower()
name1Count_T = name1.count("t")
# name1Count_R = name1.count("r")
# name1Count_U = name1.count("u")
# name1Count_E = name1.count("e")
# name1Count_L = name1.count("l")
# name1Count_O = name1.count("o")
# name1Count_V = name1.count("v")
# name1Count_E = name1.count("e")


if name1Count_T > 0 and name1Count_R > 0:
  print (f"T occurs {name1Count_T} times")
  # print (f"R occurs {name1Count_R} times")
# elif name1Count_R > 0:
#   print (f"R occurs {name1Count_R} times")
# elif name1Count_U > 0:
#   print (f"U occurs {name1Count_U} times")
# elif name1Count_E > 0:
#   print (f"E occurs {name1Count_E} times")
# elif name1Count_L > 0:
#   print (f"L occurs {name1Count_L} times")
# elif name1Count_O > 0:
#   print (f"O occurs {name1Count_O} times")
# elif name1Count_V > 0:
#   print (f"V occurs {name1Count_V} times")
# elif name1Count_E > 0:
#   print (f"E occurs {name1Count_E} times")
else:
  print ("No")

# print (f"T occurs {name1Count_T} times")

# print (name2.lower())