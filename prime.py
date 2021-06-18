import argparse
import sys 
import math

parser = argparse.ArgumentParser()
parser.add_argument("--prime", "-p", action="store_true",
                    help="check if number is prime")
parser.add_argument("--even", "-e", action="store_true",
                    help="check if number is even")
parser.add_argument("--square", "-s", action="store_true",
                    help="square a number")
parser.add_argument("--root", "-r", action="store_true",
                    help="root a number")
parser.add_argument("--autoprime", "-a", action="store_true",
                    help="find all prime numbers in custom range")
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

if args.prime:
  pnum = int(input("Enter a number => "))  
  if pnum > 1:
      for i in range(2,pnum):  
           if (pnum % i) == 0:  
            print(pnum,"is not a prime number")  
            print(i,"times",pnum//i,"is",pnum)  
            break                       
      else:  
        print(pnum,"is a prime number")
  else:  
    print(pnum,"is not prime number")    

if args.even:
  enum = int(input("Enter a number => "))  
  if enum > 1: 
      if (enum % 2) == 0:  
        print(enum,"is an even number")   
      else:
        print(enum, "is an uneven number")

if args.square:
  snum = int(input("Enter a number => "))
  sanswer = snum**2
  print(sanswer)

if args.root:
  rnum = int(input("Enter a number => "))
  ranswer = math.sqrt(rnum)
  print(ranswer)

if args.autoprime:
  lower = int(input("Enter lower range: "))  
  upper = int(input("Enter upper range: "))  
    
  for apnum in range(lower,upper + 1):  
    if apnum > 1:  
        for i in range(2,apnum):  
            if (apnum % i) == 0:  
                break  
        else:  
            print(apnum , sep=" ", end=" ", flush=True)