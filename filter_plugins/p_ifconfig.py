# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import netaddr
__author__ = 'Matthieu Gallet'


__test_string = """eth0      Link encap:Ethernet  HWaddr 08:00:27:f4:11:d0
          inet addr:10.19.1.134  Bcast:10.19.1.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fef4:11d0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:93131 errors:0 dropped:0 overruns:0 frame:0
          TX packets:52752 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:94311133 (94.3 MB)  TX bytes:4877961 (4.8 MB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:15938 errors:0 dropped:0 overruns:0 frame:0
          TX packets:15938 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:5910436 (5.9 MB)  TX bytes:5910436 (5.9 MB)"""


def parse_ifconfig(content, **kwargs):
    """
    :param content:
    :type content: :class:`str`
    :param kwargs: {'network_name': 'network_addr'}
    :return: {'kwarg_key1': None|(name, hwaddr, addr), 'kwarg_key2': None|(name, hwaddr, addr)}
    :rtype: :class:`dict`

    >>> parse_ifconfig(__test_string, test='10.19.1.0/24') == {'test': ('eth0', '08:00:27:f4:11:d0', '10.19.1.134')}
    True
    >>> parse_ifconfig(__test_string, test='10.19.2.0/24') == {'test': None}
    True

    """
    start_regexp = re.compile(r'^([\w_\-]+)\s+Link encap:([\w_\- ]+)\s+HWaddr (([a-f\dA-F]{2}):([a-f\dA-F]{2}):([a-f\dA-F]{2}):([a-f\dA-F]{2}):([a-f\dA-F]{2}):([a-f\dA-F]{2}))$')
    ip4_regexp = re.compile(r'^\s+inet addr:([\d\.]{7,})\s+.*$')
    ip6_regexp = re.compile(r'^\s+inet6 addr:\s*([\d:/a-f]+)\s+.*$')
    current_name, current_hw_addr = None, None
    result = {key: None for (key, value) in kwargs.items()}
    networks = {key: netaddr.IPNetwork(value) for (key, value) in kwargs.items()}
    for line in content.splitlines():
        matcher = start_regexp.match(line)
        if matcher:
            current_name = matcher.group(1)
            current_hw_addr = matcher.group(3)
        elif not current_name:
            continue
        matcher = ip4_regexp.match(line)
        if matcher:
            ip4 = netaddr.IPAddress(matcher.group(1))
            for network_name, network in networks.items():
                if network.version == 4 and ip4 in network:
                    result[network_name] = (current_name, current_hw_addr, str(ip4))
            continue
        matcher = ip6_regexp.match(line)
        if matcher:
            ip6 = netaddr.IPAddress(matcher.group(1).partition(str('/'))[0])
            for network_name, network in networks.items():
                if network.version == 6 and ip6 in network:
                    result[network_name] = (current_name, current_hw_addr, str(ip6))
            continue
    return result


class FilterModule(object):
    # noinspection PyMethodMayBeStatic
    def filters(self):
        return {'parse_ifconfig': parse_ifconfig, }

if __name__ == '__main__':
    import doctest

    doctest.testmod()
