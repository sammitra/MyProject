import sys
sys.path.append('/MyModule/')
import MyModule
from MyModule.mathy import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Enter Your Messsage(Two Numbers Are Necessary)")
    for word in text.split(' '):
            if word.upper() in operations.keys():
                try:
                   print("Your Results Are Below")
                   l=numberExtractor(text)
                   r=operations[word.upper()](l[0],l[1])
                   print(r)
                except:
                   Sorry()
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
    else:
        Sorry()

