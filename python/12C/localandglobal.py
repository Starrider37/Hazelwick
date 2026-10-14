score = 0

def add_points(points):
    bonus = 5
    total = total+bonus
    return total
def add_to_score(points):
    global score
    score = score+points

result = add_points(10)
print(result)
add_to_score(result)
print(score)
print(bonus)