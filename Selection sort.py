arr=[7,3,5,8,9,2]
n=len(arr)
for i in range(0,n):
    min=i
    for j in range(i+1,n):
        if arr[min]>arr[j]:
           min=j

    temp=arr[i]
    arr[i]=arr[min]
    arr[min]=temp 

print(arr) 
