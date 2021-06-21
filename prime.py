import argparse
import sys 
import math
import os

parser = argparse.ArgumentParser(description = "https://github.com/NiekGevers/primecalc")
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
parser.add_argument("--prime2file", "-p2f", action="store_true",
                    help="find all prime numbers in custom range and put them in primes.txt")
parser.add_argument("--percentages", "-%", action="store_true",
                    help="calculate with percentages")
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

if args.prime:
  os.system('cls||clear')
  pnum = int(input("Enter a number => "))  
  if pnum > 1:
      for i in range(2,int(math.sqrt(pnum))):  
           if (pnum % i) == 0:  
            print(pnum,"is not a prime number")  
            print(i,"times",pnum//i,"is",pnum)  
            break                       
      else:  
        print(pnum,"is a prime number")
  else:  
    print(pnum,"is not prime number")    

if args.even:
  os.system('cls||clear')
  enum = int(input("Enter a number => "))  
  if enum > 1: 
      if (enum % 2) == 0:  
        print(enum,"is an even number")   
      else:
        print(enum, "is an uneven number")

if args.square:
  os.system('cls||clear')
  snum = int(input("Enter a number => "))
  sanswer = snum**2
  print(sanswer)

if args.root:
  os.system('cls||clear')
  rnum = int(input("Enter a number => "))
  ranswer = math.sqrt(rnum)
  print(ranswer)

if args.autoprime:
  os.system('cls||clear')
  lower = int(input("Enter lower range: "))  
  upper = int(input("Enter upper range: "))  
    
  for apnum in range(lower,upper + 1):  
    if apnum > 1:  
        for i in range(2,int(math.sqrt(apnum))):  
            if (apnum % i) == 0:  
                break  
        else:  
            print(apnum , sep=" ", end=" ", flush=True)

if args.prime2file:
  os.system('cls||clear')
  lower = int(input("Enter lower range: "))  
  upper = int(input("Enter upper range: "))  
    
  for p2fnum in range(lower,upper + 1):  
    if p2fnum > 1:  
        for i in range(2,int(math.sqrt(p2fnum))):  
            if (p2fnum % i) == 0:  
                break  
        else:  
            f = open("primes.txt", "a")
            f.write(str(p2fnum)+" ")
            f.close()
            print("succesfully added",p2fnum, "to primes.txt")

if args.percentages:
  os.system('cls||clear')
  print("1. what is ... % of ...")
  print("2. ... is what percentage of ...")
  print("3. What is the increase/decrease in percentage of ... to ...")
  procquestion = input("choose option 1/2/3 => ")
  if procquestion == ("1"): 
    os.system('cls||clear')
    print("what is (1)% of (2)")
    question1a = int(input("(1) => "))
    question1b = int(input("(2) => "))
    print(question1b/100*question1a)
 
  elif procquestion == ("2"):
    os.system('cls||clear')
    print("(1) is what percentage of (2)")
    question2a = int(input("(1) => "))
    question2b = int(input("(2) => "))
    print(question2a/question2b*100, "%")
 
  elif procquestion == ("3"):
    os.system('cls||clear')
    print("what is the increase/decrease in percentage of (1) to (2)")
    question3a = int(input("(1) => "))
    question3b = int(input("(2) => "))
    print(100*question3b/question3a, "%")
  
  else:
    print("please select 1,2 or 3")
