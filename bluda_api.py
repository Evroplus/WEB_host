import flask

blueprint = flask.Blueprint(
    'bluda_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api')
@blueprint.route('/api/help')
def help():
    return '/api/bluda - команда для вывода всех блюд; /api/bluda/<numer> - вывод определенного блюда по номеру'

@blueprint.route('/api/bluda')
def get_bluda():
    with open('bluda.txt', mode='r', encoding='utf8') as bluda:
        bluds = bluda.readlines()
        f = ''
        for i in bluds:
            f += i + '\n'
        return f

@blueprint.route('/api/bluda/<numer>')
def get_opr_bludo(numer):
    with open('bluda.txt', mode='r', encoding='utf8') as bluda:
        f = bluda.readlines()
        return f[int(numer) - 1]