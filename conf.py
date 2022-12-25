from configparser import ConfigParser


class Config:
    """
    Class saves config parameters like self attributes.
    """
    def __init__(self, config_file_path: str):
        """
        :param config_file_path: path to config file
        """
        config = ConfigParser(allow_no_value=True)
        config.read(config_file_path)
        sections = config.sections()

        for section in sections:
            for key, value in config.items(section):
                if value:
                    setattr(self, key.upper(), str(value))
                else:
                    pass


if __name__ == '__main__':
    cfg = Config('data/config.ini')
    print(dir(cfg), cfg.MODEL)
