VancouverEagles.factory "Stripe", ['$window', 'User', '$q', ($window, User, $q) ->
  Stripe =
    open: (params) ->
      deferred = $q.defer()
      User.get('username').then (email) ->
        handler = StripeCheckout.configure
          key: $window.stripeKey
          currency: 'cad'
          name: 'Vancouver Eagles'
          email: email
          image: '/static/img/logo.png'
          description: 'Registration Fee'
          token: (token) -> deferred.resolve(token)
        handler.open params
      deferred.promise

]
