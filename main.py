import pandas as pd

def lerExcel(caminhoArquivo):
    try:
        arqLido = pd.read_excel(caminhoArquivo)
        return arqLido
    except FileNotFoundError:
        print(f"Arquivo com caminho {caminhoArquivo} não encontrado")
    except Exception as e:
        print(f"Erro de execução: {e}")


def verificar(funcionario): # O argumento é um registro de funcionário
    try:
        try:
            int(funcionario.iloc[0]) # .iloc[x] pega o registro do funcionário da coluna x, nesse caso  a matrícula
        except ValueError:
            print(f"Erro na matrícula do funcionário: {funcionario.iloc[0]}")
            return False

        if not (str(funcionario.iloc[1]).replace(' ', '').isalpha()): # replace tira todos os espaços
            # presentes da string
            print(f"Erro no nome do funcionário: {funcionario.iloc[1]}")
            return False

        if not (str(funcionario.iloc[2]).upper() in ['M','F']):
            print(f"Erro no sexo do funcionário: {funcionario.iloc[2]}")
            return False

        try:
            float(funcionario.iloc[3])
        except ValueError:
            print(f"Erro no salário do funcionárioc: {funcionario.iloc[3]}")
            return False

        try:
            float(funcionario.iloc[4])
        except ValueError:
            print(f"Erro nas horas do funcionário: {funcionario.iloc[4]}")
            return False

        else:
            return True

    except Exception as e:
        print(f"Erro de execuçao {e}")


def calcularSalario(num, df_func):
    salarioHora = float(df_func.iloc[3])
    horasTrabalhadas = float(df_func.iloc[4])
    salarioBruto = salarioHora * horasTrabalhadas
    descontos = salarioBruto * 0.10
    salarioLiquido =  salarioBruto - descontos

    return [salarioBruto, descontos, salarioLiquido]


def visualizar(dadosFunc, resultados, funcionariosValidos):
    try:
        visualizacao = int(input("Se quiser receber os dados consistentes de cada funcionário"
                             " digite 1, Se quiser receber apenas o total dos salários brutos digite 2: "))

        soma = sum([salario[0] for salario in resultados]) # salario in resultado é o vetor de cada salário dos
        # funcionários, tendo uma iteração aí. O salario[0] é o bruto. Então a linha está somando o salário bruto
        # de cada funcionário e armazenando em soma

        match visualizacao:
            case 1:
                contador = 0 # Para selecionar os funcionários armazenados dentro do vetor Resultado
                for i in funcionariosValidos: # i representa o código dos funcionários válidos
                    print(f"Matrícula: {dadosFunc.loc[i].iloc[0]} - " #seleciona a linha i da coluna 0
                        f"Nome: {dadosFunc.loc[i].iloc[1]} - " 
                        f"Salário Bruto: {resultados[contador][0]:.2f} - " #seleciona a linha contador da coluna 0
                        f"Valor dos descontos: {resultados[contador][1]:.2f} - "
                        f"Salário Líquido: {resultados[contador][2]:.2f} ")
                    contador += 1
                print(f"Salário bruto de todos os funcionários: {soma:.2f}")
            case 2:
                print(f"A soma dos salários brutos é de {soma:.2f}")
            case _:
                print(f" A entrada {visualizacao} é inválida")
    except ValueError:
        print("Entrada não válida")
    except Exception as e:
        print(f"Erro de execução {e}")



arquivo = r'/Users/brennog/Desktop/Pasta1.xlsx'
dataFrame = lerExcel(arquivo)

numFunc = dataFrame.shape[0] # .Shape[x] retorna a quantidade de linhas da coluna x
funcionariosValidos = []

for func in range(numFunc): # Para cada funcionário de 0 a numFunc
    linha = dataFrame.loc[func] # Seleciona todos os registros de uma linha, ou seja do funcionário
    if verificar(linha): # Se a verificação for verdadeira, o número de registro do usuário é guardado no vetor de
        # funcionariosValidos
        funcionariosValidos.append(func)

funcionariosSalarios = []
for calculo in funcionariosValidos:
    funcionariosSalarios.append(calcularSalario(calculo,dataFrame.loc[calculo])) # a função retorna um vetor de vetores

visualizar(dataFrame, funcionariosSalarios, funcionariosValidos) # Para visualizar, precisa do Dataframe, dos
# funcionários válidos e do salário de cada um