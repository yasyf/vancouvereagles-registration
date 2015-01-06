VancouverEagles.controller 'PaymentCtrl', ['$scope', '$rootScope', 'User', '$timeout', '$routeParams', '$location', 'Stripe', 'API',
 ($scope, $rootScope, User, $timeout, $routeParams, $location, Stripe, API) ->

  index = parseInt($routeParams.registrationId, 10)
  $scope.data = {}
  $rootScope.title = 'Payment'

  User.get 'registrations', []
  .then (registrations) ->
    $timeout ->
      if index is undefined
        index = registrations.length - 1
      $scope.registration = registrations[index]

    User.get 'registration_years', []
  .then (registration_years) ->
    $timeout ->
      $scope.year = moment().year()
      if moment().month() >= 8
        $scope.year += 1
      $scope.query =
        league: $scope.registration.league
        selections: $scope.registration.times.length
        registration_fee: not _.contains(registration_years, $scope.year)
      $scope.formURL = "/form/editable/payment?#{$.param($scope.query)}"

  $scope.$on '$includeContentLoaded', ->
    if $scope.registration?.paid
      $('#form_submit_btn').hide()

  $scope.submit = ->
    return if $scope.registration?.paid
    Stripe.open
      amount: $scope.data.total * 100
    .then (token) ->
      $scope.data.stripe_token = token.id
      $scope.data.email = token.email
      API.post ['form', 'process', 'payment'],
        data: $scope.data
    .then (response) ->
      promises = [
        User.set "registrations.#{index}.payment", response.data.payment
        User.set "registrations.#{index}.paid", response.data.paid
      ]
      if $scope.query.registration_fee
        promises.push(User.add 'registration_years', $scope.year)
      $.when.apply($, promises)
    .then (succeededs) ->
      $timeout -> $location.path "/registrations"
]
