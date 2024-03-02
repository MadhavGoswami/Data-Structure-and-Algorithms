def MergeSort(arr):
    n=len(arr)
    if n>1:
        mid=n//2
        L=arr[:mid]
        R=arr[mid:]
        MergeSort(L)
        MergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                arr[k]=L[i]
                k=k+1
                i=i+1
            else:
                arr[k]=R[j]
                k=k+1
                j=j+1   
        
        while i<len(L):
            arr[k]=L[i]
            k=k+1
            i=i+1

        while j<len(R):
            arr[k]=R[j]
            j=j+1
            k=k+1        
def printList(arr):
    print(arr)                  

if __name__=='__main__':
    arr=[1,2,4,3,5]
    MergeSort(arr)
    printList(arr)