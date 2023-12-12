import re

def main():
    file = open("day1A.txt", "r")

    digits = []
    while True:
        line = file.readline()
        # break if no lines
        if not line:
            break

        # replace all non digits (\D) with '' in line
        new = re.sub('\D', '', line)

        # append first digit * 10 and last digit (line[-1])
        digits.append(int(new[0])*10 + int(new[-1]))

    sum = 0
    for digit in digits:
        sum += digit 

    print(sum)

if __name__=="__main__":
    main()