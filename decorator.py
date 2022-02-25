from datetime import datetime

def log_decor(file_path):

    def _log_decor(function):

        def new_function(*args, **kwargs):

            log_str = f'{datetime.now()}, {function.__name__}, {args} {kwargs} '
            result = function(*args, **kwargs)
            log_str += f'{result}\n'

            try:
                with open(file_path, 'a', encoding='UTF-8') as f:
                    f.write(log_str)
            except FileNotFoundError:
                print(f'Указаный файл или директория не существуют, лог для {function.__name__} не создан')

            return result

        return new_function

    return _log_decor
