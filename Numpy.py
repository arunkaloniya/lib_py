# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 13:16:55 2020

@author: Arun
"""

'''
Numpy 

. Numpy uses less memory that why its very fast to extract the info 
. in numpy it doesn't have type checking in iterating through objects 

suppose these are the memory blocks here 

/ / / / / / / / / / / / 

in list ->  /x/ /x/ /x/x/ / / / / (non Contiguous memory)

in numpy -> /x/x/x/x/x/ / / / / (contiguous memory utilization)

our CPU has one SIMD Vecotr processign 

so whats SIMD -> Single Instruction Multiple data 

so rather than to iterating through each diff obj in list 
we can use SIMD in numpy to perform faster operation in a single through
 
in numpy :-> since numpy uses contiguous mwm then we can also use
 cache memory which is another faster memory

so through is we can also utilization of the cache memory in one through 

'''

import numpy as np

a=[1,2,3]
b=[1,2,3]



n_a=np.array(a) # One dimension array 
n_b=np.array(b) # One dimension array 


two_dim=np.array([a,a])  # two dimension array ( list within list)



# how to get dimesion 

n_a.ndim # ndim means no of dimesion 


two_dim.ndim



# how to get shape 

n_a.shape # as its one dimesional vector with rows : format is rows,col

two_dim.shape  # has two rows and three col 


# how to get datatype  

n_a.dtype # at first it shows the 32 bytes of memory for each element 

# if you know that you are not storing the big val then reduce it to 4 byte 


n_a=np.array(n_a, dtype='int16') # this is how you can change the size of array

n_a.dtype # verify it 



# how to get size 


n_a.itemsize # individual item size

n_a.nbytes # total size in bytes consumed by array 


# initialize the zero matrix 


f_zero=np.zeros(5)

f_zero=np.zeros((5,2))

f_zero=np.zeros((5,2), dtype='int16')

#Similarly for the one's matrix 


f_one=np.ones((5,2),dtype='int16')


# choose your own no 


f_my=np.full((2,3),'16Nov') # place a strign of your choice 


# full_like method -> copy an existing matrix and fill your own value 


f_my_2=np.full((n_a),'88')

# one of the limitations of this method if it only takes numerical matrix 


# how to build a random number matrix 


N_rand=np.random.rand(2,4)


# how to take only int values 
np.random.randint(4,high=20,size=(4,4))


# how to build an identity matrix 
# identity matrix is that who's diagonal elements are one '1'



np.identity((2),dtype='int16') # the argument tells the size 


# repeating an array 

a=[1,2,3]

np.repeat([a],3,axis=0)


# form the above concepts lets make the follwing matrix 

'''
1	1	1	1	1
1	0	0	0	1
1	0	9	0	1
1	0	0	0	1
1	1	1	1	1
'''

output=np.ones((5,5),dtype='int16')

zero=np.zeros((3,3),dtype='int16')


zero[1,1]=9



output[1:4,1:4]=zero


output # there you are finally 



################################ Mathematics ################################

a=np.array([1,2,3,4])


# element wise addition/subtraction/division & multiplication 

a-2
a+2
a/2
a*2
a**2

samp=np.random.randint(4,high=10,size=(3,3))


np.min(samp,axis=1) # axis=1 means horizontal , 0 means verical 


np.min(samp) # incase if you don't specify the axis it would give the min of entire matrix


np.median(samp)




######################### Resizing Matrix ###############################


a=np.array([[1,2,3,4],[5,6,7,8]])

after=a.reshape(4,2)

after=a.reshape(2,2,2)    # make sure internal arg multiplication comesout equal size

after=a.reshape(8,1)


############## Stacking #################33


a=np.array([1,2,3,4])
b=np.array([5,6,7,8])


final=np.vstack([a,b,b,b])


############################# Reading data from a file #####################


mydata=np.genfromtxt(r"C:\Users\Arun\Desktop\input.txt", delimiter=",",dtype='int32')

 # this is the input data in the file 1,  2,  3,  4,  5,  6,  7,  8,  9, 10

# incase if you dont specify the dtype then it would be an float datatype 

#filteration

mydata[mydata>5] 






































































































































 

































