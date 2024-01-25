# 𝑁=10,𝐶=3,𝐻=28,𝑊=28,𝑅=3,𝑆=3, m=64
###add negative value
import random

def initialize_random_matrix(rows, cols,C,M):
    # return [[[[round(random.uniform(0, 1)* random.choice([-1, 1]) ,2) for _ in range(cols)] for _ in range(rows)]for _ in range(C)] for _ in range(M)]
    return [[[[round(random.uniform(0, 1) ,2) for _ in range(cols)] for _ in range(rows)]for _ in range(C)] for _ in range(M)]


def naive_implementation(inputFmap, filter,stride,H,W,R,S,C,M):
    E = (H-R+stride)//stride  #height of output fmap
    F = (W-S+stride)//stride  #width of output fmap

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


def flatten_method(inputFmap, filter,stride,H,W,R,S,C,M):
    ########flattening the  filter
    E = (H-R+stride)//stride  #height of output fmap
    F = (W-S+stride)//stride

    width_flatten_filter = C*R*S
    flatte_filter = [[0 for _ in range(width_flatten_filter)] for _ in range(M)]

    for m in range(M):
        k = 0
        for c in range(C):
            for r in range(R):
                for s in range(S):
                    flatte_filter[m][k] = filter[m][c][r][s]
                    k = k+1
    # return flatte_filter
    
    ########## Toeplitz the input feature map

    toeplitz_matrix_height = C*R*S
    toeplitz_matrix_width = (H-R+1)*(W-S+1)*N
    toeplitz_input_matrix = [] #[[0 for _ in range(toeplitz_matrix_height)] for _ in range(toeplitz_matrix_width)]

    for n in range(N):
        #rslt =[]
        for i in range(E):
            for j in range(F):
                patch_list=[]
                for c in range(C):
                    #patch_list=[]
                    for r in range(R):
                        for s in range(S):
                            patch_list.append(inputFmap[n][c][stride*i + r][stride*j + s])
                
                toeplitz_input_matrix.append(patch_list)            
                    #print(patch_list)

                    
    
   
        
    return toeplitz_input_matrix





H = 3 #height of input Fmap
W = 3 #width of output Fmap
R = 2  #Height of Filter
S = 2  #Height of Filter
C = 1  #number of channel
M = 2  #number of filter
N = 1  #number of input
stride = 1  #stride 

# num = round(random.uniform(0 ,1), 2)

# inputFmap = initialize_random_matrix(H,W,C,N)
# filter = initialize_random_matrix(R,S,C,M)

# output_fmap=naive_implementation(inputFmap, filter,stride, H,W,R,S,C,M)

inputFmap = [[[[1,2,3],[4,5,6],[7,8,9]]]]
filter = [[[[1,1],[2,1]]],[[[1,0],[1,1]]]]

output_fmap = flatten_method(inputFmap, filter, stride, H,W,R,S,C,M )

print("\nInput Fmap")
for i in range(N):
    for j in range(C):
        print(inputFmap[i][j])

    
print("\nFilter")
for i in range(M):
    for j in range(C):
        print(filter[i][j])

print("\nOutput Fmap")
for row in output_fmap:
    print(row)
