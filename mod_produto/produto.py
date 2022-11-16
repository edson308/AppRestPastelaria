from webbrowser import get
from flask import Blueprint, render_template,request
import requests
import base64

bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' endereços do endpoint '''
urlApiProduto = "http://localhost:8000/produto/"
urlApiProdutos = "http://localhost:8000/produto/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}



''' rotas dos formulários '''
@bp_produto.route('/', methods=['GET','POST'])
def formListaProduto():
    try:
        response = requests.get(urlApiProduto, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaProduto.html', result=result)
    except Exception as e:
        return render_template('formListaproduto.html', erro=e)


@bp_produto.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        # id_funcionario = request.form['id']
        nome = request.form['nome']
        preco = request.form['preco']
        qtd = request.form['qtd']
        descricao= request.form['descricao']
        foto = "data:" + request.files['foto'].content_type + ";base64," + str(base64.b64encode(request.files['foto'].read()), "utf-8")
        

        # monta o JSON para envio a API
        payload = { 'nome': nome, 'preco': preco, 'qtd': qtd,'descricao': descricao,  'foto': foto}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiProduto, headers=headers, json=payload)
        result = response.json()
        return render_template('formListaproduto.html', msg=result)
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e)






@bp_produto.route('/form-produto/', methods=['GET','POST'])
def formProduto():
    return render_template('formProduto.html')
