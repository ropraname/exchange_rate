import pytest
from exchange_rate import get_best_exchange_rate
from random import randint


currencies_first = ["usd", "eur", "gbp"]
max_num_branches_first = [3, 5, 2]

currencies_second = ["abc", "f", "gg"]
max_num_branches_second = [3, 1, 2]
max_num_branches_last = [-3.15, -1, -2.5]

test_params_first = list(zip(currencies_first, max_num_branches_first))
test_params_second = list(zip(currencies_second, max_num_branches_second))
test_params_last = list(zip(currencies_second, max_num_branches_last))

@pytest.mark.parametrize("currency, max_num_branches", test_params_first)
def test_correct_work(currency, max_num_branches):
    num_branches = randint(1, max_num_branches)
    assert len(get_best_exchange_rate(currency, num_branches)) == num_branches

@pytest.mark.parametrize("currency, num_branches", test_params_first)
def test_peak_num_branches(currency, num_branches):
    with pytest.raises(IndexError) as excinfo:
        num_branches = num_branches + 10000
        excinfo = get_best_exchange_rate(currency, num_branches)
    assert str(excinfo.value) == 'Num of brunces is too big'

@pytest.mark.parametrize("currency, num_branches", test_params_second)
def test_correct_currency(currency, num_branches):
    with pytest.raises(ValueError) as excinfo:
        excinfo = get_best_exchange_rate(currency, num_branches)
    assert str(excinfo.value) == 'There is now such currency'

@pytest.mark.parametrize("currency, num_branches", test_params_last)
def test_type_num_branches(currency, num_branches):
    with pytest.raises(ValueError) as excinfo:
        excinfo = get_best_exchange_rate(currency, num_branches)
    assert str(excinfo.value) == 'num_branches is uncorrect type'

@pytest.mark.parametrize("currency, num_branches", test_params_first)
def test_sorted(currency, num_branches):
    excinfo = get_best_exchange_rate(currency, num_branches)
    sorted_in_f = []
    for elem in excinfo:
        sorted_in_f.append(elem[2])
    assert sorted_in_f == sorted(sorted_in_f)    

@pytest.mark.parametrize("currency, num_branches", test_params_first)
def test_type_of_elems_in_turple(currency, num_branches):
    excinfo = get_best_exchange_rate(currency, num_branches)
    for elem in excinfo:
        assert type(elem) == tuple
        assert type(elem[0]) == str
        assert type(elem[1]) == str
        assert type(elem[2]) == float
