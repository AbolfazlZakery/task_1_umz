# اولین تابع عدد رندوم میخواد تحویل بدیم دومین تابععدد های دودویی میده بادید در 20 ثانیه هر تعداد میتونی جواب بدی بعد بهت بگه  چند تا درسته غلط تابع سوم یه پسورد با شرایط اینکه 8 کاراکتری باشه و از حروف بزرگ و کوچک استفاده بشه و از اعداد استفاده بشه بعد ما اگه با مچین شرایطی گذروازه رو وارد کردیم و موجود بود اسم طرف رو به ما تحویل میده
import string
from time import perf_counter


def calculate_magic_numbers(start, end):
    x = 0.5
    return x * (end - start) + start


start = int(input("start: "))
end = int(input("end: "))
print(calculate_magic_numbers(start, end))


def exam_numbers():
    list_question = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011','1100', '1101', '1110', '1111']
    list_answer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    finish_list = []
    start_time = perf_counter()
    for i in range(16):
        print(f"{list_question[i]}: ", end='')
        answer = input()
        if answer in list_answer[i]:
            finish_list.append(True)
        else:
            finish_list.append(False)
        end_time = perf_counter()
        if end_time - start_time >= 20:
            break
    return finish_list


print(exam_numbers())


import string

#مربوط به بخش سوم سوال 2 تابع بکار رفت
def try_passport(password):
    confirmation = [False, False, False, False]
    for i in password:
        if len(password) == 8:
            confirmation[3] = True
        if i in string.ascii_uppercase:
            confirmation[0] = True
        if i in string.ascii_lowercase:
            confirmation[1] = True
        if i in string.punctuation:
            confirmation[2] = True
    if False not in confirmation:
        return True
    else:
        return False


def check_pass():
    username = input("Enter your username: ").split(" ")
    password = input("Enter your password: ").split(" ")
    correct_password = []
    k = 0
    for i in password:
        if try_passport(i):
            correct_password.append(username[k])
            k += 1
        else:
            k += 1
    return correct_password


print(check_pass())

