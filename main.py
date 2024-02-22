# Write a python program to translate a message into secret code language. Use the rules below to translate normal
# English into secret code language

# Coding:
# if the word contains at least 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# a function for code an english word to a secret code language

import random as ran

while True:
    perform = input("Code/Decode: ")
    request = input("Word: ")
    requests = request.split(" ")


    def code(word: str):
        """A function to code an english word to a code word"""
        # if word is greater than 3 letters
        if int(len(word)) >= 3:
            '''
            # replace word[0] to empty space
            word.replace(word[0], '')
            '''
            # first letter
            first_letter = word[0]

            # remove the first letter
            string1 = word[1:]

            # append to last
            string2 = string1 + first_letter
            '''# add three random characters to start
            string3 = string2 + "jpm"

            # add three random characters to end
            string4 = "jpm" + string1'''
            rans1 = ["deg", "aep", "awh", "rtg", "pos"]
            rans2 = ["uio", "gtd", "qws", "poi", "frt"]

            final = ran.choice(rans1) + string2 + ran.choice(rans2)
            return final
        else:
            return word[::-1]


    def decode(word):
        if int(len(word)) < 3:
            return word[::-1]
        else:
            try:
                string = word
                first_three_char = word[:2]
                # last_three_char = first_three_char[-3:]
                last_letter = word[-4]
                final = last_letter + word[3:-4]
                return final
            except IndexError:
                print("Sorry this is already decoded")

    if __name__ == "__main__":
        # code or decode
        if perform.lower() == 'code':
            for r in requests:
                print(code(r))

        elif perform.lower() == 'decode':
            for r in requests:
                print(decode(r))

        else:
            raise NameError(f"Only code or decode but not {perform}")
