def get_binomial_distribution(n, p):
    return lambda k : choose(n, k)*(p**(k))*((1-p)**(n-k))

