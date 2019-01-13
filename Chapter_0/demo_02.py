# 已知a+b+c=1000，且a^2+b^2 =c^2，求a，b，c的所有自然数解

import time

start_time = time.time()

for a in range(1, 1001):  # 第一层
    for b in range(1, 1001):  # 第二层
        if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
            print('a:%3d, b:%3d, c:%3d' % (a, b, 1000 - a - b))

end_time = time.time()
print("程序已完成，总计用时: %f" % (end_time - start_time))