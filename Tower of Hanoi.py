class Hanoi:
    def toh(self, n, fromm, to, aux, moves):
        Hanoi.moves=2**n-1
        if(n==1):
            print("move disk 1 from rod "+str(fromm)+" to rod "+str(to))
            return
        self.toh(n-1,fromm,aux,to,moves)  #breaks problem into smaller pieces, first thinks about how to move
        #all disks to an auxilary rod so it could move the largest one onto the To rod
        #then breaks that problem into smaller pieces and looks for a solution on how to move all but the last disk
        #in this recursive call so it could move that last disk to the right rod, and so on.
        #If n=4, The problem was broken to smaller subproblems, like for moving 4 disks to C you first need to move 3 disks to B.
        #And to move 3 disks to B, you need to first move 2 disks to C. And to move 2 disks to C you need to first move one disk to B.
        #That's when n==1 and we print that we moved disk 1 from A to B. Then we go back and call again for the second time (down below) and so on.﻿
        print("move disk "+str(n)+" from rod "+str(fromm)+" to rod "+str(to))  #for the remaining disks when n-1th disk has been moved to target rod
        self.toh(n-1,aux,to,fromm,moves)
        Hanoi.moves=2**n-1
import math
def main():
    T = int(input())
    while(T > 0):
        N = int(input())
        Hanoi.moves = 0
        h = Hanoi()
        h.toh(N, 1, 3, 2, Hanoi.moves)
        print(Hanoi.moves)
        T -= 1
if __name__ == "__main__":
    main()
