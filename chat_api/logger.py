import datetime

def get_log_filename():
    current_time = datetime.datetime.now()
    return f"Log_{current_time.strftime('%Y%m%d_%H%M%S')}.txt"

def log_response(response):
    filename = get_log_filename()
    with open(f'logs/{filename}', 'a') as file:
        file.write(response + '\n')
