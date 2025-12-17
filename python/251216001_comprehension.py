# Comprehension
# - 기존 묶음자료형에 일괄적으로 작업을 수행하여 새로운 묶음 자료형을 만들어 내는 것
# Using Lambda expression

# before comprehension
nums = [1,2,3,4,5]
result = []

for num in nums:
    result.append(num*2)
print(result)

# using comprehension

result = [num * 2 for num in nums]

