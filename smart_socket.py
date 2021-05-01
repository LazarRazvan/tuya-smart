import tinytuya
import time
# TODO:Global info about socket
SOCKET_ID   = 'bf124dacc393877023yyys'
SOCKET_IP   = '192.168.100.55'
SOCKET_KEY  = '47b927234326c368'

#d = tinytuya.OutletDevice('DEVICE_ID_HERE', 'IP_ADDRESS_HERE', 'LOCAL_KEY_HERE')
#d.set_version(3.3)
#data = d.status() 
#print('set_status() result %r' % data)

# Scan devices from local network
def tuya_scan_devices():
    print("Scanning all smart devices from local network...")
    #devices = scanDevices()
    tinytuya.scan()

def tuya_wizard():
    print("Running wizard for smart devices...")
    tinytuya.wizard()

def get_smart_socket_status():
    d = tinytuya.OutletDevice(SOCKET_ID, SOCKET_IP, SOCKET_KEY)
    d.set_version(3.3)
    data = d.status() 
    print('set_status() result %r' % data)

    # Suppose socket is already turned on
    print("=================================================")
    print("Start switching socket states!")
    print("=================================================")

    for x in range(10):
        if x % 2 == 0:
            print("Switching socket off")
            d.turn_off()
        else:
            print("Switching socket on")
            d.turn_on()
        
        # Sleep 3 seconds before switching states
        time.sleep(3)
        
    print("=================================================")
    print("End switching socket states!")
    print("=================================================")

if __name__ == "__main__":
    #tuya_scan_devices()
    #tuya_wizard()
    get_smart_socket_status()