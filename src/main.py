from constants import NUM,OPR
from kernel import calculaTORR,converTORR

def main() -> None:
    read=''
    run=True
    def tokenization(inp:list[str]):
        tokenized=[]
        readarr=inp.split(' ')
        for i in range(len(readarr)): 
            if readarr[i]!='': tokenized.append(readarr[i])
        return tokenized
    def validation(inp:list[str]):
        workstring=''
        if inp==[]:
            workstring+='Ошибка! Пустая строка. '
        else:    
            if len(inp)==1 and inp[0]=='--help':
                print('1) Команда "calc <ВЫРАЖЕНИЕ>" - подключает калькулятор для вычисления указанного выражения.')
                print('Особенности калькулятора:\n1. Не поддерживаются скобки\n2. Поддерживаемые операции:сложение(+),вычитание(-),деление(/),умножение(*)')
                print('3. Отрицательные числа помечаются впередиидущим знаком вычитания (пример:2+-2=> -2 отрицательное, результат 0)')
                print('4. Нет ограничений на количство пробелов между элементами выражения')
                print('2) Команда "convert <ЗНАЧЕНИЕ> <НАЧ.ЕД.ИЗМ> -> <КОНЕЧ.ЕД.ИЗМ>" - перевод значения из одной единицы измерения')
                print('Особенности переводчика:\n1. Поддерживаются:длина(mm,cm,m,km),масса(g,kg),температура(k,f,c)')
                print('2. Вызов переводчка может быть омуществлен только с такой струтурой и ХОТЯ БЫ ОДНИМ ПРОБЕЛОМ между элементами\n3. Регистр единицы измерения не важен')
                print('3) Команда "EOF" - завершение работы программы')      
            elif inp[0]=='calc':
                for i in range(1,len(inp)):
                    workstring+=inp[i]
                workstring=calculaTORR(workstring)
            elif inp[0]=='convert':
                for i in range(1,len(inp)):
                    workstring+=inp[i]
                workstring=converTORR(workstring)      
            else:
                workstring='Ошибка! Неправильный синтаксис. Попробуйте ещё раз. '
        return workstring               
    while run:
        if read=='':read=input()
        token=tokenization(read)
        if token==['EOF']:
            run=False
        else:    
            print(validation(token))
            read=''
            token=[]   

if __name__ == "__main__":
    main()