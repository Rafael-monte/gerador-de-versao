class ArgsController:
    __PROGRAM_FLAGS=['-angular', '-spring', '-grails']
    __ENVIRONMENT_FLAGS=['env=hom', 'env=prod','env=rovitex','env=whatsapp2']
    __ENV_KEY='env='
    projects_to_versionate=[]
    environment_to_versionate=''
    
    def get_operation_by_args(self, args):
        if type(args) == 'list':
            args = ' '.join(args)
        self.__set_programs_to_versionate(args);
        self.__set_environment_to_versionate(args);
    
    def __set_programs_to_versionate(self, command):
        for project in self.__PROGRAM_FLAGS:
            if project in command:
                self.projects_to_versionate.append(project[1:])

    def __set_environment_to_versionate(self, command):
        for env in self.__ENVIRONMENT_FLAGS:
            if env in command:
                self.environment_to_versionate=env[env.index(self.__ENV_KEY):]
                break