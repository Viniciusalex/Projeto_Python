from datetime import datetime



class DataBr:
    def __init__(self):
        self.momento_cadastro =datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano=[
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio",
        "Junho", "Julho","Agosto", "Setembro","Novembro","Dezembro"
        ]
        mes_castro = self.momento_cadastro.month -1
        return mes_castro[mes_castro]

    def dia_semana(self):
        dia_da_semana_lista = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
        dia_da_semana= self.momento_cadastro.weekday()
        return  dia_da_semana_lista[dia_da_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return  data_formatada

    def tempo_cadastro(self):
        tempo_cadatro = datetime.today() - self.momento_cadastro
        return tempo_cadatro
