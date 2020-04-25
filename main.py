from rome_numerals import Rim                                            # Importing our class RomeNumerals.

print("I am a program that can work with Roman numbers.\n"
      "If you want end this program, write: \" exit \" " "\n"
      "Please enter your Roman number!")
key = True

while key:                                                              # Entering a number in the loop.
    number_1 = input("\t")
    number_2 = input("\t")
    if number_1 == "exit" or number_2 == "exit":
        key = False
        break
    num_rim = Rim(number_1,number_2)

    try:
      if num_rim.__str__() == 'None':
          print("You entered an invalid number. Please, try again")
          continue
      print("\tYour numbers: ", number_1, number_2)
      print("\tConvert numbers: ", num_rim.__str__())
    except KeyError:
        print("You entered an invalid numbers. Please, try again")
        continue
