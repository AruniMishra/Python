from employee import Employee

import pytest

def test_apply_raise():
    emp_1 = Employee('Corey', 'Schafer', 50000)
    print('test_apply_raise')
    emp_1.apply_raise()
    assert emp_1.pay == 100000