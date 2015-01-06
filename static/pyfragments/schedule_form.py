# This file is used as a template to pre-load the database, and may not be up-to-date

def _make_location(days, times, extra):
  d = dict([x for x in zip(days, times) if x[1]])
  d.update(extra)
  return {k[:k.index(' (')].replace(' ', '_').lower():'{} [{}]'.format(k, v) for k,v in d.items()}

def make_west(times, extra={}):
  days = ["Monday (Trafalgar)", "Wednesday (Trafalgar)", "Thursday (Kitchener)", "Friday (Kitchener)"]
  return _make_location(days, times, extra)

def make_central(times, extra={}):
  days = ["Monday (Van Horne)", "Wednesday (Van Horne)", "Friday (Jamieson)"]
  return _make_location(days, times, extra)

def make_northeast(times, extra={}):
  days = ["Tuesday (Dr. Lord)"]
  return _make_location(days, times, extra)

def transform(data):
  times = [k for k,v in data.items() if v]
  return {'times': times}

def form(**kwargs):
  checkboxes = {
    "west": {
      1: make_west(["5:00pm - 6:00pm", None, "5:00pm - 6:00pm", "5:00pm - 6:00pm"]),
      2: make_west(["6:00pm - 7:00pm", "5:00pm - 6:00pm", "6:00pm - 7:00pm", "6:00pm - 7:00pm"]),
      3: make_west(["7:00pm - 8:00pm"]*4, {"Wednesday 2 (Trafalgar)": "6:00pm - 7:00pm"}),
      4: make_west(["8:00pm - 9:30pm"]*4),
      5: make_west([None]*4, {"Friday (Jamieson)": "8:30pm - 10:00pm"})
    },
    "central": {
      1: make_central(["5:00pm - 6:00pm"]*2 + [None]),
      2: make_central(["6:00pm - 7:00pm"]*2 + ["5:00pm - 6:00pm"]),
      3: make_central(["7:00pm - 8:00pm"]*2 + ["6:00pm - 7:00pm"]),
      4: make_central(["8:00pm - 9:30pm"]*2 + ["7:00pm - 8:30pm"]),
      5: make_central([None]*2 + ["8:30pm - 10:00pm"]),
    },
    "northeast": {
      1: make_northeast(["5:00pm - 6:00pm"]),
      2: make_northeast(["6:00pm - 7:00pm"]),
      3: make_northeast(["7:00pm - 8:00pm"])
    }
  }
  rows = {time:[label, "checkbox"] for time,label in checkboxes[kwargs['location']][int(kwargs['league'])].items()}
  return {
    'rows': [{k:v} for k,v in rows.items()],
    'optional': rows.keys()
  }
