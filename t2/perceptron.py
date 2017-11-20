def perceptron(max_it, E, alpha, X, d):
    weights = [0,0]
    bias = 0.1
    t = 1
    erro = [0,0,0,0]
    Y = [0,0,0,0]

    while(t<max_it and E>0):
        for i in range(len(X)):
            Y[i]  = function(weights, X[i], bias)
            erro[i] = d[i] - Y[i]
            weights[0] = weights[0] + alpha*erro[i]*X[i][0]
            weights[1] = weights[1] + alpha*erro[i]*X[i][1]
            bias = bias + alpha*erro[i]
            erro[i] = erro[i]**2
        E = sum(erro)
        t = t +1
    print("----")
    print(Y)
    print(weights)
    print(bias)

def function(w, x, b):
    if( w[0]*x[0] + w[1]*x[1] + b < 0):
        return 0
    else:
        return 1
    
X = [[0,0],[0,1],[1,0],[1,1]]
d = [0,0,0,1]
perceptron(10, 1, 0.1, X, d)
