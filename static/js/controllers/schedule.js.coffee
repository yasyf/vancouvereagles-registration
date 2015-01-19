VancouverEagles.controller 'ScheduleCtrl', ['$scope', '$rootScope', 'User', '$timeout', '$routeParams', '$location', 'API',
 ($scope, $rootScope, User, $timeout, $routeParams, $location, API) ->

  index = parseInt($routeParams.registrationId, 10)
  $scope.data = {}

  User.get 'registrations', []
  .then (registrations) ->
    $timeout ->
      if index
        registration = registrations[index]
        $scope.index = index
        $rootScope.title = 'Schedule'
        $scope.formURL = "/form/readonly/schedule?location=#{registration.location}&league=#{registration.league}"
      else
        registration = registrations[registrations.length - 1]
        $scope.index = registrations.length - 1
        $rootScope.title = 'New Schedule'
        $scope.formURL = "/form/editable/schedule?location=#{registration.location}&league=#{registration.league}"
      $scope.data = _.object(_.map(registration.times, (v) -> [v, true]))

  unless index
    $scope.submit = ->
      keyCount = _.filter($scope.data, (v) -> v).length
      return unless 0 < keyCount < 3
      API.post ['form', 'process', 'schedule'],
        data: $scope.data
      .then (response) ->
        User.set "registrations.#{$scope.index}.times", response.data.times
      .then (succeeded) ->
        $timeout -> $location.path "/payment/#{$scope.index}"
]
