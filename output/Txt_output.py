
def text_output(dictionary):
    for (name,name_dict) in dictionary.items():
        print("For "+name+":")
        for (ttp_ioc,list_value) in name_dict.items():
            print(ttp_ioc+": "+str(list_value)[1:-1].replace("'",""))

def test():
    dict_test = dict({'./tools/scrape.py': {'TTP': ['T1021.001', 'T1560.001', 'T1219', 'T1573', 'T1486', 'T1489', 'T1490'], 
        'IPv6': ['::', '2001:0db8:0000:85a3:0000:0000:ac1f:8001', '2001:db8:0:85a3:0:0:ac1f:8001', '2001:db8:0:85a3::'], 
        'MD5': ['66682880b58943ac2358aa5416a5880f', 'f0b7fdf47863b4d6d018e35c25c66169', '8f57434b9a58fbbe29c999df50ffecc2'], 
        'SHA1': ['10886660c5b2746ff48224646c5094ebcf88c889', '7b650a8ce213738d38b60ee9d99ffae8def286e5', '4e9429cec96a08face2c8deeb01c27228b725ed2'], 
        'SHA256': ['746df05c8f3a0b07a46c0967cfbc5cbe5b9d48d0f79b6177eeedf8be6c8b34b5', 'a1efca12ea51069abb123bf9c77889fcc2a31cc5483fc14d115e44fdf07c7980', 'a1f0b78b8c1320690327800e3a5de10e7dbba7b6c752e702193a395a52c727b6'], 
        'IPv4': ['8.8.8.8', '255.255.255.255', '12.35.216.251']}})
    text_output(dict_test)

#test()