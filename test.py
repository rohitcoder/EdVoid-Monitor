import pyshark
from core import system
from pyshark.tshark.tshark import get_tshark_interfaces

zoomIpRange = system.ReadFile('footprints/zoom_ip.txt', 'list', True)

PortRanges = ['19302-19308']
ports = ['3389', '5938', '5939', '3478', '3479']

for PortRange in PortRanges:
    port = PortRange.split('-')
    for i in range(int(port[0]), int(port[1])+1):
        ports.append(str(i))

IPfilterQuery = ' || ip.dst == '.join(zoomIpRange)
IPfilterQuery = 'ip.dst == '+IPfilterQuery.lstrip(' || ')


FilterTCPPortsQuery = ' || tcp.port == '.join(ports)
FilterTCPPortsQuery = 'tcp.port == '+FilterTCPPortsQuery.lstrip(' || ')


FilterUDPPortsQuery = ' || udp.port == '.join(ports)
FilterUDPPortsQuery = 'udp.port == '+FilterUDPPortsQuery.lstrip(' || ')


capture = pyshark.LiveCapture(interface='en0', display_filter=FilterUDPPortsQuery+' || '+FilterTCPPortsQuery+' || '+IPfilterQuery)

for packet in capture.sniff_continuously(packet_count=5):
    print("Packet arrived {} ".format(packet))