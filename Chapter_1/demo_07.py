n = 1000
k = 0

# 第一部分时间复杂度为O(n)
if n >= 0:
    for a in range(n):
        k += 1

# 第二部分时间复杂度为O(n²)
else:
    for a in range(n):
        for b in range(n):
            k += 1

print(k)
