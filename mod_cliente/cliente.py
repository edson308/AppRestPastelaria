from webbrowser import get
from flask import Blueprint, render_template,request
import requests
from funcoes import Funcoes
bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' endereços do endpoint '''
urlApiClientes = "http://localhost:8000/cliente/"
urlApiCliente = "http://localhost:8000/cliente/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}



''' rotas dos formulários '''
@bp_cliente.route('/', methods=['GET','POST'])
def formListaCliente():

    try:
        response = requests.get(urlApiClientes, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaCliente.html', result=result)
    except Exception as e:
        return render_template('formListaCliente.html', erro=e)





@bp_cliente.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        # id_funcionario = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        login= request.form['login']
       # senha = request.form['senha']
        senha = Funcoes.cifraSenha(request.form['senha'])
        matricula = request.form['matricula']
        pega_fiado=request.form['pega_fiado']

        # monta o JSON para envio a API
        payload = { 'nome': nome, 'cpf': cpf, 'telefone': telefone,'login': login,  'senha': senha,'matricula': matricula,'pega_fiado':pega_fiado }
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiClientes, headers=headers, json=payload)
        result = response.json()
        return render_template('formListaCliente.html', msg=result)
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e)






    










@bp_cliente.route('/form-cliente/', methods=['GET','POST'])
def formCliente():
    return render_template('formCliente.html')


