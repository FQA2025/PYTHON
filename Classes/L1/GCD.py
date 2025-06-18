largest = int(input("Enter largest number :"))
smallest = int(input("Enter smallest number :"))

while(smallest):
    numStore = smallest
    smallest = largest % smallest
    largest = numStore

    print("HCF is : ", largest)
