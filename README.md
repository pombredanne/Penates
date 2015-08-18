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

Processes:

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
    
    
TODO:

  * NTP
  * DNSSEC
  * DNS / DANE
  * user creation
  * group creation
  * A/AAAA external records
  * mails