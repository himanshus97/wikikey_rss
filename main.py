#!/usr/bin/env python3
"""
Main.py
used to run whole code in systematic manner, it takes 2 optional arguments
regex or soup just for demonstration of two implementations.

References
-> https://www.tutorialspoint.com/python/python_command_line_arguments.htm
"""
import sys,getopt
import rsstitle

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:],"ho:",["option="])
    except getopt.GetoptError:
        print("----Please Enter Valid input----")
        print(f'{__file__} -o soup OR regex')
        sys.exit(2)

    if(len(opts)!=0):
        for opt, arg in opts:
            if opt == '-h':
                print("\t\t----HELP----")
                print(f'{__file__} -o soup OR regex')
                sys.exit()
            elif opt in ("-o", "--option"):
                if arg == 'soup':
                    print("_____RUNNING RSS TITLE EXTRACTION USING BEAUTIFULSOUP____")
                    rsstitle.soup()
                    print("_____EXTRACTION DONE____")
                elif arg == 'regex':
                    print("_____RUNNING RSS TITLE EXTRACTION USING REGEX____")
                    rsstitle.regex()
                    print("_____EXTRACTION DONE____")
                else:
                    print("----Please Enter Valid input----")
                    print(f'{__file__} -o soup OR regex')
                    sys.exit()
    else:
        print("----Please Enter Valid input----")
        print(f'{__file__} -o soup OR regex')
        sys.exit()
