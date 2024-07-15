export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0

touch ~/.Xauthority
xauth generate $DISPLAY . trusted

python3 src/main.py