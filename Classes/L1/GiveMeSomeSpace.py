def sum(n):
    return n*(n+1)/2
#Space complexity:

def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i
    return(sum)

a = [12, 3, 4, 15]
arraysum(a)
print("Sum of array elements:", arraysum(a))

print("with the size of the array, the spacce also required increases")



