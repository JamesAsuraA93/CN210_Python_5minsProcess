import time


def find_Pi_digits():
    start = time.time()
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        end = time.time()
        if (end - start) >= 600:  # (sec) : 600 sec = 5 minutes
            print(f"Now times = {(end - start)} sec")
            break
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


digits_lst = []
digit_count = 0
for i in find_Pi_digits():
    digit_count += 1
    digits_lst.append(str(i))

digits_lst = digits_lst[:1] + ['.'] + digits_lst[1:]  # split to 3 len lst
print("For approximated 5 minutes this is result")
print(f"Counting of digits of Pi : {digit_count}")
print(f"All digits of Pi : {''.join(digits_lst)}")
