from configparser import ConfigParser

if __name__ == "__main__":
    cfg = ConfigParser()
    ### *** WRITE config file ***

    # cfg['configData1'] = {'conf1': 'one', 'conf2': '12', 'conf3': 'false'}
    # cfg['configData2'] = {}
    # cfg['configData2']['config_string'] = 'string'
    # cfg['configData2']['config_bool'] = 'true'
    # cfg['configData2']['config_int'] = '21'
    # cfg['configData2']['config_float'] = '10.221'
    #
    # with open('config.ini', 'w') as configfile:
    #     cfg.write(configfile)


    ### *** READ config file ***
    cfg.read('config.ini')
    print(cfg.sections())
    print(cfg.items('configData1'))
    print(cfg.get('configData1', 'conf1'))

    print(cfg.get('configData2', 'config_string'))
    print(cfg.get('configData2', 'config_bool'))
    print(cfg.get('configData2', 'config_int'))
    print(cfg.get('configData2', 'config_float'))