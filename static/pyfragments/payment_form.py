# This file is used as a template to pre-load the database, and may not be up-to-date

import stripe, os

stripe.api_key = os.environ.get('STRIPE_API_KEY')

def transform(data):
  charge = stripe.Charge.create(amount=int(data['total'] * 100 * 1.03), currency='cad',
    card=data['stripe_token'], description=data['email'])
  data.update({'charge': charge.id})
  return {'paid': True, 'payment': data}

def form(**kwargs):
  costs = {
    1: {1: 120, 2: 190},
    2: {1: 120, 2: 190},
    3: {1: 120, 2: 190},
    4: {1: 160, 2: 260},
    5: {1: 160, 2: 260}
  }
  cost = costs[int(kwargs['league'])][int(kwargs['selections'])]
  total = cost
  if kwargs['registration_fee'] == 'true':
    total += 40
  return {
    'rows': [
      {
        'stripe_token': [None, 'hidden'],
        'email': [None, 'hidden'],
        'cost': [None, 'hidden', cost],
        'total': [None, 'hidden', total],
        'registration_fee': [None, 'hidden', kwargs['registration_fee']]
      }
    ],
    'button': 'Pay With Credit Card (${:,.2f})'.format(total)
  }
