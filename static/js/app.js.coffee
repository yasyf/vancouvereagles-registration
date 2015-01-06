VancouverEagles = angular.module 'VancouverEagles', ['ngMaterial', 'ngRoute', 'ui.mask']

VancouverEagles.controller 'RootCtrl',  ['$scope', '$location', 'User', ($scope, $location, User) ->
  $scope.goHome = ->
    $location.path '/registrations'

  if $location.path() isnt '/login' and not User.check()
    $location.path '/login'
]

VancouverEagles.config ['$routeProvider', '$locationProvider', ($routeProvider, $locationProvider) ->
  $routeProvider
  .when '/registrations',
    templateUrl: '/template/index'
    controller: 'IndexCtrl'
  .when '/registration/:registrationId',
    templateUrl: '/template/registration'
    controller: 'RegistrationCtrl'
  .when '/schedule/:registrationId',
    templateUrl: '/template/schedule'
    controller: 'ScheduleCtrl'
  .when '/payment/:registrationId',
    templateUrl: '/template/payment'
    controller: 'PaymentCtrl'
  .when '/login',
    templateUrl: '/template/login'
    controller: 'LoginCtrl'
  .otherwise
    redirectTo: '/registrations'

  $locationProvider
  .html5Mode(true)
  .hashPrefix('!')

]
