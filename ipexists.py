#!/usr/bin/python3
from optparse import OptionParser
import sys
import re

def get_host_ipaddresses():
    ips = []
    exit_code , stdout, stderr = run(cmd='ifconfig')
    if exit_code == 0:
        for line in stdout.split('\n'):
            if 'inet' in line:
                ip = line.strip()
                ip = re.split(' |%',ip)[1]
                ips.append(ip)
    return ips

def run(cmd):
    import sys
    import subprocess
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, universal_newlines = True)
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout.strip(), stderr

if __name__ == '__main__':

    host_ips = get_host_ipaddresses()
    required_args = "ip".split()
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest = "ip",help = "Comma seperated IP addresses to check if exist.")
    parser.add_option("-c", "--compare", type = "choice", choices = ('all','any'), default = ('any'), help = "Match any or all IPs %s. Default: %s"%('all', 'any'))
    parser.add_option("-v", "--verbose", action = "store_true", dest="verbose", default = False, help = "Verbose, print matched IPs.")
    (options, args) = parser.parse_args()

    for r in required_args:
        if options.__dict__[r] is None:
            parser.error("parameter %s required"%r)

    ips = options.ip.split(',')
    cmp = options.compare
    vrb = options.verbose

    matches = []
    for i in ips:
        if i in host_ips:
            matches.append(i)
            if vrb == True:
                print(i)
    if len(matches) == 0:
        sys.exit(1)
    if cmp == 'all' and len(matches) == len(ips):
        sys.exit(0)
    elif cmp == 'all' and len(matches) != len(ips):
        sys.exit(1)
    sys.exit(0)
