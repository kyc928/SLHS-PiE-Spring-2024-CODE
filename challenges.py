"""
Pioneers in Engineering Spring 2024 Coding Challenges Starter Code
"""

# Question 1
def delivery(lst: list) -> int:
    hist = {"Ordinary Prisoner": 1, "Pugilist Prisoner": 2,  "Herculean Prisoner": 3, "Recidivist": 4, "Infamous Recidivist": 5}
    meals = 1
    for p in lst:
        if p in hist:
            meals += hist[p]
    return meals


# Question 2
def prisoners_list(lst: list) -> list:
    lst.sort() #not necessary
    return list(dict.fromkeys(lst))


# Question 3
def check_for_contraband(belongings):
    contraband = tuple(["knife", "drugs", "weapons", "cellphone", "alcohol","Knife", "Drugs", "Weapons", "Cellphone", "Alcohol"])
    check = list()
    final = [True, check]
    for x in belongings:
        if x in contraband:
            final[0] = False
            check.append(x)
    return tuple(final)

# Question 4
def hop(n) -> int:
    a = 1
    b = 1
    for i in range(n-1):
        temp = a
        a = a+b
        b = temp
    return a


# Quetsion 5
def survival_points(dict1, dict2) -> dict:
    final = dict()
    for key in dict1:
        final[key] = dict1[key] + dict2.get(key, 0)
    for key in dict2:
        if key not in final:
            final[key] = dict2[key]
    
    return final


# Question 6
visitation_slots = [
    ("09:00", "10:00"),
    ("10:00", "11:00"),
    ("11:00", "12:00"),
    ("13:00", "14:00"),
    ("14:00", "15:00")]

visitors = {slot: None for slot in visitation_slots}


def display_schedule():
    for slot, visitor in visitors.items():
        print(f"{slot}: {visitor or 'Available'}")

def add_visitor(slot, visitor_name):
    if slot in visitation_slots:
        if visitors[slot] is None:
            visitors[slot] = visitor_name
    display_schedule()


# Question 7
def acquaintance(id1, id2, *lists) -> bool:
    for l in lists:
        if id1 in l and id2 in l:
            return True
        
    common_1 = set()
    common_2 = set()
    for l in lists:
        if id1 in l and len(l) > 3:
            common_1.update(l)

    for l in lists:
        if id2 in l and len(l) > 3:
            common_2.update(l)

    common = common_1 & common_2

    return False or len(common) >= 3


# Question 8
def multiply_list(lst: list) -> int:
    product = 1
    for i in lst:
        product *= i
    return product


def ssspookyyyy(str: str) -> list:
    n = len(str)
    dp = [(float('inf'), 0) for _ in range(n + 1)]
    dp[0] = (0, 0)  
    for i in range(1, n + 1):
        for j in range(max(0, i - 4), i - 1):
            chunk = str[j:i]
            if len(chunk) < 2 or len(set(chunk)) == 1 and len(chunk) > 3:
                continue 
            prev_splits, prev_max_chunk = dp[j]
            current_chunk_length = i - j
            if prev_splits + 1 < dp[i][0] or (prev_splits + 1 == dp[i][0] and current_chunk_length > dp[i][1]):
                dp[i] = (prev_splits + 1, max(prev_max_chunk, current_chunk_length))

    result = []
    i = n
    while i > 0:
        for j in range(max(0, i - 4), i - 1):
            chunk = s[j:i]
            if len(chunk) < 2 or len(set(chunk)) == 1 and len(chunk) > 3:
                continue
            if dp[i][0] == dp[j][0] + 1 and dp[i][1] == max(dp[j][1], len(chunk)):
                result.append(chunk)
                i = j
                break

    return list(reversed(result))