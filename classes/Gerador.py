from classes.AngularEnvironment import AngularEnvironment
from classes.ArgsController import ArgsController
from classes.GrailsEnvironment import GrailsEnvironment
from classes.SpringEnvironment import SpringEnvironment
from classes.TerminalController import TerminalController

class Gerador:
    projetos=[AngularEnvironment(), GrailsEnvironment(), SpringEnvironment()]
    args_controller = ArgsController()
    terminal=TerminalController()
    
    def start(self, args):
        self.args_controller.get_operation_by_args(args);
        if len(self.args_controller.projects_to_versionate) > 0:
            self.filtrar_projetos_para_versionar()
            self.buscar_ambiente_para_versionar()
        else:
            self.terminal.print_error('Não encontrei nenhum projeto para versionar!')

    def filtrar_projetos_para_versionar(self):
        self.projetos = list(filter(lambda projeto:
            projeto.environment_name in self.args_controller.projects_to_versionate, self.projetos))
        
    def buscar_ambiente_para_versionar(self):
        if self.args_controller.environment_to_versionate != '':
            for projeto in self.projetos:
                projeto.environment = self.args_controller.environment_to_versionate
        else:
            self.terminal.print_warn('Nenhum ambiente informado, serao usados os ambientes que estão configurados nos arquivos js')