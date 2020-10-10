import time
from datetime import datetime as dt

hosts_path = "host"
redirect_host = "127.0.0.1"
website_lists = ['"www.facebook.com', 'www.gmail.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 2):
        print("Working hours...Block the sites")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for web in website_lists:
                if web in content:
                    pass
                else:
                    file.write(redirect_host + " " + web+"\n")
        break

    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in website_lists):
                    file.write(line)
            file.truncate()
        print("Sleep time..Unblock the sites")
        break


# to make it work hosts_path has to be the system path where your hosts file is residing.
# To automate this process and to make it work as system starts, change the file ext. to pyw and run it. And create a task!
