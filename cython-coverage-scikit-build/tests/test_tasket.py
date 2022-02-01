import tasket

def test_sin():
    x = 0.25
    v1 = tasket.sin_squared(x)
    v2 = tasket.A(x).sin_squared()
    assert(abs(v1 - v2) < 1e-15)

def test_cos():
    x = 0.25
    v1 = tasket.cos_squared(x)
    v2 = tasket.A(x).cos_squared()
    assert(abs(v1 - v2) < 1e-15)
