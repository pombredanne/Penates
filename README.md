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
    * get private key and certificate
    * get SSH key
    * register its MAC addresses to its IP addresses

  * a new service is installed:
   
    * register itself (protocol://hostname:port/) with a description
    * register CNAME and SRV DNS records, DHCP records
    * get private key and certificate
    * get keytab
    
  * a new user is created by admin:
  
    * create password
    * create certificate (email, authent)
    * create ssh public key
    * create private key
    
    
TODO
====

Step 1
------

  * NTP
  * DNSSEC
  * DNS / DANE
  * user creation
  * group creation
  * A/AAAA external records
  * mail
  * pkinit
  * certificates and ssh public keys in LDAP 
  * revoke certificate
  * set machine keytab/certificate/rsa ssh key

Step 2
------

  * TFTP server + ISO mirror
  * ubuntu mirror
  * moneta mirror
  * supervision
  * logging
  * kerberos authent on machines
  * LDAP autz on machines (netgroups)

Step 3
------

  * XML profiles for iOS / OS X
  * XMPP
  * IMAP/POP3
  * proxy HTTP + kerberos

Step 4
------

  * Plex
  * IRC bouncer
  * Seafile

Step 5
------

  * Gitlab
  * Maven
  * Readthedocs
  * Updoc
  * Vagrant mirror
  * SIP
  * pypi mirror
  
Step 6
------

  * infrastucture secondaire (LDAP, Kerberos, DNS+Postgres, DHCP, NTP)
  
Step 7
------

  * VPN
  * 802.1x
  * backup
  * restauration depuis le backup