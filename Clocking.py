import time


def find_Pi_digits():
    start = time.time()
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        end = time.time()
        print(f"Now times = {(end - start)} sec")
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2




digits_lst = []
digit_count = 0
start = time.time()
for i in find_Pi_digits():
    digit_count += 1
    digits_lst.append(str(i))
    if digit_count == 52659:
        end = time.time()
        print("For the best computer can process 52659 task per 5 minutes")
        print(f"then my computer can do 52659 task within times : {end - start} sec ")
        break

digits_lst = digits_lst[:1] + ['.'] + digits_lst[1:]  # split to 3 len lst
print(f"Counting of digits of Pi : {digit_count}")
print(f"All digits of Pi : {''.join(digits_lst)}")
