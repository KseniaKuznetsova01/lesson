from RomeNumerals import Rim                                            # Importing our class RomeNumerals.

print("I am a program that can work with Roman numbers.\n"
      "If you want end this program, write: \" exit \" " "\n"
      "Please enter your Roman number!")
key = True

while key:                                                              # Entering a number in the loop.
    number = input("\t")
    if number == "exit":
        key = False
        break
    num_rim = Rim(number)
    try:
      if num_rim.__str__() == 'None':
          print("You entered an invalid number. Please, try again")
          continue
      print("\tYour number: ", number)
      print("\tConvert number: ", num_rim.__str__())
    except KeyError:
        print("You entered an invalid number. Please, try again")
        continue
