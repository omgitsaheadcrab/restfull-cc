# WARNING
# This script will create a new empty db or drop_all from current db.

from restful_cc import app
app.app_context().push()

from restful_cc import db
db.drop_all()
db.create_all()

print "Done"
