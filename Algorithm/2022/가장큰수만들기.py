# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))


def solution(numbers):
    number_list = list(map(str, numbers))
    target = ''.join(sorted(number_list, key=lambda x: x*3, reverse=True))
    print(target)

print(solution([3,30,34,5,9]))