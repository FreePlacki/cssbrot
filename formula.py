from sys import argv


def scale(x, a_to, b_to, a_from=1, b_from=20, ):
    """
    Maps x that is in [a_from, b_from] to be in [a_to, b_to]
    """
    # there has to be a space before an operator in css
    return f"{a_to} + ({x} - {a_from})*({b_to} - {a_to})/({b_from} - {a_from})"


def sq(num):
    return f"pow({num},2)"


def var(name):
    return f"var(--{name})"


x = scale(var('x'), -2.0, 1.0)
y = scale(var('y'), -1.5, 1.5)


def gen_iters(n):
    """
    The square of z after n iterations
    """

    def rec(num, i):
        if i == 0:
            return num
        (re, im) = rec(num, i-1)
        return (f"{sq(re)} - {sq(im)} + {x}", f"2*({re})*({im}) + {y}")

    (re, im) = rec((x, y), n-1)
    return f"{sq(re)} - {sq(im)}"


def clamp(num, min, max):
    return f"clamp({min}, {num}, {max})"


def mapping(num):
    return f"1/(1 + exp(abs({num})))"


n = 3 if len(argv) == 1 else int(argv[1])

print(mapping(gen_iters(n)))
