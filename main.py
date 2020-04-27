from rome_numerals import Rim  # Importing our class RomeNumerals.

print("I am a program that can work with Roman numbers.\n"
      "If you want end this program, write: \" exit \" " "\n"
      "Please enter your Roman number!")
key = True

while key:  # Entering a number in the loop.
      
    try:    
        number_1 = input("\t")
        number_2 = input("\t")
        if number_1 == "exit" or number_2 == "exit":
            key = False
            break
        num_rim_1 = Rim(number_1)
        num_rim_2 = Rim(number_2)
            
    except ValueError:
        print("You entered an invalid numbers. Please, try again")
        continue
      
    try:
        if num_rim_1.__str__() == 'None' or num_rim_2.__str__() == 'None':
                  
            print("You entered an invalid number. Please, try again")
            continue
            
        print("\tYour numbers: ", number_1, number_2)
        print("\tConvert numbers: ", num_rim_1.__str__(), num_rim_2.__str__())
        print("\tSum: ", num_rim_1 + num_rim_2)
        print("\tSub: ", num_rim_1 - num_rim_2)
        print("\tMul: ", num_rim_1 * num_rim_2)
        print("\tTruediv: ", num_rim_1 / num_rim_2)
        print("\tFloordiv: ", num_rim_1 // num_rim_2)
        print("\tMod: ", num_rim_1 % num_rim_2)
        print("\tFirst more them Second? ", num_rim_1 > num_rim_2)
        print("\tFirst equals Second? ", num_rim_1 == num_rim_2)
        print("\tFirst less them Second? ", num_rim_1 < num_rim_2)

    except KeyError:
      
        print("You entered an invalid numbers. Please, try again")
        continue
