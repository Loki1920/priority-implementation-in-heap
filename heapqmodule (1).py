#Heap operation using heapq module
import heapq
heap = []
#heappush() operation to insert an element
heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,3)
print(heap)
#heappop() operation to delete smallest element
print("smallest element:",heapq.heappop(heap))

#heapify operation to covert list to binary heap
heap1 = [2,4,67,34,2,90,59]
print("list before heapify:",heap1)
heapq.heapify(heap1)
print("heap after heapify:",heap1)

#heappushpop operation first it will insert given item then perform pop operation
heap1 = [2,4,67,34,2,90,59]
print("list before heappushpop operation:",heap1)
print("poped element is :",heapq.heappushpop(heap1,101))
print("list after heappushpop operation:",heap1)

#heapreplace operation first perform pop and than push
heap1 = [2,4,67,34,2,90,59]
print("heap1 before operation:",heap1)
print("poped element is:",heapq.heapreplace(heap1,200))
print("heap1 after heapreplace operation:",heap1)

# nsmallest(n,iterable) gives n smallest number
heap1 = [2,4,67,34,2,90,59]
print('smallest number are:',heapq.nsmallest(3,heap1))
#nlargest(n,iterable) gives n largest number 
print("largest number are:",heapq.nlargest(3,heap1))

list1 = [(1,'lucky'),(3,'sam'),(4,'yash'),(2,'neeru')]

heapq.heapify(list1)
print(list1)
for i in range(len(list1)):
  print("poped element:",heapq.heappop(list1))

