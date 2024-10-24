import pandas as pd

def ler(caminho_arquivo):
    try:
        df = pd.read_excel(caminho_arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    return df


def verificacao(dataframe):
    try:
        errados = []
        matricula = dataframe['Matrícula']
        for registro in matricula:
            if  str(registro).isdigit():
                continue
            else:
                print(f"Mátricula {registro} inválida ")
                errados.append(registro)
        nome = dataframe['Nome do Empregado']

        for registro in nome:
            if str(registro).strip().isalpha():
                continue
            else:
                print(f"Nome {registro} inválido")
                errados.append(registro)

        sexo = dataframe['Sexo']
        for registro in sexo:
            if registro == 'M' or registro == 'F':
                continue
            else:
                print(f"Sexo {registro} inválido")
                errados.append(registro)


        horas = dataframe['Horas Trabalhadas']
        for registro in horas:
            if str(registro).isdigit():
                continue
            else:
                print(f"Horas Trabalhadas {registro} inválidas ")
                errados.append(registro)

        return errados
    except Exception as e:
        print(f"Erro de execução {e}")


arquivo = r"C:\Users\alunodev10\Desktop\Registros_Empregados.xlsx"
dataframe = (ler(arquivo))

lista_retirados = verificacao(dataframe)

for i in lista_retirados:
    if i not in dataframe:
        print(i)
