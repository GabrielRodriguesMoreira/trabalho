import _sqlite3
from datetime import datetime, date


def conecta():
    BD = 'cadastro.db'
    return _sqlite3.connect(BD)


def get_cursor(conexao):
    return conexao.cursor()


def fechar_conexao(conexao):
    conexao.close()


def novo_cadastro(nome, matricula, nome_mae, idade, telefone, sexo, endereço):
    # TODO: Verificar se a matricula ja existe
    if buscar_por_matricula(matricula):
        print('Matricula já existe!')
    else:
        sql = f'insert into aluno(nome,matricula,nome_mae,idade,telefone,sexo,endereço)' \
              f' values("{nome}","{matricula}","{nome_mae}","{idade}","{telefone}","{sexo}","{endereço}")'
        conexao = conecta()
        get_cursor(conexao).execute(sql)
        conexao.commit()
        conexao.close()


def buscar_por_nome(nome):
    sql = f"select * from aluno where nome like '{nome}%'"
    conexao = conecta()
    cursor_contato = get_cursor(conexao).execute(sql)
    return cursor_contato.fetchall()


def alterar_cadastro(nome, nome_mae, idade, sexo, telefone, endereço, matricula):
    print(matricula)
    print(type(matricula))
    sql = f"update aluno set nome='{nome}',nome_mae='{nome_mae}', idade='{idade}', sexo='{sexo}',telefone='{telefone}', endereço='{endereço}' where matricula={matricula}"
    conexao = conecta()
    get_cursor(conexao).execute(sql)
    conexao.commit()
    conexao.close()


def mostrar_todos():
    sql = f'select * from aluno'
    conexao = conecta()
    cursor_contatos = get_cursor(conexao).execute(sql)
    return cursor_contatos.fetchall()


def excluir_cadastro(matricula):
    sql = f'delete from aluno where matricula={matricula}'
    conexao = conecta()
    get_cursor(conexao).execute(sql)
    conexao.commit()
    conexao.close()


def buscar_por_matricula(matricula):
    sql = f'select * from aluno where matricula={matricula}'
    conexao = conecta()
    cursor = get_cursor(conexao).execute(sql)
    return cursor.fetchone()


hoje = date.today()
print(hoje.strftime('%d/%m/%Y'))


def gerar_log(msg):
    with open("log.txt", 'a') as log:
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        log.write(agora + ' - ' + msg + '\n')


gerar_log("")
