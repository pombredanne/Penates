#!/usr/bin/env bash
set -e
ansible-playbook -i servers_1504.ini common_pass_1.yml
say "common pass 1"
ansible-playbook -i servers_1504.ini auth_servers.yml
say "authentication server"
ansible-playbook -i servers_1504.ini common_pass_2.yml
say "common pass 2"
ansible-playbook -i servers_1504.ini dhcp_servers.yml
say "DHCP server"
ansible-playbook -i servers_1504.ini log_servers.yml
say "log server"
ansible-playbook -i servers_1504.ini ntp_servers.yml
say "NTP server"
ansible-playbook -i servers_1504.ini mail_servers.yml
say "mail server"
ansible-playbook -i servers_1504.ini supervision_servers.yml
say "supervision server"
