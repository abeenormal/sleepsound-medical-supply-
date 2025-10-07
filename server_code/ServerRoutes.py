import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import route

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
@anvil.server.route('/sitemap.txt')
