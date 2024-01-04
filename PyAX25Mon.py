"""
PyAX25Mon is a program to read & print KISS frames from a TCP Socket.

For use with programs like Dire Wolf.
"""
#import time
#from threading import Thread
from bitarray import bitarray
import configparser

from rich import print
#from ax253 import Frame
import kiss

config = configparser.ConfigParser()
config.read('config.ini')

ki = kiss.classes.TCPKISS(host=config["pyax25mon"]["host"], port=int(config["pyax25mon"]["port"]), strip_df_start=True)

def print_recv_frame(frame):
    print('[bright_white]Data received : [/bright_white][bright_red]'+ str(frame) + "[/bright_red]")
    ##########################################    
        
    ''' Grab Dest Callsign from AX25 frame '''

    ##########################################
    ##########################################
    print("Dest callsign in bytes : ", end="")
    print(str(frame[:6]), end="")
    print(" - and in hex : ", end="")
    for b in frame[:6]:
        print(str(hex(b>>1)), end="")
        print("\\", end="")
    print("")
    print("Dest callsign encoded in bytes : ", end="")
    dest_callsign = bytes(b >> 1 for b in frame[:6]).rstrip()
    print(dest_callsign, end="")
    print(" - and decoded('utf-8') to str : ", end="")
    decode_dest_callsign = dest_callsign.decode("utf-8")
    print("[green]" + decode_dest_callsign + "[/green]")
    
    ##########################################
    ##########################################
        
                
    ''' Grab Dest SSID byte from AX25 frame '''


    ##########################################
    ##########################################
    print("Dest ssid byte : ", end="")
    dest_ssid = int(bytes(frame[6:7]).hex(), 16)
    dest_ssid_r = int('{:08b}'.format(dest_ssid)[::-1], 2).to_bytes()
    print(dest_ssid_r, end="")
    dest_ssid_bits = bitarray()
    dest_ssid_bits.frombytes(dest_ssid_r)
    print(" and in bits : ", dest_ssid_bits)
    dest_ssid_hdlc_bit = dest_ssid_bits[0]
    dest_ssid_encoding_bits = dest_ssid_bits[1:5]
    dest_ssid_rrbits = dest_ssid_bits[5:7]
    dest_ssid_cr_bit = dest_ssid_bits[7]
    print("Dest HDLC bit 0 : " + str(dest_ssid_hdlc_bit) + " - SSID bits 1-4 : " + str(dest_ssid_encoding_bits) + " - SSID rr bits 5-6 : " + str(dest_ssid_rrbits) + " - SSID c_r bit 7 : " + str(dest_ssid_cr_bit))
    ##########################################
    ##########################################
        
        
    ''' Grab Src Callsign from AX25 frame '''

    ##########################################
    ##########################################
    print("Src callsign in bytes : ", end="")
    print(frame[7:13], end="")
    print(" - and in hex : ", end="")
    for b in frame[7:13]:
        print(hex(b>>1), end="")
        print("\\", end="")
    print("")
    print("Src callsign encoded in bytes : ", end="")
    src_callsign = bytes(b >> 1 for b in frame[7:13]).rstrip()
    print(src_callsign, end="")
    print(" - and decoded('utf-8') to str : ", end="")
    decode_src_callsign = src_callsign.decode("utf-8")
    print("[green]" + decode_src_callsign + "[/green]")
    ##########################################
    ##########################################
    ''' Grab Src SSID byte from AX25 frame '''
    ##########################################
    ##########################################
    print("Src ssid byte : ", end="")
    src_ssid = int(bytes(frame[13:14]).hex(), 16)
    src_ssid_r = int('{:08b}'.format(src_ssid)[::-1], 2).to_bytes()
    print(src_ssid_r, end="")
    src_ssid_bits = bitarray()
    src_ssid_bits.frombytes(src_ssid_r)
    print(" and in bits : ", src_ssid_bits)
    src_ssid_hdlc_bit = src_ssid_bits[0]
    src_ssid_encoding_bits = src_ssid_bits[1:5]
    src_ssid_rrbits = src_ssid_bits[5:7]
    src_ssid_cr_bit = src_ssid_bits[7]
    print("Src HDLC bit 0 : " + str(src_ssid_hdlc_bit) + " - SSID bits 1-4 : " + str(src_ssid_encoding_bits) + " - SSID rr bits 5-6 : " + str(src_ssid_rrbits) + " - SSID c_r bit 7 : " + str(src_ssid_cr_bit))
    ##########################################
    ##########################################
    ''' Grad Control Byte from Frame '''
    ##########################################
    ##########################################
    print("Frame control byte : ", end="")
    frame_ctrl_byte = frame[14:15]
    print(frame_ctrl_byte, end="")
    frame_ctrl_bits = bitarray()
    frame_ctrl_bits.frombytes(frame_ctrl_byte)
    print(" - and in bits - ", end="")
    print(frame_ctrl_bits)
    ##########################################
    ##########################################
    ''' Grab PID byte from frame '''  
    ##########################################
    ##########################################
    pid_byte = frame[15:16]
    print("Frame PID byte : ", end="")
    print(pid_byte, end="")
    pid_bits = bitarray()
    pid_bits.frombytes(pid_byte)
    print(" - and the bits : ", end="")
    print(pid_bits)
    ##########################################
    ##########################################
    ''' Grab Info from AX25 frame'''
    
    ##########################################
    ##########################################
    info_bytes = frame[16:]
    info = info_bytes.decode('utf-8')
    info1 = info.split("\r")
    print("Frame Info in str : ", end="")
    for b in info1:
        print("[green]" +  b + "[/green]")
    print("")
    
# def send_msg():
#     while True:
#         frame = Frame.u_ui(
#             destination="NL3NVV",
#             source=config["pyax25mon"]["mycall"],
#             path=[],
#             info="test",
#             dcr = False,
#             scr = True,
#         )
#         # print(frame)
#         ki.write(frame)
#         ki.write(b'\x9c\x98r\xae\x8c\x98`\x9c\x98d\x9a\xac\xac\xe11')
#         time.sleep(10)
    
def main():
    ki.start()
    print('[bright_green]Connected to Direwolf on[/bright_green][bright_red] ' + config['pyax25mon']['host'] + '[/bright_red][bright_green] port : [/bright_green][bright_red]' + config['pyax25mon']['port'] + "[/bright_red]")
    # try:
    #     Thread(target=send_msg).start()
    # except:
    #     pass

    ki.read(callback=print_recv_frame, min_frames=None)

if __name__ == "__main__":
    main()
    