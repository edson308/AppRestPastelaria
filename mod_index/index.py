from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__, url_prefix="/home", template_folder='templates')

''' rotas dos formulários '''
@bp_index.route('/', methods=['GET','POST'])
def formListaIndex():
    return render_template('formIndex.html'), 200