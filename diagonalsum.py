def diagonalSum(arr , n):
  n = len(arr)
  ld ,rd = 0,0
  for i in range(n):
    ld+= arr[i][i]
    rd+= arr[i][n-1-i]
  return (abs(ld-rd))
    
  
