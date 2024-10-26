
while True:
    
    user_input = int(input("Please input a number between 1 and 50 (to exit input any other numbers):"))
    
    if user_input < 1 or user_input > 50:

        break

    range_1_10 = 0
    range_11_20 = 0
    range_21_30 = 0
    range_31_40 = 0
    range_41_50 = 0

    if 1 <= user_input <= 10:
        range_1_10 += 1

    elif 11 <= user_input <= 20:
        range_11_20 += 1

    elif 21 <= user_input <= 30:
        range_21_30 += 1

    elif 31 <= user_input <= 40:
        range_31_40 += 1

    elif 41 <= user_input <= 50:
        range_41_50 += 1

print("Number of inputs in each range:")
print(f"1 - 10  = {range_1_10}")
print(f"11 - 20 = {range_11_20}")
print(f"21 - 30 = {range_21_30}")
print(f"31 - 40 = {range_31_40}")
print(f"41 - 50 = {range_41_50}")
