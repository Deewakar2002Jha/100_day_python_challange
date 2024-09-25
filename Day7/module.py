 
import argparse

parser = argparse.ArgumentParser{
    description='this program print the name of my dogs'
}
parser.add_argument('-c','--color',metavar='color',
    required= True, help='the color to search for')

args = parser.parse_args()


print(args.color)
