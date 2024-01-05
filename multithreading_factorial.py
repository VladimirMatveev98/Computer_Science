import threading
import time

#=================================
TEST_CONST = 250000
LOGS = False
#=================================


def check_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return res
    return wrapper


@check_time
def factorial(number:int) -> int:
    res = 1
    number = int(number)
    for i in range(2,number+1):
        res = res * i

        if i % 500 == 0 and LOGS:
            print("Активные потоки: ", threading.active_count())
            print("thr-1 is alive: ", thr_1.is_alive())
            print("Итерация: ", i)
            print("-" * 22)

    print("Обычная функция завершила работу!")
    return res


@check_time
def mult_factorial(number:int) -> int:
    #Реализовать через класс, получить результат вычислений
    def part_fact(start, end):
        """Возвращает произведение всех чисел от start
        до end включительно"""
        res = 1
        for i in range(start+1, end+1):
            res = res * i

            if i % 5000 == 0 and LOGS:
                print("Многопоточные вычисления.")
                print("Активные потоки: ", threading.active_count())
                print("Итерация: ", i)
                print("-" * 22)

        return res

    def main(number):
        """Возвращает факториал числа, вычисляя его по частям"""

        number = int(number)

        #Аргументы для потоков
        arg_2 = (1, number//4)
        arg_3 = ((number//4)-1, (number//4)*2)
        arg_4 = (((number//4)*2)-1, (number//4)*3)
        arg_5 = (((number//4)*3)-1, number)

        #Описание потоков
        threads = [
        threading.Thread(target=part_fact, args=(arg_2),name='thr-2'),
        threading.Thread(target=part_fact, args=(arg_3),name='thr-3'),
        threading.Thread(target=part_fact, args=(arg_4),name='thr-4'),
        threading.Thread(target=part_fact, args=(arg_5),name='thr-5')
        ]

        #Запуск потоков
        for thread in threads:
            thread.start()

        #Ожидание завершения потоков
        for thread in threads:
            thread.join()


    #Вычисление результата, возврат результата(?)
    main(number)
    print("Многопоточная функция завршила работу!")



if __name__ == '__main__':
    thr_1 = threading.Thread(target=factorial,args=(str(TEST_CONST),)
                            ,name='thr-1')
    thr_1.start()
    print("Обычная функция начала работу!")


    thr = threading.Thread(target=mult_factorial,args=(str(TEST_CONST),)
                          ,name='thr-mult')
    thr.start()
    print("Многопоточная функция начала работу!\n")
