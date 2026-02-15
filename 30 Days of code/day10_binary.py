if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)[2:]
    consec = 0
    max_ones=0
    for i in binary:
        if i == '1':
            consec +=1
            max_ones = max(max_ones,consec)
        else:
            consec=0
    print(max_ones)



"""
calculate the consecutive 1 in binary 


"""
