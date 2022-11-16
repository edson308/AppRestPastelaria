
from webbrowser import get
from flask import Blueprint, render_template, request, redirect, url_for
import requests
bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' endereços do endpoint '''
urlApiFuncionarios = "http://localhost:8000/funcionario/"
urlApiFuncionario = "http://localhost:8000/funcionario/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}



''' rotas dos formulários '''
@bp_funcionario.route('/', methods=['GET','POST'])
def formListaFuncionario():
    try:
        response = requests.get(urlApiFuncionarios, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaFuncionario.html',result=result )
    except Exception as e:
        return render_template('formListaFuncionario.html', erro=e)


@bp_funcionario.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        # id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = request.form['senha']
        # monta o JSON para envio a API
        payload = { 'nome': nome, 'matricula': matricula,'cpf': cpf, 'telefone': telefone, 'grupo': grupo, 'senha': senha}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiFuncionarios, headers=headers, json=payload)
        result = response.json()

        return redirect( url_for('funcionario.formListaFuncionario', msg=result) )
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e)
    #     return render_template('formListaFuncionario.html', msg=result)
    # except Exception as e:
    #     return render_template('formListaFuncionario.html', msgErro=e)




@bp_funcionario.route('/form-funcionario/', methods=['GET','POST'])
def formFuncionario():
    return render_template('formFuncionario.html')


'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListaFuncionario.html'), 200
'''