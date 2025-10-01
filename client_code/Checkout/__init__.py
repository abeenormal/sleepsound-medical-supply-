from ._anvil_designer import CheckoutTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Checkout(CheckoutTemplate):
  def __init__(self, id_name, back_button_callback, **properties):
    self.back_button_callback = back_button_callback
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_form(id_name)
    # Any code you write here will run before the form opens.

  def update_form(self, id_name):
    product = anvil.server.call('get_product_details', id_name)
    self.name_label.content = product["name"]
    self.description_label.text = product['description']
    self.price_label.text = f"${product['price']} USD"
    self.image_content.source = product['image']

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()

  