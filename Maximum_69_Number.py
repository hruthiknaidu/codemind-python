def maximum69Number(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] == '6':
            return int(num_str[:i] + '9' + num_str[i+1:])
    return num
    
    
n = int(input())
print(maximum69Number(n))