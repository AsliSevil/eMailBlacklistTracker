import serviceControll

# -------------------------------------------------------------------
#IP YA DA DOMAIN:
ip = '62.203.2.59'
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# dnsblInfo:
fileDnsbl = open('dnsblInfo-list.txt', 'r')
LinesDnsbl = fileDnsbl.readlines()

for line in LinesDnsbl:
    params_dnsblInfo = {'bl': line,
                        'ip': ip,
                        'cb': '105772550',
                        'token': '05b3d2c267017ecf08f244bbc9a2b2ef'
                        }
    url_dnsblInfo = 'https://www3.dnsbl.info/test-a.php?'
    dnsblInfo = serviceControll.Service(url_dnsblInfo, params_dnsblInfo, ip)
    dnsblInfo.searchService()
# -------------------------------------------------------------------
