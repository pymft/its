import logme


@logme.logme_part_one
def mysum(a, b):
    return a + b

@logme.logme_part_two('logs_new.csv')
def mysub(a, b):
    return a - b

logtemp = logme.LogMeClass('logs_again.csv')

@logtemp
def mymul(a, b):
    return a * b 

if __name__ == '__main__':
    mymul(9, 2)
    mymul(50, 20)
