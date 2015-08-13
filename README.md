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
    
    
Newly installed machines should register themselves to these services:

  * create a DHCP entry for each MAC to fix IP addresses
  * create a DNS entry for the fqdn
  * create a certificate
  * crate a Kerberos principal for the HOST/ keytab
  * create a netgroup LDAP entry for admin rights
  
