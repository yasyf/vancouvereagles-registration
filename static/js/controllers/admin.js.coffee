VancouverEagles.controller 'AdminCtrl', ['$scope', '$rootScope', 'API', '$window', '$timeout',
 ($scope, $rootScope, API, $window, $timeout) ->

  $rootScope.title = 'All Registrations'
  $scope.years = []
  $scope.seasons = []
  $scope.locations = []
  $scope.registrations = []
  $scope.data = {}

  $scope.$watch 'data', (data) ->
    if data.location
      $rootScope.title = "Vancouver #{data.location} (#{data.season} #{data.year})"
  , true

  API.get ['admin', 'get', 'registrations']
  .then (data) ->
    $timeout ->
      $scope.registrations = data.registrations
      registrations = _.flatten(_.values(data.registrations))
      $scope.years = _.uniq(_.pluck(registrations, 'year'))
      $scope.seasons = _.uniq(_.pluck(registrations, 'season'))
      $scope.locations = _.uniq(_.pluck(registrations, 'location'))
      $scope.data =
        year: $scope.years[0]
        season: $scope.seasons[0]
        location: $scope.locations[0]

  doExport = (type_, query) ->
    API.post ['admin', 'export', type_],
      query: query
    .then (data) ->
      blob = new Blob [data.csv],
        type : 'text/csv'
      $window.location = URL.createObjectURL(blob)

  $scope.exportAll = ->
    doExport 'location', {}

  $scope.exportUser = (userId) ->
    doExport 'user',
      _id: userId

  $scope.exportLocation = ->
    doExport 'location',
      year: $scope.data.year
      season: $scope.data.season
      location: $scope.data.location
]
