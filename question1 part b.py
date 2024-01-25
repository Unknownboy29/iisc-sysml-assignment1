import random

#function for generate random matrix 
def initialize_random_matrix(rows, cols,C,M):
    return [[[[round(random.uniform(0, 1)* random.choice([-1, 1]) ,2) for _ in range(cols)] for _ in range(rows)]for _ in range(C)] for _ in range(M)]


def flatten_conc_layer_computation(inputFmap, filter,stride,H,W,R,S,C,M):
    E = (H-R+stride)//stride  #height of output feature map
    F = (W-S+stride)//stride  #width of output feature map

    #width of flattened filter
    width_flatten_filter = C*R*S 


    flatted_filter = [[0 for _ in range(width_flatten_filter)] for _ in range(M)]

    for m in range(M):
        k = 0
        for c in range(C):
            for r in range(R):
                for s in range(S):
                    flatted_filter[m][k] = filter[m][c][r][s]
                    k = k+1
    
    ########## Toeplitz the input feature map

    toeplitz_matrix_ip_height = C*R*S
    toeplitz_matrix_ip_width = E*F * N
    toeplitz_input_matrix_ip = []

    for n in range(N):
        #rslt =[]
        for i in range(E):
            for j in range(F):
                patch_list=[]
                for c in range(C):
                    for r in range(R):
                        for s in range(S):
                            patch_list.append(inputFmap[n][c][stride*i + r][stride*j + s])
                
                toeplitz_input_matrix_ip.append(patch_list)            
                    #print(patch_list)

    output_flatten=[]
    # print("\n",len(toeplitz_input_matrix_ip), len(toeplitz_input_matrix_ip[0]), toeplitz_matrix_ip_width)

    
    for m in range(M):
        op_lst=[]
        
        for w in range(toeplitz_matrix_ip_width):
            temp = 0 
            for h in range(toeplitz_matrix_ip_height):
                temp += flatted_filter[m][h] * toeplitz_input_matrix_ip[w][h]

            op_lst.append(round(temp,2))

        output_flatten.append(op_lst)

    
    return output_flatten



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
output_Fmap=flatten_conc_layer_computation(inputFmap, filter,stride, H,W,R,S,C,M)

print(output_Fmap)