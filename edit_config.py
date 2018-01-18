from configparser import ConfigParser
company_id = input("Please input the company ID")

cfg = ConfigParser()
    ## *** WRITE config file ***

    cfg['configData1'] = {'conf1': 'one', 'conf2': '12', 'conf3': 'false'}
    cfg['configData2'] = {}
    cfg['configData2']['config_string'] = 'string'
    cfg['configData2']['config_bool'] = 'true'
    cfg['configData2']['config_int'] = '21'
    cfg['configData2']['config_float'] = '10.221'

    with open('config.ini', 'w') as configfile:
        cfg.write(configfile)


