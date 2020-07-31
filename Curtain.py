import os
import csv
import datetime


class states:
    init_time = 0
    init_break = 0
    on_break = False
    timing_on = False
    since_start = False
    time_mod = False


def task_submition(state, root_or_start=False, entr1=False, entr2=False):
    logtime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if state == 'start':
        # Timer Starting
        data = [logtime, 'Start of Session', '00:00:00']
    elif state == 'pause':
        # pause button initiated
        data = [logtime, 'Break started', root_or_start]
    elif state == 'unpause':
        # unpause initiated
        data = [logtime, 'Break ended', root_or_start]
    elif state == 'stop':
        data = [logtime, 'End of Session', entr1]
    elif state == 'log':
        task_name = entr1.get()
        description = entr2.get()
        data = [logtime, task_name, description]
    else:
        return 'a huge fucking error'

    cwd = os.getcwd()
    filename = "timerlog.csv"
    filepath = os.path.join(cwd, filename)
    if os.path.exists(filepath):
        # open with append
        with open(filename, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    else:
        # open with write
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerows([["Time", "TaskName", "Description"], data])
    if (state == 'log') or (state == 'stop'):
        # regular log entry form closure
        root_or_start.destroy()


def start_timer():
    states.timing_on = True
    states.init_time = datetime.datetime.now()
    task_submition('start')


def stop(root):
    duration = stringify_timedate(datetime.datetime.now() - states.init_time)
    task_submition('stop', root_or_start=root, entr1=duration)


def break_duration():
    return stringify_timedate(datetime.datetime.now() - states.init_break)


# change the task submition function to handle 'states' rather than all these true false statements
def pause_timer(app):
    print(app.pause_button.config('text')[-1])
    if app.pause_button.config('text')[-1] == 'Unpause':
        print('now weere unpausing')
        task_submition('unpause', root_or_start=break_duration())
        timing_on = True
        app.pause_button.config(text='Pause')
    else:
        print('now were pausing')
        states.init_break = datetime.datetime.now()
        task_submition('pause', root_or_start=states.init_break)
        timing_on = False
        app.pause_button.config(text='Unpause')


def stringify_timedate(dt):
    '''should only be used on datetime-delta objs'''
    seconds = dt.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return'{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))  # since.strftime("%H:%M:%S")


def time(app):
    time_string = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    app.clock_label.config(text=time_string)
    app.clock_label.after(1000, lambda: time(app))


def time_since(app):
    cwt = datetime.datetime.now()
    if states.timing_on:
        since_start = cwt - states.init_time
        app.shift_timer.config(text=stringify_timedate(since_start))
        states.time_mod = True
    elif ((not states.timing_on) and states.since_start) and states.time_mod:
        app.shift_timer.config(text=stringify_timedate(states.since_start))
        states.time_mod = False
    else:
        app.shift_timer.config(text='--/--/--')
        states.time_mod = True
    app.shift_timer.after(1000, lambda: time_since(app))
