# CMPS 2200 Assignment 3
## Answers

**Name:**_ Mackenzie Bookamer


Place all written answers from `assignment-03.md` here for easier grading.






- **b.**

We decrease the size of our list by 1 every step, and at every step, the comparison is done in constant time. Thus, our work and span recurrences are both W(n) = w(n-1) + 1, which is O(n) and S(n) = S(n-1) + 1, which is O(n). 


- **d.**

We know from class that for scan, W(n) = W(n/2) +n and S(n) = S(n/2) + 1 (no further explanation since it was thoroughly covered on class). Therefore, scan has W(n) in O(n) and S(n) in O(log n). 

We also know from class that for reduce, W(n) = 2W(n/2) + 1 and S(n) = S(n/2)+1. Therefore, reduce has W(n) in O(n) and S(n) in O(log n). 



- **f.**

We divide our list in half at every step and compute each half in parallel with the parallel work being done in constant time, so W(n) = 2W(n/2) + 1. Thus, 
W(n) is in O(n). Since we are dividing our list in half every step, S(n) = S(n/2) + 1 so S(n) in O(log n).
