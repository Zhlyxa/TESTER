import time

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
    def decorator(function):
        def _wraper(*arguments, **kwargs):
            result = 0
            tp = ''
            for enum, args in enumerate(listArgs):
                try:
                    start_time = time.time()
                    result_func = function(*args)
                    end_time = time.time()
                    if result_func == listResult[enum]:
                        tp = f'Test passed V: time of execution: {end_time-start_time}'
                    else:
                        tp = 'Test failure X'
                        result -= 1
                except Exception as e:
                    tp = f'Test failure X: {str(e)}'
                    result -= 1

                print(tp)

            print(
                f'result run test: passed {len(listResult)+result}, failure {-result}')
        return _wraper
    return decorator


