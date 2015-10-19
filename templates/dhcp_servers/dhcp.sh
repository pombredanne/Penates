#!/usr/bin/env bash
k5start -q -f /etc/host.keytab -U -- curl --anyauth -u : -o /etc/dhcp/dhcpd.conf https://{{ penates_directory_fqdn }}/auth/conf/dhcpd.conf
service isc-dhcp-server restart
service isc-dhcp-server6 restart
