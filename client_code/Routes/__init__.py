from ._anvil_designer import RoutesTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from routing.router import Route


class IndexRoute(Route):
  path = "/"
  form = "Pages.Home"

  class AboutRoute (Route):
    path = "/about"
    form = "Pages.About"

  class OurProductsRoute(Route):
    path = "/ourproducts"
    form = "Pages.OurProducts"

  class MyProducts(Route):
    path = "/myproducts"
    form = "Pages.MyProducts"

    class PrivateRoute(Route):
      path = "/private"
      form = "Pages.Private"
      private = False
    