import json
import difflib
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm
data = json.load(open("data/data.json"))

def meaning(U_input):
    if U_input.lower() in data:
        return data[U_input.lower()]

            
    else:
        return "There is no such word"
    

#########################################################
########### EITHER I COULD DO IT LIKE THESE #############
#########################################################
# def word_corrector(us_in):
#     for i in data.keys():
#         a = sm(None, us_in, i).ratio()
#         if a > 0.8:
#             text = i
#             i1 = 'y'
#             inp = input("\nDid you mean {} press yes: 'Y' and no: 'N'".format(i))
#             if inp == i1:
#                  return meaning(text)
#                  break
#             else:
#                  return "There is no such word"
#                  break
             
#########################################################
########### OR I COULD DO IT LIKE THESE #################
#########################################################

def word_corrector(us_in):
    if us_in in data.keys():
        return meaning(us_in)
    else:
        a = gcm(us_in, data.keys())[0]
        inp = input("did you mean {}: press 'y' for yes and 'n' for no:".format(a))
        if inp == 'y':
            text = a
            return meaning(text)
        else:
             return "There is no such word"    
             

user_input = input("Enter a word : ")

output = word_corrector(user_input)
if type(output) == list:
    count = 0
    print("Meaning:")
    for item in output:
        count = count + 1
        print("{}. ".format(count)+item)
else:
    print(output)