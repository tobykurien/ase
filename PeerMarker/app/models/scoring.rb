require 'matrix'
def parknewman(matrixA, alpha=0.2)
    n = matrixA.row_size

    i = Matrix.unit(n)
    ones = Matrix.[]([1]*n) 
    kout = (ones* matrixA).transpose
    kin = matrixA * (ones.transpose)
    w = (i - alpha* matrixA.transpose)
    w = w.inverse*kout

    l = (i - alpha* matrixA)
    l = l.inverse*kin

    return w-l
end    

def colley(matrixA)
    n = matrixA.row_size
    ones = Matrix.[]([1]*n)
    kout = (ones * matrixA).transpose
    kin = matrixA * (ones.transpose)

    b = ones.transpose + (kout - kin)*0.5

    c  = Matrix.unit(n)
    
    n.times do |i|
        n.times do |j|
            if(i==j) then
                c[i,j] = ((kout[i,0] + kin[i,0]) + 2)
            else
                c[i,j] = -(matrixA[i,j] + matrixA[j,i])
            end
        end
    end            

    return b.transpose/c
end

def standardize(r)
    return r.round 2
end    

class Matrix
  def []=(i, j, x)
    @rows[i][j] = x
  end
end 

def test()
    matrixA = Matrix[[0,1,1,0,0,0],[0,0,0,0,0,0], [1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,0,1,0,1],[0,0,0,1,0,0]]
    p = parknewman(matrixA)
    c = colley(matrixA)
    p = standardize(p)
    c = standardize(c.transpose)
    n = matrixA.row_size
    puts "Park Newman\tColley"
    puts n.times.map {|i| "#{p[i,0]}\t#{c[i,0]}"}
end

if __FILE__ == $PROGRAM_NAME
   test()    
end
