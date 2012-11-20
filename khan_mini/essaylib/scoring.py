import numpy
from numpy import matrix
from numpy import array
from numpy import linalg


def parknewman(A, alpha=0.2):
    N = A.shape[0]

    I = numpy.identity(N)
    kout = (matrix(numpy.ones(N))* A).T
    kin = A * matrix(numpy.ones(N)).T
    w = (I - alpha* A.T)
    w = w.I*kout

    l = (I - alpha* A)
    l = l.I*kin

    return w-l
    

def colley(A):
    N = A.shape[0]
    kout = (matrix(numpy.ones(N))* A).T
    kin = A * matrix(numpy.ones(N)).T

    b = 1+(kout - kin)/2
    C  = matrix(numpy.identity(N))
    for i in range(N):
        for j in range(N):
            if(i==j): 
                C[i,j] = ((kout[i] + kin[i]) + 2)
            else:
                C[i,j] = -(A[i,j] + A[j,i])


    return linalg.solve(C, b)

def standardize(r):
    r = (r - numpy.mean(r))/ numpy.std(r)
    return r

 

def test():
    A = numpy.matrix([[0,1,1,0,0,0],
                      [0,0,0,0,0,0],
                      [1,1,0,0,1,0],
                      [0,0,0,0,1,1],
                      [0,0,0,1,0,1],
                      [0,0,0,1,0,0]], dtype=numpy.float) 
    p = parknewman(A)
    c = colley(A)
    p = standardize(p)
    c = standardize(c)
    print "Park Newman\tColley"
    print "\n".join(["%s\t%s" % (p.item(i), c.item(i)) for i in range(A.shape[0])])


if __name__ == "__main__":
    test()
