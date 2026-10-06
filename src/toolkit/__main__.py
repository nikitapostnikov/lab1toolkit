from .kernel import calculaTORR,converTORR
import argparse
import sys

def command():
    parser=argparse.ArgumentParser(prog="python -m toolkit",description="Toolkit - Калькулятор и переводчик между единицами измерения")
    sub=parser.add_subparsers(dest="command",required=True)
    calc=sub.add_parser("calc",help="Калькулятор для вычислеия значения выражений")
    calc.add_argument("expression")
    convert= sub.add_parser("convert",help="Переводчик значения между соответсвующими друг другу единицами измерения")
    convert.add_argument("value")
    convert.add_argument("--from",required=True,dest="in_unit")
    convert.add_argument("--to",required=True,dest="out_unit")
    return parser

def main(marg:list[str]| None = None) -> int:
    parser=command()
    argm=parser.parse_args(marg)
    if argm.command == 'calc':
        workstr="".join(argm.expression)
        result=calculaTORR(workstr)
        print(result)
        return 0 if not result.startswith("Ошибка") else 1
    if argm.command =='convert':
        
        result=converTORR(argm.value,argm.in_unit,argm.out_unit)
        print(result)
        return 0 if not result.startswith("Ошибка") else 1
    return 1

if __name__ == "__main__":
    sys.exit(main())