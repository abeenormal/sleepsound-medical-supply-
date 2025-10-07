import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import routes

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
@anvil.server.route('/sitemap.txt')
def get_sitemap():
 # putting these in here so we don't import these all the time
  from rounting.router._route import sorted_routes
  import anvil.server
  import anvil.media

 # Grab the app origin url
  origin - anvil.server.get_app_origin()

  sitemap = [origin]

  # Go through each of the fefined routes
  for route in sorted_routes:
      # We can maskroutes when defining them by adding a private = True attribute
    if not getattr(route, "private", False):
      sitemap.append(f"{origin}{route.path}")

  # Compile the routes, one per line
  file_contents = "\m".join(sitemap).encode()
  file = anvil.BlobMedia(content_type="text/plain", content=file_contents, name="sitemap.text")

  #serve up our up-to-date sitemap.
  return anvil.server.HttpResponse(200, file)

  
    