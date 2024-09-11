import itertools


def solve_cryptarithmetic():
    
    letters = 'SENDMOREY'

    
    for perm in itertools.permutations('0123456789', len(letters)):
        
        assignment = {letter: int(digit) for letter, digit in zip(letters, perm)}
        
    
        s = assignment['S']
        e = assignment['E']
        n = assignment['N']
        d = assignment['D']
        m = assignment['M']
        o = assignment['O']
        r = assignment['R']
        y = assignment['Y']

    
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

    
        if send + more == money and s != 0 and m != 0:
            print(f"SEND: {send}")
            print(f"MORE: {more}")
            print(f"MONEY: {money}")
            print(f"Solution: {assignment}")
            return assignment

    print("No solution found")


solve_cryptarithmetic()
