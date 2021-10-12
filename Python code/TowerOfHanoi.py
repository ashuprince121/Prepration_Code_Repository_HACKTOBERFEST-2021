#Python program to solve Tower of Hanoi using recursion.
def TowerOfHanoiSolver(n , source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoiSolver(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoiSolver(n-1, auxiliary, destination, source)
          
n = 4
TowerOfHanoiSolver(n,'A','B','C') 