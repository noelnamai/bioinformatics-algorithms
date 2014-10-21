## Python function that finds the most frequent k-mers in a string given a DNA string Text and an integer k.

## Find the most frequent k-mers in a string.
## Input: A string Text and an integer k.
## Output: All most frequent k-mers in Text.

def frequent_words_problem(text, k):
    count = []
    frequent_patterns = []
    for i in range(len(text) - k):
        pattern = text[i : k+i]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
    for i in range(len(text) - k):
        if count[i] == max_count:
            frequent_patterns.append(text[i : k+i])            
    return set(frequent_patterns) 

string = "".join(open("./data/frequent_words_problem.txt")).split()
frequent_words_problem(string[0], int(string[1]))
