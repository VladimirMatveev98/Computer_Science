def calculate_pi(n_terms):
    """Из-за особенностей типа float, число пи будет отображено
    с 15-ю символами после запятой. Тем не менее, чем выше показатель
    n_terms, тем точнее будет это число из-за округления не отображаемых
    значений, но и время на вычисления будет увеличиваться."""
    
    numerator = float(4)
    denominator = float(1)
    operation = float(1)
    pi = float(0)
    
    for i in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2
        operation *= -1
        
    return pi


if __name__ == '__main__':
    print("Вычисления займут какое-то время. Пожалуйста, ожидайте...")
    print(calculate_pi(100000000))
    print("Вычисления повышенной точности. Ожидайте...")
    print(calculate_pi(1000000000))
