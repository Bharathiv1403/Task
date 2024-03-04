
string = input("Enter the String : ")
n = int(input("Enter the number: "))
m = [string[i:i+n] for i in range(0, len(string), n)]
arr = []
for i in m[::-1]:
    arr.append(i)
print("".join(arr))















