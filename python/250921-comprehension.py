# Comprehension

# 설명

# Before comprehension

nums = [1,2,3,4,5]
result = []

for i in nums:
    if i % 2 == 0:
        result.append(i*2)

# with comprehension

# 할일 - 대상 - 조건 순 으로 나열
result = [i * 2 for i in nums if i % 2 == 0]

