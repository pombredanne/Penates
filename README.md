Penates
=======

Group of Ansible tasks for configuring a basic private network with the following services:

  * PKI (openssl)
  * LDAP (openldap)
  * DHCP (isc-dhcp-server)
  * DNS (powerdns)
  * NTP (ntpd)
  * Kerberos (MIT kerberos)
  * webservices (PenatesServer)
  * pkinit for users

Processes
---------

  * a new machine is installed:
  
    * register itself (create Kerberos principal, private key, public SSH key, certificate, PTR DNS record, A/AAAA DNS record, SSHFP DNS record) and get a host keytab
        GET https://directory01.{{ domain }}/no-auth/get_host_keytab/<hostname>
    * get private key and certificate
        GET https://directory01.{{ domain }}/auth/get_host_certificate/
    * register SSH keys
        POST https://directory01.{{ domain }}/auth/set_ssh_pub/
    * register its MAC address with its (primary) IP address
        GET https://directory01.{{ domain }}/auth/set_dhcp/<mac_address>/

  * a new service is installed:
   
    * register itself (protocol://hostname:port/) with a description, register CNAME and SRV DNS records
        GET https://directory01.{{ domain }}/auth/set_service/<scheme>/<hostname>/<port>/?keytab=<HTTP>&protocol=udp
    * get private key and certificate
        GET https://directory01.{{ domain }}/auth/get_service_certificate/<scheme>/<hostname>/<port>/?protocol=udp
    * get keytab
        GET https://directory01.{{ domain }}/auth/get_service_keytab/<scheme>/<hostname>/<port>/?protocol=udp
    
  * register a foreign domain name:
        GET https://directory01.{{ domain }}/auth/set_extra_service/<hostname><?ip=<ip>
    
  * a new user is created by admin:
  
    * create password
    * create certificate (email, authent)
    * create ssh public key
    * create private key


TODO
====

Step 1
------

  * [OK] IP fixe
  * [OK] set machine keytab/certificate/rsa ssh key
  * [OK] NTP
    * crypto authentication
  * [OK] A/AAAA external records
  * [OK] user creation
  * [OK] group creation
  * [OK] set user password
  * [OK] get self certificate
  * [OK] pkinit : kinit -X "X509_user_identity=FILE:${cert}" ${principal}  ; kinit -C FILE:${cert} ${principal}
  * [OK] tests pour chaque étape
  * [OK] DANE
  * [OK] DNSSEC
  * SMTP
    * [OK] système (sans auth mais local uniquement)
    * [OK] utilisateur (ldap)
    * [OK] spamassassin
    * [OK] dkim
    * [OK] spf
    * clamav
    * utilisateur (kerberos)
    
  * [OK] IMAP4
    * [OK] utilisateur (ldap)
    * [OK] utilisateur (kerberos)

  * [OK] kerberos authent on machines
  * [OK] revoke certificate
  * [OK] sudo for admins
  * [OK] LDAP autz on machines (netgroups)
  * utiliser DNSSEC
  * external DNS config

Step 2
------

  * fail2ban
    * [OK] ssh
    * [OK] dovecot
    * opensmtpd
    * kerberos
  * [OK] logging
    * [OK] centralization
    * [OK] >= warning
    * [OK] logrotate
  * [OK] snmpd
  * nrpe
  * rkhunter
  * [OK] ISO generation
    * [OK] login
    * [OK] name
    * [OK] password1
    * [OK] password2
    * [OK] encrypt home
    * [OK] configure LVM?
  * [OK] CA generation
  * supervision
    * shinken
    * nrpe
    * php4nagios ?
    * graphite ?
    * snmp
  * TFTP server + ISO mirror
  * ubuntu mirror
  * moneta mirror
  * remove machine
  * remove service
  * remove external service
  * disable user


Step 3
------

  * XML profiles for iOS / OS X
  * XMPP
  * proxy HTTP + kerberos

Step 4
------

  * Plex
  * IRC bouncer
  * Seafile

Step 5
------

  * Gitlab
  * CardDAV, CalDAV
  * Readthedocs
  * Updoc
  * Vagrant mirror
  * Pypi mirror
  * Asterisk
  
Step 6
------

  * infrastucture secondaire (LDAP, Kerberos, DNS, DHCP, NTP, SMTP)
  * analyse de logs
  
Step 7
------

  * VPN
  * 802.1x
  * backup
  * restauration depuis le backup


TODO
----

  * récupération de la conf pour les DNS secondaires
  * smtp + kerberos
  * ajouter un password admin sur penatesserver (header/get ?)
  
  * serveur d'installation :
  
    * DHCP
    * miroir Ubuntu
    * miroir pour les paquets supplémentaires
    * serveur TFTP
    * génération des clefs
    
  * poste d'administration

Notes
-----

  ldapsearch -x '(&(objectClass=posixAccount)(memberof=cn=Administrators,ou=CoreGroups,dc=test,dc=example,dc=org))' -LLL
  ldapsearch -x '(&(objectClass=posixAccount)(memberof=cn=Users,ou=CoreGroups,dc=test,dc=example,dc=org))' -LLL

