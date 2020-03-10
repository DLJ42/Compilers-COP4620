import re as re
import sys

keywords = ("else", "if", "int", "void", "while", "return")
operators = ("+", "-", "*", "/")
relation = ("<", ">", "=", "<=", ">=", "==", "!=")
special = (";", ",", "(", ")", "[", "]", "{", "}", "/*", "*/", "//")
#symbols = ("+", "-", "*", "/", "<", "<=", ">", ">=", "==", "!=", "=", ";", ",", "(", ")", "[", "]", "{", "}", "/*", "*/")

# read input file and check if its given at runtime ex. "pgm input"
def scanner():
    try:
        input_file = sys.argv[1]
        # Read each input line into variable
        with open(input_file, "r") as f:
            input_code = f.readlines()

        # analysize each line and tokenize recognized character string (no floats, no pointers, no signed ints)
        # ignore comments
        # white space separates IDs, NUMS, and keywords
        # ex. tokens: keywords (else, if, int, void, while, return), IDs ([a-zA-Z]+)
        # ID = 1 or more letters
        # NUMS = 1 or more digits
        # spaces are delimeters for tokens (i.e. spaces separate tokens)
        # read each line character by character

        comment_started = False

        with open("tokens.txt","w") as f1:
            # loop through each line of code
            for line in input_code:
                #print(line)

                # remove leading/trailing \n
                line = line.strip()
                #if line:
                    #print("INPUT: " + line)
                
                # split each line into an array of strings using specified regex delimeters
                line_array = re.split(r'([a-zA-Z]+|\d+|\-|\+|\=\=|\=|\<\=|\<|\>\=|\>|\!\=|\s+|//|\/\*?|\*\/?|\;|\,|\(|\)|\[|\]|\{|\}|[\@\_\~\`\!\#\$\%\^\&\:\|\\\"\'\.\?a-zA-Z\d]+[a-zA-Z\d]*)', line)

                #line_array = re.split(r'(.*[a-zA-Z]+.*)', line)
                #line_array = re.split(r'([a-zA-Z]+|\-|\+|\=\=|\=|\<\=|\<|\>\=|\>|\!\=|\s+|//|\/\*?|\*\/?|\;|\,|\(|\)|\[|\]|\{|\}|[a-zA-Z]*[\@\_\~\`\!\#\$\%\^\&\:\|\\\"\'\.\?a-zA-Z]*[a-zA-Z\d]+$)', line)
                #line_array = re.split(r'(\s+|//|\+|\-|\/\*?|\*\/?|\<\=|\<|\>\=|\>|\=\=|\!\=|\=|\;|\,|\(|\)|\[|\]|\{|\}|^[a-zA-Z]+|^[\-\?\@\_\~\`\!\#\$\%\^\&\:\|\\]+[\w\d\s]*$)', line)
                #line_array = re.split(r'(\s+|//|\+|\-|\/\*?|\*\/?|\<\=|\<|\>\=|\>|\=\=|\!\=|\=|\;|\,|\(|\)|\[|\]|\{|\}|^[a-zA-Z]+|^[\-\?\@\_\~\`\!\#\$\%\^\&\:\|\\]+[\w\d\s]*$)', line)

                # rebuild code line array after removing elements that are empty or filled with one or more spaces
                line_array = ' '.join(line_array).split()

                #print(line_array)

                # if line of code is empty, skip it
                if len(line_array) == 0:
                    continue
                else:
                    for string in line_array:
                        if comment_started == True:
                            if re.match(r'^.?\*\/$', string):
                                comment_started = False
                                #print("^^ ended comment")
                            else:
                                continue
                        else:
                            # if sttring is an open/close comment (e.g. /* hsbejuhb */)
                            if re.match(r'^\/\*.*\*\/$', string):
                                continue
                            # if string is a single line comment omit everything after it (break out of loop)
                            elif re.match(r'//', string):
                                break
                            # if string started a multi-line comment
                            elif re.match(r'^\/\*+$', string):
                                #print("^^ comment started")
                                comment_started = True
                            # if string ends multiline comment
                            elif re.match(r'^.+\*\/', string) and comment_started == True:
                                #print("^^ comment ended")
                                continue
                            # if string matches a keyword
                            elif string in keywords:
                                #print("KW: " + string)
                                f1.writelines("KW: " + string + "\n")
                            # if string is an operator
                            elif string in operators:
                                #print(string)
                                f1.writelines(string + "\n")
                            # if string is a relation
                            elif string in relation:
                                #print(string)
                                f1.writelines(string + "\n")
                            # if string is special character not in operators or relations
                            elif string in special:
                                if len(string) > 1:
                                    for c in string:
                                        #print(c)
                                        f1.writelines(c + "\n")
                                else:
                                    #print(string)
                                    f1.writelines(string + "\n")
                            elif re.match(r'[a-zA-Z]+', string):
                                #print("ID: " + string)
                                f1.writelines("ID: " + string + "\n")
                            # if character is a NUM (a numeric-only string)
                            elif re.match(r'^[0-9]+$', string):
                                #print("INT: " + string)
                                f1.writelines("INT: " + string + "\n") 
                            else:
                                #print("Error: " + string)
                                f1.writelines("Error: " + string + "\n")
    except:
        print("No input file given")    



