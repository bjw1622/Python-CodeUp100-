from random import randint

def generate_numbers(n):
    numbers = []
    while len(numbers) < n :
        a = randint(1,45)
        if a not in numbers:
            numbers.append(a)
    return numbers

def draw_winning_numbers():
    new_numbers = generate_numbers(6)
    new_numbers.sort()
    a = randint(1,45)
    if a not in new_numbers:
        new_numbers.append(a)
    return new_numbers

def count_matching_numbers(numbers, winning_numbers):
    # 코드를 작성하세요.
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count+=1
    return count
def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    count = count_matching_numbers(numbers,winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers,winning_numbers[6:])
    if count == 6:
        return 1000000000
    elif count ==5 and bonus_count==1:
        return 50000000
    elif count ==5:
        return 1000000
    elif count ==4:
        return 50000
    elif count ==3 :
        return 5000

# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))