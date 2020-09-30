import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('login info', 'baseURL')
        return url

    @staticmethod
    def get_email():
        user_email = config.get('login info', 'userEmail')
        return user_email

    @staticmethod
    def get_password():
        password = config.get('login info', 'password')
        return password
