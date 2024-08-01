input_numbers: list[int] = [int(x) for x in input().split()]

result: int = sum(integer for integer in input_numbers if integer % 2 == 0)

print(result)
