class Config:
    '''
    General configuration parent class
    '''
    API_KEY = 'd2058fcf62674d56874e601e24678c59'
    base_Url = 'https://newsapi.org/v2/top-headlines/sources?apiKey='



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True