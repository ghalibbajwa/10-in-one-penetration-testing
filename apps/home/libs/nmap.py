import requests
import json
import xmltodict
import subprocess


scripts = "acarsd-info,address-info,afp-ls,afp-path-vuln,afp-serverinfo,afp-showmount,ajp-auth,ajp-headers,ajp-methods,ajp-request,allseeingeye-info,amqp-info,asn-query,auth-owners,auth-spoof,backorifice-info,bacnet-info,banner,bitcoin-getaddr,bitcoin-info,bitcoinrpc-info,bittorrent-discovery,bjnp-discover,broadcast-avahi-dos,broadcast-bjnp-discover,broadcast-db2-discover,broadcast-dhcp-discover,broadcast-dhcp6-discover,broadcast-dns-service-discovery,broadcast-dropbox-listener,broadcast-eigrp-discovery,broadcast-igmp-discovery,broadcast-listener,broadcast-ms-sql-discover,broadcast-netbios-master-browser,broadcast-networker-discover,broadcast-novell-locate,broadcast-ospf2-discover,broadcast-pc-anywhere,broadcast-pc-duo,broadcast-pim-discovery,broadcast-ping,broadcast-pppoe-discover,broadcast-rip-discover,broadcast-ripng-discover,broadcast-sybase-asa-discover,broadcast-tellstick-discover,broadcast-upnp-info,broadcast-versant-locate,broadcast-wake-on-lan,broadcast-wpad-discover,broadcast-wsdd-discover,broadcast-xdmcp-discover,cassandra-info,cccam-version,cics-enum,cics-info,cics-user-enum,citrix-enum-apps-xml,citrix-enum-apps,citrix-enum-servers-xml,citrix-enum-servers,clamav-exec,clock-skew,coap-resources,couchdb-databases,couchdb-stats,creds-summary,cups-info,cups-queue-info,daap-get-library,daytime,db2-das-info,dhcp-discover,dict-info,distcc-cve2004-2687,dns-blacklist,dns-cache-snoop,dns-check-zone,dns-client-subnet-scan,dns-fuzz,dns-ip6-arpa-scan,dns-nsec-enum,dns-nsec3-enum,dns-nsid,dns-random-srcport,dns-random-txid,dns-recursion,dns-service-discovery,dns-srv-enum,dns-update,dns-zeustracker,dns-zone-transfer,docker-version,domcon-cmd,domino-enum-users,drda-info,duplicates,eap-info,enip-info,epmd-info,eppc-enum-processes,fcrdns,finger,fingerprint-strings,firewalk,firewall-bypass,flume-master-info,fox-info,freelancer-info,ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-syst,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,ganglia-info,giop-info,gkrellm-info,gopher-ls,gpsd-info,hadoop-datanode-info,hadoop-jobtracker-info,hadoop-namenode-info,hadoop-secondary-namenode-info,hadoop-tasktracker-info,hbase-master-info,hbase-region-info,hddtemp-info,hnap-info,hostmap-bfk,hostmap-crtsh,hostmap-robtex,http-adobe-coldfusion-apsa1301,http-affiliate-id,http-apache-negotiation,http-apache-server-status,http-aspnet-debug,http-auth-finder,http-auth,http-avaya-ipoffice-users,http-awstatstotals-exec,http-axis2-dir-traversal,http-backup-finder,http-barracuda-dir-traversal,http-bigip-cookie,http-cakephp-version,http-chrono,http-cisco-anyconnect,http-coldfusion-subzero,http-comments-displayer,http-config-backup,http-cookie-flags,http-cors,http-cross-domain-policy,http-csrf,http-date,http-default-accounts,http-devframework,http-dlink-backdoor,http-dombased-xss,http-domino-enum-passwords,http-drupal-enum-users,http-drupal-enum,http-enum,http-errors,http-exif-spider,http-favicon,http-feed,http-fetch,http-fileupload-exploiter,http-form-fuzzer,http-frontpage-login,http-generator,http-git,http-gitweb-projects-enum,http-google-malware,http-grep,http-headers,http-huawei-hg5xx-vuln,http-icloud-findmyiphone,http-icloud-sendmsg,http-iis-short-name-brute,http-iis-webdav-vuln,http-internal-ip-disclosure,http-jsonp-detection,http-litespeed-sourcecode-download,http-ls,http-majordomo2-dir-traversal,http-malware-host,http-mcmp,http-method-tamper,http-methods,http-mobileversion-checker,http-ntlm-info,http-open-proxy,http-open-redirect,http-passwd,http-php-version,http-phpmyadmin-dir-traversal,http-phpself-xss,http-put,http-qnap-nas-info,http-referer-checker,http-rfi-spider,http-robots.txt,http-robtex-reverse-ip,http-robtex-shared-ns,http-security-headers,http-server-header,http-shellshock,http-sitemap-generator,http-slowloris-check,http-slowloris,http-sql-injection,http-stored-xss,http-svn-enum,http-svn-info,http-title,http-tplink-dir-traversal,http-trace,http-traceroute,http-trane-info,http-unsafe-output-escaping,http-useragent-tester,http-userdir-enum,http-vhosts,http-virustotal,http-vlcstreamer-ls,http-vmware-path-vuln,http-vuln-cve2006-3392,http-vuln-cve2009-3960,http-vuln-cve2010-0738,http-vuln-cve2010-2861,http-vuln-cve2011-3192,http-vuln-cve2011-3368,http-vuln-cve2012-1823,http-vuln-cve2013-0156,http-vuln-cve2013-6786,http-vuln-cve2013-7091,http-vuln-cve2014-2126,http-vuln-cve2014-2127,http-vuln-cve2014-2128,http-vuln-cve2014-2129,http-vuln-cve2014-3704,http-vuln-cve2014-8877,http-vuln-cve2015-1427,http-vuln-cve2015-1635,http-vuln-cve2017-1001000,http-vuln-cve2017-5638,http-vuln-cve2017-5689,http-vuln-cve2017-8917,http-vuln-misfortune-cookie,http-vuln-wnr1000-creds,http-waf-detect,http-waf-fingerprint,http-webdav-scan,http-wordpress-enum,http-wordpress-users,http-xssed,iax2-version,icap-info,iec-identify,ike-version,imap-capabilities,imap-ntlm-info,informix-query,informix-tables,ip-forwarding,ip-https-discover,ipidseq,ipmi-cipher-zero,ipmi-version,ipv6-multicast-mld-list,ipv6-node-info,ipv6-ra-flood,irc-botnet-channels,irc-info,irc-unrealircd-backdoor,iscsi-info,isns-info,jdwp-exec,jdwp-info,jdwp-inject,jdwp-version,knx-gateway-discover,knx-gateway-info,krb5-enum-users,ldap-novell-getpass,ldap-rootdse,ldap-search,lexmark-config,llmnr-resolve,lltd-discovery,maxdb-info,mcafee-epo-agent,membase-http-info,memcached-info,metasploit-info,mmouse-exec,modbus-discover,mongodb-databases,mongodb-info,mqtt-subscribe,mrinfo,ms-sql-config,ms-sql-dac,ms-sql-dump-hashes,ms-sql-empty-password,ms-sql-hasdbaccess,ms-sql-info,ms-sql-ntlm-info,ms-sql-query,ms-sql-tables,ms-sql-xp-cmdshell,msrpc-enum,mtrace,murmur-version,mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122,nat-pmp-info,nat-pmp-mapport,nbd-info,nbstat,ncp-enum-users,ncp-serverinfo,ndmp-fs-info,ndmp-version,netbus-auth-bypass,netbus-info,netbus-version,nfs-ls,nfs-showmount,nfs-statfs,nntp-ntlm-info,nrpe-enum,ntp-info,ntp-monlist,omp2-enum-targets,omron-info,openlookup-info,openwebnet-discovery,oracle-enum-users,oracle-tns-version,ovs-agent-version,p2p-conficker,path-mtu,pcworx-info,pjl-ready-message,pop3-capabilities,pop3-ntlm-info,pptp-version,puppet-naivesigning,qconn-exec,qscan,quake1-info,quake3-info,quake3-master-getservers,rdp-enum-encryption,realvnc-auth-bypass,redis-info,resolveall,reverse-index,rfc868-time,riak-http-info,rmi-dumpregistry,rmi-vuln-classloader,rpc-grind,rpcap-info,rpcinfo,rsa-vuln-roca,rsync-list-modules,rtsp-methods,rusers,s7-info,samba-vuln-cve-2012-1182,servicetags,sip-call-spoof,sip-enum-users,sip-methods,skypev2-version,smb-double-pulsar-backdoor,smb-enum-domains,smb-enum-groups,smb-enum-processes,smb-enum-services,smb-enum-sessions,smb-enum-shares,smb-enum-users,smb-flood,smb-ls,smb-mbenum,smb-os-discovery,smb-print-text,smb-protocols,smb-psexec,smb-security-mode,smb-server-stats,smb-system-info,smb-vuln-conficker,smb-vuln-cve-2017-7494,smb-vuln-cve2009-3103,smb-vuln-ms06-025,smb-vuln-ms07-029,smb-vuln-ms08-067,smb-vuln-ms10-054,smb-vuln-ms10-061,smb-vuln-ms17-010,smb-vuln-regsvc-dos,smb2-capabilities,smb2-security-mode,smb2-time,smb2-vuln-uptime,smtp-commands,smtp-enum-users,smtp-ntlm-info,smtp-open-relay,smtp-strangeport,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764,sniffer-detect,snmp-hh3c-logins,snmp-info,snmp-interfaces,snmp-ios-config,snmp-netstat,snmp-processes,snmp-sysdescr,snmp-win32-services,snmp-win32-shares,snmp-win32-software,snmp-win32-users,socks-auth-info,socks-open-proxy,ssh-auth-methods,ssh-hostkey,ssh-publickey-acceptance,ssh-run,ssh2-enum-algos,sshv1,ssl-ccs-injection,ssl-cert-intaddr,ssl-cert,ssl-date,ssl-dh-params,ssl-enum-ciphers,ssl-heartbleed,ssl-known-key,ssl-poodle,sslv2-drown,sslv2,sstp-discover,stun-info,stun-version,stuxnet-detect,supermicro-ipmi-conf,targets-asn,targets-ipv6-multicast-echo,targets-ipv6-multicast-invalid-dst,targets-ipv6-multicast-mld,targets-ipv6-multicast-slaac,targets-sniffer,targets-traceroute,teamspeak2-version,telnet-encryption,telnet-ntlm-info,tftp-enum,tls-alpn,tls-nextprotoneg,tls-ticketbleed,tn3270-screen,tor-consensus-checker,traceroute-geolocation,tso-enum,unittest,unusual-port,upnp-info,ventrilo-info,versant-info,vmware-version,vnc-info,vnc-title,voldemort-info,vtam-enum,vuze-dht-info,wdb-version,weblogic-t3-info,whois-domain,whois-ip,wsdd-discover,x11-access,xdmcp-discover,xmlrpc-methods,xmpp-info"

def remove_protocol(url):
    url = url.split(":")

    return(url[1][2:])

def run_test(test):

    ip = test['test_url']
  

    
    try:
        scan(test['id'],ip)
       
        return {"success":'OK'}

    except Exception as e:
        return {"error":f'{e}'}


def execute_nmap(ip):
    """
    Execute nmap command with specified scripts and return the XML output as a string.
    """
    try:
        # Run the nmap command with XML output and specified scripts
        result = subprocess.run(['nmap', '-sCSV', '--script', scripts, '-oX', '-', ip],
                                capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None



def scan(test_id,url):
    
    scan_data = execute_nmap(url)
    scan_data = xmltodict.parse(scan_data)
   
    url = 'http://localhost:5000/nmap'
    request_data = {'progress':100, 'status':"succeeded", 'test':test_id,'nmap_data': scan_data}
    json_data = json.dumps(request_data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json_data, headers=headers)



