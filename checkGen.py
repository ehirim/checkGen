print("😳 Let's Identify your Generation 🤪")
print()
birthYear = int(input("What year were you born? "))
if (birthYear < 1883) and (birthYear <= 1900):
  print("Hmmm! How are you still alive? Your Generation is the \033[31mLost Generation\033[0m, Wow!")
elif (birthYear >= 1901) and (birthYear <= 1927):
  print("Okay, they call this the \033[36mGreatest Generation\033[0m! 🤔")
elif (birthYear >= 1928) and (birthYear <= 1945):
  print("The \033[35mSilent Generation\033[0m. How quiet are you? 😶")
elif (birthYear >= 1946) and (birthYear <= 1964):
  print("Aha! And to think this modern generation likes fornicating... Why was this called \033[35mBaby Boomers\033[0m. Duh! 👶")
elif (birthYear >= 1965) and (birthYear <= 1980):
  print("\033[34mGeneration X\033[0m. Your Era sounds like a movie title! 🤟")
elif (birthYear >= 1981) and (birthYear <= 1996):
  print("\033[34mMillenials\033[0m. You sure are the real MVPs 💯")
elif (birthYear >= 1997) and (birthYear <= 2012):
  print("For real yo! Coping with you \033[34mGeneration Z (Gen Zee)\033[0m is like dealing directly with a GOAT! 🐐")
elif (birthYear > 2013):
  print("\033[34mGeneration Alpha\033[0m. I really feel sorry for you all because things are so wrong and it is affecting your brains 😭")
else:
  print("Like really, are you alive? Yo call the ghostbusters down here.")
