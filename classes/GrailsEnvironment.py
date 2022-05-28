from classes.AbstractEnvironment import AbstractEnvironment
class GrailsEnvironment(AbstractEnvironment):
    JS_ENV_URLS=[]
    def __init__(self):
        self.environment_name='grails'
        self.add_aditional_attributes(self.get_environment_from_file());
        
    def add_aditional_attributes(self, config_i):
        self.JS_ENV_URLS=config_i.JS_ENV_URLS;

    def show(self):
        urls=','.join(self.JS_ENV_URLS)
        print(f'Versão: {self.version}, jsUrls:{urls}');