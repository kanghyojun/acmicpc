from nono_power import prime


def test_nono_power_prime():
    b = prime(10)
    r = []
    for i, p in enumerate(b):
        if p:
            r.append(i)
    assert [1, 2, 3, 5, 7] == r
