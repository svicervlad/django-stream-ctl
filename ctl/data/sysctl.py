import subprocess
from datetime import datetime


def simple_command(self):
    self = subprocess.check_output(str(self).split())
    return self


def command(self):
    self = simple_command(self).decode()
    return self


def commands(self, cmd):
    #     This function run or stop all timers
    ex = []
    flag = 0
    for i in self:
        self = subprocess.check_call(str(i).split())
        if self == 0:
            flag += 1
            b = i.split()
            ex.append((str(str(b[3]) + " " + str(cmd))))
    if flag == 4:
        return cmd
    else:
        return ex


# list command to start timers for run stream
timer_news = ["systemctl --user start news_start.timer",
              "systemctl --user start news_stop.timer",
              "systemctl --user start news_stop_repeate.timer",
              "systemctl --user start news_start_repeat.timer"]


class Sys:
    #     Sys class to get system and status information, run systemd service and timers
    @staticmethod
    def timers_start():
        return commands(timer_news, "start")

    @staticmethod
    def timers_stop():
        c = []
        for i in timer_news:
            c.append(i.replace("start", "stop", 1))
        return commands(c, "stop")

    @staticmethod
    def list_timers():
        cmd = command("systemctl --user list-timers --all")
        if cmd[0] == "0":
            return "False"
        else:
            return "Active"

    @staticmethod
    def err():
        return command("journalctl -p err -b")

    @staticmethod
    def stream_status():
        try:
            command("systemctl --user status news.service --no-pager")
            return "Active"
        except Exception:
            return "False"

    @staticmethod
    def stream_start():
        try:
            return command("systemctl --user start news.service")
        except Exception:
            return "False"

    @staticmethod
    def stream_stop():
        command("systemctl --user stop news.service")
        return "Stop"

    @staticmethod
    def next_start_release():
        #         get times run streams
        try:
            timers_out = command("systemctl --user list-timers ")
            col = []
            for i in timers_out.split("\n"):
                col.append(i.split())
            next_start = []
            for data in col[1:5]:
                if data[-2].find("stop") != -1:
                    next_start.append(data[1:3])
            date_f = []
            for i in next_start:
                date_f.append(datetime.strptime(str(i[0] + " " + i[1]), '%Y-%m-%d %H:%M:%S').isoformat())
            return date_f
        except:
            return "False"
