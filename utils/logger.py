import datetime


# def write_file(file_name, write_str):
#     with open('file_name', 'w') as file:
#         file.write(write_str)


def logger(patch):
    def logger_(old_function):
        def new_function(*args, **kwargs):
            with open(patch, 'a') as f:
                print(datetime.datetime.now(), file=f)
                print(f'Вызвана функция {old_function.__name__} с аргументами {args} и {kwargs}', file=f)
                result = old_function(*args, **kwargs)
                print(f"Возвращаемое значение - {result}\n", file=f)
            return result
        return new_function
    return logger_