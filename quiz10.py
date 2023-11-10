import random

def number():
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    return lotto_numbers

def main():
    lotto_numbers = number()
    lotto_numbers_str = lotto_numbers
    print(lotto_numbers_str)

if __name__ == "__main__":
    main()
