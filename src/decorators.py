import time


def log(filename):
    def wrapper(func):
        def inner(a, b):
            try:
                result = func(a, b)
            except:
                result = "ZeroDivisionError"
            now_time = time.localtime()
            current_time = time.strftime("%Y-%m-%dT%H:%M:%S", now_time)

            if filename is not None:
                with open(filename, "a", encoding="utf-8") as file:
                    if result != "ZeroDivisionError":
                        file.write(f"{current_time} my_function ok \n")
                    else:
                        file.write(f"{current_time} my_function error: <{result}>. Inputs: {a, b} \n")
            else:
                if result != "ZeroDivisionError":
                    print(f"{current_time} my_function ok \n")
                else:
                    print(f"{current_time} my_function error: <{result}>. Inputs: {a, b} \n")
            return result
        return inner
    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    """
    Функция принимает два числа и возвращает результат сложения двух чисел.
    :param x: Число.
    :param y: Число.
    :return: Результат.
    """
    return x / y


print(my_function(2, 1))
