'''
Vincent Fazio
CSC 2343-01 
2/28/20
Lab4 - Sequences

This program takes the user inputted sequence and determines whether it is a geometric, arithmetric, or unknown sequence.
'''

def unknown(seq):
   # Finding the common difference, in two places
   D = (int(seq[1]) - int(seq[0]))
   Dcheck = (int(seq[2]) - int(seq[1]))

   D2 = (int(seq[1]) / int(seq[0]))
   D2check = (int(seq[2]) / int(seq[1]))

   # If the difference isnt the same then this can't be arithmetic/geometric
   if(D != Dcheck):
      print(seq,"is an unknown sequence.")
      exit(1)
   elif(D2 != D2check):
      print(seq,"is an unknown sequence.")
      exit(1)

def arith(seq):
   # Finding the common difference
   D = (int(seq[1]) - int(seq[0]))
   
   #If the common difference is the same through, it is arithmetic, else its unknown
   if(D == (int(seq[2]) - int(seq[1]))):
      print(seq,"is an arithmetic sequence.") 
      exit(1) 
 
def geometric(seq):
   # Finding the common difference
   D = (int(seq[1]) / int(seq[0]))
  
   #If the common difference is the same through, it is geometric, else its unknown
   if(D == (int(seq[2]) / int(seq[1]))):
      print(seq,"is an geometric sequence.") 
      exit(1)

#User input
print("Example Input: 1,3,5,7")
seq = input("Enter an Arithmetic/Geometric sequence: ")
seq = seq.split(",")

# Function Calls
arith(seq)
geometric(seq)
unknown(seq)
