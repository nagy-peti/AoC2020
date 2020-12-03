def task(nums):
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                if int(num1)+int(num2)+int(num3) == 2020:
                    print(int(num1), int(num2), int(num3))
                    print(int(num1)*int(num2)*int(num3))
                    return [int(num1), int(num2), int(num3)]


file = open("in.txt", "r")
nums = file.readlines()
file.close()

numbers = task(nums)
