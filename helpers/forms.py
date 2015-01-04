import imp
from mongo import forms

def get_form_module(name):
  form_code = forms.find_one({'name': name})['code']
  module = imp.new_module(name)
  exec form_code in module.__dict__
  return module

def update_form_module(name, code):
  forms.update({'name': name}, {'name': name, 'code': code}, upsert=True)

def update_form_module_from_file(name, filename):
  with open(filename) as f:
    update_form_module(name, f.read())
