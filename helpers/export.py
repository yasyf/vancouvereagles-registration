import tablib

EXCLUDES = ['parents', 'times', 'payment']

def create_dataset(registrations):
  keys = reduce(lambda acc, x: acc | set(x.keys()), registrations, set())
  days = reduce(lambda acc, x: acc | set(x['times']), registrations, set())
  headers = sorted([x for x in keys if x not in EXCLUDES], key=lambda x: x.split('_')[-1])

  def format_col(data):
    col = {k:v for k,v in data.items() if k not in EXCLUDES}
    col['parents'] = ', '.join(data['parents'])
    col.update({day: day in data['times'] for day in days})
    if data.get('payment'):
      data['total_paid'] = data['payment']['total']
    else:
      data['total_paid'] = 0
    return [data[x] for x in headers]

  cols = map(format_col, registrations)
  return tablib.Dataset(*cols, headers=headers)
