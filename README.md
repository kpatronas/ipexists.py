# ipexists.py
A simple script that exits with code 0 when the given ip exists on the host, 1 if not.

I created this script because i wanted a non-thinking, non-grep way to verify which host has the Virtual IP of the cluster which a script should execute only there.

Examples:
```
./ip_exists.py  -i 127.0.0.1,127.0.0.2 -c all; echo $?
1

./ip_exists.py  -i 127.0.0.1,127.0.0.2 -c any; echo $?
0

./ip_exists.py  -i 127.0.0.2 -c any; echo $?
1
```
-c parameter defaults to 'any'

```
 ./ip_exists.py  -i 127.0.0.2 ; echo $?
1
./ip_exists.py  -i 127.0.0.2,127.0.0.1 ; echo $?
0
```
