#!/usr/bin/python3

# Reference: https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/howto/argparse.html
import argparse


argparser = argparse.ArgumentParser(prog='arg_parse.py', 
                                    description='Template for Argument Parser in Python Codes using Argparse')

# This is a positional Argument, which would mean a mandatory one.
# If there are more than one Positional arguments, their ordering is important.
# However Positional and Optional Arguments do not need ordering
# Positional arguments do not have short options.
argparser.add_argument( "greetings",
                        help = "Displays greetings on Program executaion")


# By default the arguments that we supply are strings,
# so we need to specfy if we are expecting an integer.
# Short options need not be single character
# Note: '--' can be used to identify if it is a positional or an optional argument
# If an optional argument is not passed its default Value is 'NONE' if printed.
argparser.add_argument("-sq",
                        "--square",
                        help = "Displays the square of the specified integer",
                        type = int)


# Single Inverted Commas can be used in place of Double Inverted Commas
# Action=store_true sets the args.verbose value to TRUE without specify any value
# For example: ./arg_parse -v should be sufficient to display verbosity,
# If action = "store_true" was not specified, 
# then "./arg_parse -v 1(keep in mind that this is a string value)" would have been required to pass the if loop in the code below
argparser.add_argument("-v",
                        "--verbose",
                        action = "store_true",
                        help = "Sets Verbosity")

# If type = int is not specified, then we need to use string to compare            
argparser.add_argument("-p",
                        "--points",
                        help = "Outputs shape drawn using the input points",
                        type = int,
                        choices=[0,1,2,3,4])

#TODO: Add more examples
#argparser.add_argument('--test',
#                        action='store_true',
#                        help='Run tests : This would reflash the device and then run tests')
#

args = argparser.parse_args()

# This will print the first command line argument 'greetings' with the value passed
print(args.greetings)

if args.square:
    if args.verbose:
        print("Square of {} is {}".format(args.square, args.square**2))
    else:    
        print("Result:", args.square**2)

if args.points == 0:
    print("Blank")
elif args.points == 1:
    print("Shape is Line")
elif args.points == 2:
    print("Shape is Line")
elif args.points == 3:
    print("Shape is Triangle")
elif args.points == 4:
    print("Shape is Square")