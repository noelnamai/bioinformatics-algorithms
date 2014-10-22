## Python function that finds the reverse complement of a DNA string given a DNA string Pattern. 
## Reverse Complement Problem: Find the reverse complement of a DNA string.
## Input: A DNA string Pattern.
## Output: Pattern, the reverse complement of Pattern.
                
def reverse_complement_problem(string):    
    dictionary = {"A":"T", "T":"A", "C":"G", "G":"C"}
    output = [dictionary[x] for x in string[::-1]]
    return "".join(output)
    
string = "".join(open("./data/reverse_complement_problem.txt")).split()
reverse_complement_problem(string[0])
