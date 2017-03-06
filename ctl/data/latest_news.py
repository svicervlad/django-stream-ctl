#! /usr/bin/python3
import os
import subprocess

"""
This script getting path to latest created file for streaming if running as module.
If script's run how main script, it's returns vlc streaming command.
"""
def simple_command(self):
    self = subprocess.check_output(str(self).split())
    return self


def command(self):
    self = simple_command(self).decode()
    return self


VIDEO_ROOT = "/home/videoarchive/media/news_releases/"
all_files = os.listdir(VIDEO_ROOT)


def latest_url():
    mp4 = []
    for i in all_files:
        if i.find("mp4") != -1 and i[0].isdigit():
            mp4.append(os.path.join(VIDEO_ROOT, i))

    latest_file = max(mp4, key=os.path.getctime)
    latest_file = latest_file[19::]
    return latest_file


def latest_news():
    mp4 = []
    for i in all_files:
        if i.find("mp4") != -1 and i[0].isdigit():
            mp4.append(os.path.join(VIDEO_ROOT, i))

    latest_file = max(mp4, key=os.path.getctime)
    return latest_file


def latest_info():
    info = latest_news().split('/')[-1]
    return str(info)


sout = '#duplicate{dst=std{access=rtmp,mux=ffmpeg{mux=flv},' \
       'dst=rtmp://127.0.0.1:1935/live},dst=udp{mux=ts,dst=239.50.0.1:1234}}'


if __name__ == "__main__":
    # execute only if run as a script
    command(str("/usr/bin/cvlc -vvv " + str(latest_news()) + " --sout " + sout))


