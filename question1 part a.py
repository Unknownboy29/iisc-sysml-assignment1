import random

#function for generate random matrix 
def initialize_random_matrix(rows, cols,C,M):
    return [[[[round(random.uniform(0, 1)* random.choice([-1, 1]) ,2) for _ in range(cols)] for _ in range(rows)]for _ in range(C)] for _ in range(M)]


# Naive 7-layer for loop implementation
def naive_implementation(inputFmap, filter,stride,H,W,R,S,C,M):
    E = (H-R+stride)//stride  #height of output fmap
    F = (W-S+stride)//stride  #width of output fmap

    # empty output map
    outputFmap = [[[[0 for _ in range(E)] for _ in range(F)]for _ in range(M)]for _ in range(N)]

    for n in range(N):  
        for m in range(M):
            for x in range(E):
                for y in range(F):
                    for i in range(R):
                        for j in range(S):
                            for k in range(C):
                                outputFmap[n][m][x][y] += inputFmap[n][k][stride*x+i][stride*y+j] * filter[m][k][i][j]
                    
            

            #rounding output map values upto two decimal place
                    outputFmap[n][m][x][y] = round(outputFmap[n][m][x][y] , 2)
    return outputFmap


H = 28 #height of input Fmap
W = 28 #width of output Fmap
R = 3  #Height of Filter
S = 3  #Height of Filter
C = 3  #number of channel
M = 64  #number of filter
N = 10  #number of input
stride = 2  #stride 

#input feature Mapp
inputFmap = initialize_random_matrix(H,W,C,N)   

#kernal/ filter matrix
filter = initialize_random_matrix(R,S,C,M)

#output feature map
output_Fmap=naive_implementation(inputFmap, filter,stride, H,W,R,S,C,M)

#priting final output feature maping
print(output_Fmap)