from flask import render_template, jsonify, request, g
from app import app, dev
from helpers import *

@app.before_request
def preprocess_request():
  g.dev = dev

@app.after_request
def postprocess_request(response):
  return response

@app.errorhandler(404)
def missing_page_hangler(error):
  return index_view()

@app.template_filter('attrs')
def currency_filter(mapping):
  excludes = ['options']
  if mapping:
    return ' '.join(['{}="{}"'.format(k, v) for k,v in mapping.items() if k not in excludes])
  else:
    return ''

@app.route('/')
def index_view():
  return render_template('index.html')

@app.route('/template/<name>')
def terminal_view(name):
  return render_template('fragments/_{}.html'.format(name))

@app.route('/form/<state>/<name>')
def form_view(state, name):
  module = get_form_module(name)
  form = module.form(**request.args.to_dict())
  return render_template('_form.html', form=form, state=state)

@app.route('/api/login/<username>', methods=['POST'])
def api_login_view(username):
  user = User(username=username)
  password = request.json.get('password')
  if user.check():
    if user.login(password):
      return jsonify({'error': False, 'message': 'You are now logged in as {}!'.format(username), 'userId': user.get_id()})
    else:
      return jsonify({'error': True, 'message': 'Your password was incorrect.'})
  else:
    try:
      user = User.create(username, password)
      return jsonify({'error': False, 'message': 'Your account has been created!', 'userId': user.get_id()})
    except:
      return jsonify({'error': True, 'message': 'Your account could not be created.'})

@app.route('/api/admin/export/location', methods=['POST'])
def api_admin_export_location_view():
  query = request.json.get('query', {})
  def predicate(registration):
    return all([str(registration.get(v)) == v for k,v in query.items()])
  registrations = filter(predicate, User.get_all('registrations'))
  dataset = create_dataset(registrations)
  return jsonify({'csv': dataset.csv})

@app.route('/api/admin/export/user', methods=['POST'])
def api_admin_export_user_view():
  userid = request.json.get('query', {}).get('_id')
  user = User(userid=userid)
  registrations = user.get('registrations', [])
  dataset = create_dataset(registrations)
  return jsonify({'csv': dataset.csv})

@app.route('/api/admin/get/<key>')
def api_admin_get_view(key):
  return jsonify({key: User.get_all(key)})

@app.route('/api/user/<userid>/get/<key>')
def api_user_get_view(userid, key):
  user = User(userid=userid)
  return jsonify({key: user.get(key)})

@app.route('/api/user/<userid>/set/<key>', methods=['POST'])
def api_user_set_view(userid, key):
  user = User(userid=userid)
  value = request.json.get(key)
  user.set(key, value)
  return jsonify({key: value})

@app.route('/api/user/<userid>/add/<key>', methods=['POST'])
def api_user_add_view(userid, key):
  user = User(userid=userid)
  value = request.json.get(key)
  user.add(key, value)
  return jsonify({key: value})

@app.route('/api/form/process/<name>', methods=['POST'])
def api_form_process_view(name):
  module = get_form_module(name)
  transform = module.transform
  return jsonify({'data': transform(request.json['data'])})
