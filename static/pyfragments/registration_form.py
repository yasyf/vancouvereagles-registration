# This file is used as a template to pre-load the database, and may not be up-to-date

import datetime

YEAR = datetime.date.today().year
if 9 <= datetime.date.today().month:
  YEAR += 1

def ui_mask(pattern):
  return {"ui-mask": pattern, "placeholder": pattern}

def options(opts):
  return {x:x.capitalize() for x in opts}

def transforms():
  return \
  {
    "parents": lambda x: x.split(",")
  }

def form():
  return \
  {
    "rows": [
      {
        "first_name": ["First Name"],
        "last_name": ["Last Name"]
      },
      {
        "grade": ["Grade", "slider", {"step": 1, "min": 1, "max": 12}]
      },
      {
        "new_player": ["{{data.first_name || 'Registrant'}} Is New To The Program", "checkbox"],
        "gender": ["Gender", "radio", {"options": options(["male", "female"])}]
      },
      {
        "school": ["School"],
        "birthday": ["Birthday", "text", ui_mask("MM/DD/YY")]
      },
      {
        "address": ["Street Address"],
        "city": ["City"],
        "postal_code": ["Postal Code", "text", {"pattern": "[a-zA-Z][1-9][a-zA-Z] ?[1-9][a-zA-Z][1-9]"}],
      },
      {
        "phone": ["Home Phone", "text", ui_mask("999-999-9999")],
        "emergency_phone": ["Emergency Contact Number", "text", ui_mask("999-999-9999")],
        "email": ["Email", "email"]
      },
      {
        "parents": ["Parents' Names", "text", {"class": "long"}]
      },
      {
        "medical_problems": ["Medical Problems", "text", {"class": "long"}]
      },
      {
        "previous_experience": ["Previous Basketball Experience", "slider", {"step": 1, "min": 1, "max": 5}]
      },
      {
        "season": ["Season", "radio", {"options": {
          "fall": "Fall {}: September 22 &mdash; December 5".format(YEAR - 1),
          "winter": "Winter {}: January 5 &mdash; April 3".format(YEAR),
          "spring": "Spring {}: April 6 &mdash; June 19".format(YEAR),
          "summer": "Summer {}: June 29 &mdash; September 11".format(YEAR)
        }}],
        "league": ["League", "radio", {"options": {
          1: "League 1: 6-7 Years Old",
          2: "League 2: 8-9 Years Old",
          3: "League 3: 10-11 Years Old",
          4: "League 4: 12-14 Years Old",
          5: "League 5: 14-16 Years Old"
        }}]
      },
      {
        "location": ["Location", "radio", {"options": {
          "west": "Vancouver West",
          "central": "Vancouver Central",
          "northeast": "Vancouver Northeast",
        }}],
        "early_bird_gift": ["Early Bird Gift", "radio", {"options": {
          "tshirt": "Vancouver Eagles T-Shirt",
          "basketball": "Basketball"
        }}]
      }
    ],
    "bare": [1, 8],
    "optional": ["medical_problems", "new_player", "early_bird_gift"]
  }
