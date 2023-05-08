class NotCorrectConstruction(Exception):
    def __init__(self) -> None:
        self.comments = 'некоректный ввод конструкции аргументов'
    
    def __str__(self) -> str:
        return self.comments


def test_case(listArgs: list = [],listResult:list = []):
    """В listArgs вводяться все аргументы нужные для функции которую мы продекорировали. В формате [(...,...),...]

если аргумент один то в формате [(values,),...]

В listArgs вводяться все выходные результата. В формате [values,...]"""

    if not all([True if type(x) == tuple and len(listArgs) != 1 else False for x in listArgs]): raise NotCorrectConstruction()

    def test_case_decorator(function):
        def _wraper(*arguments, **kwargs):
            result = 0
            tp = ''
            for enum,args in enumerate(listArgs):
                print(tp:= 'Test passed V') if function(*args) == listResult[enum] else print(tp:= 'Test failed X')

                if tp[-1] == 'X':
                    result -= 1

            print(f'result run test: passed {len(listResult)+result}, failure {-result}')
        return _wraper
    return test_case_decorator

@test_case([(1),(1,2,3)],[3,6])
def some_function(n1,n2,n3):
    return n1 + n2 + n3

some_function()