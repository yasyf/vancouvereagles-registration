VancouverEagles.service 'User', ['API', (API) ->
  userId = localStorage.getItem('userId')
  baseParams = ['user', userId]
  User =
    check: ->
      !!userId
    get: (key, default_=undefined) ->
      API.get baseParams.concat(['get', key])
      .then (response) ->
        response[key] or default_
    set: (key, value) ->
      params = {}
      params[key] = value
      API.post baseParams.concat(['set', key]), params
      .then (response) ->
        response[key] == value
    add: (key, value) ->
      params = {}
      params[key] = value
      API.post baseParams.concat(['add', key]), params
      .then (response) ->
        response[key] == value
]
