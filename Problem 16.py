powerdigit = str(2**1000)

mybiglist = [int(powerdigit[a]) for a in range(len(powerdigit))]

print(sum(mybiglist))
