## Pattern Matching Problem: Find all occurrences of a pattern in a string.
## Input: Strings Pattern and Genome.
## Output: All starting positions in Genome where Pattern appears as a substring.

def pattern_matching_problem(pattern, genome):    
    position = []
    k = len(pattern)        
    for i in range(len(genome)):
        if pattern == genome[i: i+k]:
            position.append(str(i))            
    return " ".join(position)
    
string = "".join(open("./data/pattern_matching_problem.txt")).split()
pattern_matching_problem(string[0], string[1])
