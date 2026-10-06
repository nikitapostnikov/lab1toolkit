from pathlib import Path
import pytest
from src.toolkit.kernel import calculaTORR

def test_test1():
    teststr="2+3*4"
    assert calculaTORR(teststr)=="14"
def test_test2():
    teststr="10/4"
    assert calculaTORR(teststr)=="2.5"
def test_test3():
    teststr="2*-3"
    assert calculaTORR(teststr)=="-6"
def test_test4():
    teststr="1+-2"
    assert calculaTORR(teststr)=="-1"
def test_test5():
    teststr="2*/3"
    assert calculaTORR(teststr)=="Ошибка! Два бинарных оператора подряд. " 
def test_test6():
    teststr="2+a"
    assert calculaTORR(teststr)=="Ошибка! Недопустимый символ. Ошибка! Пропущенный операнд/оператор. "
def test_test7():
    teststr="1/0"
    assert calculaTORR(teststr)=="Ошибка! Деление на ноль. "
def test_test8():
    teststr="12+.52"
    assert calculaTORR(teststr)=="12.52"
def test_test9():
    teststr="12+48-"
    assert calculaTORR(teststr)=="Ошибка! Пропущенный операнд/оператор. "                           
def test_test10():
    teststr="12+13*2-9/0"
    assert calculaTORR(teststr)=="Ошибка! Деление на ноль. "    
def test_test11():
    teststr="12/0+$"
    assert calculaTORR(teststr)=="Ошибка! Недопустимый символ. Ошибка! Деление на ноль. Ошибка! Пропущенный операнд/оператор. "    
def test_test12():
    teststr="12*+7"
    assert calculaTORR(teststr)=="84"    