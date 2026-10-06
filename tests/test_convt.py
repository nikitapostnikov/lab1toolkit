from pathlib import Path
import pytest
from src.toolkit.kernel import converTORR

def test_test1():
    value="1200"
    in_unit="g"
    out_unit="kg"
    assert converTORR(value,in_unit,out_unit)=="1.2 kg"
def test_test2():
    value="120"
    in_unit="k"
    out_unit="C"
    assert converTORR(value,in_unit,out_unit)=="-153.14999999999998 C"
def test_test3():
    value="-300"
    in_unit="c"
    out_unit="K"
    assert converTORR(value,in_unit,out_unit)=="Ошибка! Неверное числовое значение. "
def test_test4():
    value="50"
    in_unit="mM"
    out_unit="Km"
    assert converTORR(value,in_unit,out_unit)=="4.9999999999999996e-05 Km"
def test_test5():
    value="1000"
    in_unit="mM"
    out_unit="m"
    assert converTORR(value,in_unit,out_unit)=="1.0 m"
def test_test6():
    value="1.5"
    in_unit="Kg"
    out_unit="g"
    assert converTORR(value,in_unit,out_unit)=="1500.0 g"
def test_test7():
    value="0"
    in_unit="c"
    out_unit="f"
    assert converTORR(value,in_unit,out_unit)=="32.0 f"
def test_test8():
    value="273.15"
    in_unit="c"
    out_unit="k"
    assert converTORR(value,in_unit,out_unit)=="546.3 k"    
def test_test9():
    value="273.15"
    in_unit="k"
    out_unit="c"
    assert converTORR(value,in_unit,out_unit)=="0.0 c"
def test_test10():
    value="abc"
    in_unit="k"
    out_unit="c"
    assert converTORR(value,in_unit,out_unit)=="Ошибка! Неверное числовое значение. "
def test_test11():
    value="abc"
    in_unit="k"
    out_unit="c"
    assert converTORR(value,in_unit,out_unit)=="Ошибка! Неизвестная единица измерения. Ошибка! Неизвестная единица измерения. "
def test_test12():
    value="200"
    in_unit="4"
    out_unit="3"
    assert converTORR(value,in_unit,out_unit)=="Ошибка! Неизвестная единица измерения. Ошибка! Неизвестная единица измерения. " 
def test_test13():
    value="200"
    in_unit="g"
    out_unit="m"
    assert converTORR(value,in_unit,out_unit) == "Ошибка! Несовместимые единицы измерения. "    
