file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 17\\Day17.txt', 'r')

for line in file:
    if line == "\n":
        break

out = []
instructions = []

for line in file:
    for char in line:
        if char.isdigit():
            instructions += char

def run_prog_for_a(a: int) -> list:
    """ Program [2, 4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0] 
    converted to simplified Python instructions. """
    
    b = c = 0 # Both B and C are completely dependent on the value of A so their initial value is indifferent
    out = []
    
    while a:
        b = a % 8 
        b = b ^ 6 
        c = a // 2**b 
        b = b ^ c 
        b = b ^ 7 
        a = a // 2**3 # ONLY OPERATION THAT CHANGES A!!!
        out.append(b % 8) 
        
    return out

valid_vals_for_a = {0} 

for instruction in reversed(instructions): 
    next_vals_for_a = set()
    
    for a_val in valid_vals_for_a:
        a_shifted = a_val * 8 # Equivalent to left shift by 3, so can now add any three bits
        
        for candidate_a in range(a_shifted, a_shifted+8): # Try all 8 values of a+modifier
            out = run_prog_for_a(candidate_a) # Run single cycle
            if out and out[0] == int(instruction): # If we've output the required value
                next_vals_for_a.add(candidate_a) # this value is good
                
    valid_vals_for_a = next_vals_for_a

print(min(valid_vals_for_a))
  
