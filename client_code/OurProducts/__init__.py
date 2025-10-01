from ._anvil_designer import OurProductsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Checkout import Checkout


class OurProducts(OurProductsTemplate):
  def __init__(self, **properties):

    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_products()
    # Any code you write here will run before the form opens.
    
  def back(self):
    self.content_panel.clear()
    self.load_products()

  def load_products(self):
    products = anvil.server.call ("get_all_products").search()
    products_panel = GridPanel()

    for i, product in enumerate(products):
      c = products(name=products["product_name"], button_text=f"Purchase for ${products['price']}", description=products["description"], image=products["image"], button_callback=self.render_checkout)
      products_panel.add_component(c, row=str(i//2), width_xs=6)

    self.content_panel.add_component(products_panel)

