import re
import requests
requests.packages.urllib3.disable_warnings()

IOC_REGEX = [
    {"Name":"IPv4","regex":r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"},
    {"Name":"IPv6","regex":r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"},
    {"Name":"MD5","regex":r"\b[A-Fa-f0-9]{32}\b"},
    {"Name":"SHA1","regex":r"\b[a-fA-F0-9]{40}\b"},
    {"Name":"SHA256","regex":r"\b[a-fA-F0-9]{64}\b"}]

TTP_REGEX = "T[0-1]\d{3}\.\d{3}|T[0-1]\d{3}"

# Return dict with TTP from a list of lines
def find_TTP(list_lines):
    ttp_dict=dict(TTP=[])
    for line in list_lines:
        t1_strings = re.findall(TTP_REGEX, str(line))
        if t1_strings == []: continue
        for s in t1_strings:
            if s not in ttp_dict["TTP"]:
                ttp_dict["TTP"] += [s]
    return ttp_dict

def find_IoC(list_lines):
    ioc_dict=dict()
    for line in list_lines:
        for regexioc in IOC_REGEX:
            name_regex = regexioc["Name"]
            regex = regexioc["regex"]
            t1_strings = re.findall(regex, str(line))
            if t1_strings == []: continue
            if ioc_dict.get(name_regex) is None: ioc_dict[name_regex]=[]
            for s in t1_strings:
                # We can do better here but hey it works
                if type(s) == type(('list','list')):
                    s = s[0]
                if s not in ioc_dict[name_regex]:
                    ioc_dict[name_regex] += [s]
    return ioc_dict

# For test
def test():
    list_lines = ["Remote Desktop Protocol [T1021.001]Archive via Utility [T1560.001]Remote Access Software [T1219], Encrypted Channel [T1573]Data Encrypted for Impact [T1486], Service Stop [T1489], Inhibit System Recovery [T1490]"]
    print(find_TTP(list_lines))

    # For url
    url = "http://unit42.paloaltonetworks.com/ransom-cartel-ransomware/"
    response = requests.get(url, verify=False)
    #print(find_TTP(response.iter_lines()))
    #print(find_IoC(response.iter_lines()))

    list_lines = ["Remote Desktop Protocol [T1021.001]Archive via Utility [T1560.001]Remote Access Software [T1219], Encrypted Channel [T1573]Data Encrypted for Impact [T1486], Service Stop [T1489], Inhibit System Recovery [T1490]",
    """
    md5 66682880b58943ac2358aa5416a5880f f0b7fdf47863b4d6d018e35c25c66169 8f57434b9a58fbbe29c999df50ffecc2 
    sha1 10886660c5b2746ff48224646c5094ebcf88c889 7b650a8ce213738d38b60ee9d99ffae8def286e5 4e9429cec96a08face2c8deeb01c27228b725ed2 
    sha256 746df05c8f3a0b07a46c0967cfbc5cbe5b9d48d0f79b6177eeedf8be6c8b34b5 a1efca12ea51069abb123bf9c77889fcc2a31cc5483fc14d115e44fdf07c7980 a1f0b78b8c1320690327800e3a5de10e7dbba7b6c752e702193a395a52c727b6
    ipv4 8.8.8.8 255.255.255.255 12.35.216.251
    ipv6 2001:0db8:0000:85a3:0000:0000:ac1f:8001 2001:db8:0:85a3:0:0:ac1f:8001 2001:db8:0:85a3::ac1f:8001"""]
    dict_test = dict({'./tools/scrape.py': {'TTP': ['T1021.001', 'T1560.001', 'T1219', 'T1573', 'T1486', 'T1489', 'T1490'], 
        'IPv6': ['::', '2001:0db8:0000:85a3:0000:0000:ac1f:8001', '2001:db8:0:85a3:0:0:ac1f:8001', '2001:db8:0:85a3::'], 
        'MD5': ['66682880b58943ac2358aa5416a5880f', 'f0b7fdf47863b4d6d018e35c25c66169', '8f57434b9a58fbbe29c999df50ffecc2'], 
        'SHA1': ['10886660c5b2746ff48224646c5094ebcf88c889', '7b650a8ce213738d38b60ee9d99ffae8def286e5', '4e9429cec96a08face2c8deeb01c27228b725ed2'], 
        'SHA256': ['746df05c8f3a0b07a46c0967cfbc5cbe5b9d48d0f79b6177eeedf8be6c8b34b5', 'a1efca12ea51069abb123bf9c77889fcc2a31cc5483fc14d115e44fdf07c7980', 'a1f0b78b8c1320690327800e3a5de10e7dbba7b6c752e702193a395a52c727b6'], 
        'IPv4': ['8.8.8.8', '255.255.255.255', '12.35.216.251']}})

    print(find_IoC(list_lines))
#test()