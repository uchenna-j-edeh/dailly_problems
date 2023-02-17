"""Parse a log file and count all ip address. 
"""

import re
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

def parse_log(content):
    lines = content.split('\n')
    ips = {}
    for line in lines:
        ip = pattern.search(line)
        if ip is not None:
            ip = ip[0]
            if ips.get(ip, False):
                ips[ip] += 1
            else:
                ips[ip] = 1

    for i in ips:
        print(i, ips[i])


logs = """
21:28:27.318642 IP lab022-VirtualBox.ssh > 192.168.4.33.56440: Flags [P.], seq 6984:7340, ack 1, win 501, options [nop,nop,TS val 532834705 ecr 402128081], length 356
21:28:27.326989 IP 192.168.4.33.56440 > lab022-VirtualBox.ssh: Flags [.], ack 7340, win 2048, options [nop,nop,TS val 402128228 ecr 532834705], length 0
21:28:27.455064 IP lab022-VirtualBox.ssh > 192.168.4.33.56440: Flags [P.], seq 7340:7696, ack 1, win 501, options [nop,nop,TS val 532834841 ecr 402128228], length 356
21:28:27.464283 IP 192.168.4.33.56440 > lab022-VirtualBox.ssh: Flags [.], ack 7696, win 2048, options [nop,nop,TS val 402128364 ecr 532834841], length 0
21:28:27.556419 IP lab022-VirtualBox.ssh > 192.168.4.33.56440: Flags [P.], seq 7696:8052, ack 1, win 501, options [nop,nop,TS val 532834942 ecr 402128364], length 356
21:28:27.566605 IP 192.168.4.33.56440 > lab022-VirtualBox.ssh: Flags [.], ack 8052, win 2048, options [nop,nop,TS val 402128464 ecr 532834942], length 0
21:28:27.664108 IP lab022-VirtualBox.ssh > 192.168.4.33.56440: Flags [P.], seq 8052:8408, ack 1, win 501, options [nop,nop,TS val 532835050 ecr 402128464], length 356
21:28:27.671452 IP 192.168.4.33.56440 > lab022-VirtualBox.ssh: Flags [.], ack 8408, win 2048, options [nop,nop,TS val 402128572 ecr 532835050], length 0
21:28:27.771730 IP lab022-VirtualBox.ssh > 192.168.4.33.56440: Flags [P.], seq 8408:8764, ack 1, win 501, options [nop,nop,TS val 532835158 ecr 402128572], length 356
21:28:27.779110 IP 192.168.4.33.56440 > lab022-VirtualBox.ssh: Flags [.], ack 8764, win 2048, options [nop,nop,TS val 402128680 ecr 532835158], length 0
21:28:27.877286 IP lab022-VirtualBox.ssh > 192.168.4.33.56440: Flags [P.], seq 8764:9120, ack 1, win 501, options [nop,nop,TS val 532835263 ecr 402128680], length 356
21:28:27.884109 IP 192.168.4.33.56440 > lab022-VirtualBox.ssh: Flags [.], ack 9120, win 2048, options [nop,nop,TS val 402128785 ecr 532835263], length 0
"""

parse_log(logs)