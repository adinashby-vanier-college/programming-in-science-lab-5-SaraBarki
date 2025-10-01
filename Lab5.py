import math
# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****

def hollow_square(n):
    result = ""

    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                result += '*'
            result += '\n'
        else:
            # for k in range(n-2):
            result += '*' + ' ' * (n - 2) + '*'
            result += '\n'
    

    return result.rstrip()
        


print (hollow_square(5))




# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ''
    for i in range(n):
        for j in range(i + 1):
            result += str(j + 1)
        result += '\n'
    result = result.rstrip()
    return result
    
    

print(number_pattern(4))




# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    list = range(n + 1)
    result = math.fsum(list)
    return int(result)

print(sum_of_natural_numbers(5))


# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ''
    for i in range(n):  
         result +=  (n - 1 - i) * ' ' + '*' * (2 * i + 1) 
         result += '\n'
    return result.rstrip()
print (centered_star_pyramid(4))


# ' ' * ( (2 * n - 1) - (2 * i + 1) )  + '*' * (2 * i + 1) + ' ' *  ( (2 * n - 1) - (2 * i + 1) ) 
# + ' ' * (n - 1 - i) maybe use this if not work