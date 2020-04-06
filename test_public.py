import pytest

from exchange_rate import get_best_exchange_rate

def test_small_big_brunhes():
    with pytest.raises(IndexError) as excinfo:
        excinfo = get_best_exchange_rate("RUB", 0)
    assert str(excinfo.value) == 'Num of brunces is too small'
    
    with pytest.raises(IndexError) as excinfo:
        excinfo = get_best_exchange_rate("RUB", len(all_values))
    assert str(excinfo.value) == 'Num of brunces is too big'

def test_types_of_elems():
    excinfo = get_best_exchange_rate("EUR", 3)
    assert type(excinfo[0]) == tuple
    assert type(excinfo[0][0]) == str
    assert type(excinfo[0][1]) == str
    assert type(excinfo[0][2]) == float

def test_len_num_of_elems():
    num_branches = 7
    currency_code = "EUR"
    excinfo = get_best_exchange_rate(currency_code, num_branches)
    assert len(excinfo) == num_branches

def test_sort():
    num_branches = 10
    currency_code = "EUR"
    excinfo = get_best_exchange_rate(currency_code, num_branches)
    sorted_excinfo = sorted(excinfo, key=lambda tup: tup[2])
    assert excinfo == sorted_excinfo
