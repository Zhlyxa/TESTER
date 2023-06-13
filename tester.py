class NotCorrectConstruction(Exception):
    def __init__(self) -> None:
        self.comments = 'некоректный ввод конструкции аргументов / not correct construction arguments'

    def __str__(self) -> str:
        return self.comments


def test_case(listArgs: list = [], listResult: list = []):
    """
    ##### Russian language/Русский язык
    Декоратор нужный для тестирования функции и
    проверки выполнения нужных действий со входными параметрами
    
    Аргументы:
        В listArgs вводяться все аргументы нужные для функции которую мы продекорировали. В формате [(...,...),...]
        если аргумент один то в формате [(values,),...]
        В listArgs вводяться все выходные результата. В формате [values,...]

    ##### English language/Английский язык
    Decorator necessary for testing a function and verifying the execution of the necessary actions with input parameters.

    Arguments:

        listArgs: all the required arguments for the function we decorated are entered in the format [(...,...),...]. 
        If there is only one argument, it is in the format [(values,),...].
        listRes: all the output results are entered in the format [values,...].
    """

    if not all([True if type(x) == tuple and len(listArgs) != 1 else False for x in listArgs]):
        raise NotCorrectConstruction()

    def test_case_decorator(function):
        def _wraper(*arguments, **kwargs):
            result = 0
            tp = ''
            for enum, args in enumerate(listArgs):
                print(tp := 'Test passed V') if function(
                    *args) == listResult[enum] else print(tp := 'Test failed X')

                if tp[-1] == 'X':
                    result -= 1

            print(
                f'result run test: passed {len(listResult)+result}, failure {-result}')
        return _wraper
    return test_case_decorator