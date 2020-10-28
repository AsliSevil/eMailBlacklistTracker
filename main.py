import serviceControll
import blacklistSearch
# -------------------------------------------------------------------
# IP YA DA DOMAIN:
ip = 'google.com'


#ULTRATOOLS
search_blacklist = blacklistSearch.UltraTools(ip)
search_blacklist.searchForBlacklist()

# -------------------------------------------------------------------
#MXTOOLBOX
#search_blacklist = blacklistSearch.MxToolbox(ip)
#search_blacklist.searchForBlacklist()



#WHAT IS MY IP
#search_blacklist = blacklistSearch.WhatIsMyIp(ip)
#search_blacklist.searchForBlacklist()

# -------------------------------------------------------------------




'''
# -------------------------------------------------------------------
# dnsblInfo:
fileDnsbl = open('dnsblInfo-list.txt', 'r')
LinesDnsbl = fileDnsbl.readlines()

for line in LinesDnsbl:
    params_dnsblInfo = {'bl': line,
                        'ip': ip,
                        'cb': '1047725336',
                        'token': '19f7a69caad8e97c7c1198883edd0938'
                        }
    url_dnsblInfo = 'https://www4.dnsbl.info/test-a.php?'
    dnsblInfo = serviceControll.Service(url_dnsblInfo, params_dnsblInfo, ip)
    dnsblInfo.searchService()
# -------------------------------------------------------------------

'''

