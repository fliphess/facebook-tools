form = """
<head>
  <meta charset="utf-8">
  <title>Facebook even attendees</title>
  <link href="bootstrap.min.css" rel="stylesheet">
</head>
<body>
<link rel="icon" href="favicon.ico" type="image/x-icon"/>
<div class="container">
  <div class="row row-offcanvas row-offcanvas-right">
    <div class="col-xs-12 col-sm-9">
      <div class="jumbotron">
        <h1>Attendee lister</h1>
        <p>Print a quick overview of all attending of a facebook event.</p>
      </div>
      <div class="row">
        <div class="row row-offcanvas row-offcanvas-right">
          <center>
            <h2>Enter event ID</h2>
            <form method="get" action="next.cgi">
              <input type="text" name="event">
              <button type="submit" class="btn btn-default">Go</button>
            </form>
            <p>If you receive an error, you forgot to invite Flip to the event :)</p>
          </center>

        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

header = """
<head>
  <meta charset="utf-8">
  <title>Facebook even attendees</title>
  <link href="bootstrap.min.css" rel="stylesheet">
</head>
<body>
<link rel="icon" href="favicon.ico" type="image/x-icon"/>
<div class="container">
  <h1>Facebook Attendees</h1>
  <ol class="breadcrumb">
    <li><a target="_blank" href="https://www.facebook.com/events/%s">Event</a></li>
    <li>Total attendees: %s</li>
    <li><a href="index.cgi">Back</a></li>
  </ol>
  <table class="table table-striped">"""

table = """
<tr>
  <td>%s</td>
</tr>"""

footer = """</table>
</div>
</body>
</html>"""
