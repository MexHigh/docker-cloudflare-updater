from cfupdater import LOCATION, IPV6_WRONG_PREFIXES

import os
from requests import get


def getIPv4():

    try:
        ip = os.popen('{}/get_ipv4.sh'.format(LOCATION)).read().replace("\n", "")
        if ip == "":
            printToLog("Couldn't get external IPv4 via UPnP. Starting Ipifiy API...")
            ip = get('https://api.ipify.org').text
            if ip == "":
                printToLog("Couldn't call Ipifiy API")
                return None
            else: return ip
        else:
            #printToLog("Discovered IPv4: {}".format(ip))
            return ip
    except Exception as e:
        printToLog("Critical error while retrieving external IPv4: {}".format(e))
    except:
        printToLog("Critical error while retreiving external IPv4. Type unknown.")


def getIPv6():

    try:
        ip = ""
        ips = list(ipUnparsed.split("scope")[0].split("/")[0] for ipUnparsed in os.popen("ip -6 a | grep 'scope global'").read().replace(" ","").replace("inet6", "").split("\n")[0:-1])
        for ipToBeTested in ips:
          if not any(ipToBeTested.startswith(wrongPrefix) for wrongPrefix in IPV6_WRONG_PREFIXES):
            ip = ipToBeTested
        if ip == "":
            printToLog("Couldn't get external IPv6 via UPnP. Starting Ipifiy API...")
            ip = get('https://api6.ipify.org').text
            if ip == "":
                printToLog("Couldn't call Ipifiy API")
                return None
            else: return ip
        else:
            #printToLog("Discovered IPv6: {}".format(ip))
            return ip
    except Exception as e:
        printToLog("Critical error while retrieving external IPv6: {}".format(e))
    except:
        printToLog("Critical error while retreiving external IPv6. Type unknown.")


def printToLog(string):

    from datetime import datetime

    print("{} -- {}".format(datetime.now(), string))
    log = open("{}/logs/cfupdater.log".format(LOCATION), "a")
    log.write("\n{} -- {}".format(datetime.now(), string))
    log.close()
