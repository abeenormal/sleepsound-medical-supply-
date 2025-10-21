from ._anvil_designer import ProductsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Products(ProductsTemplate):
  def __init__(self,id_name,button_text, description,image, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)    
    self.name_label.content = id_name
    self.description_label.content = description
    self.image_content.source = image
    self.button.text = button_text
    # Any code you write here will run before the form opens.

    
  def button_click(self,  **event_args):
    """This method is called when the button is clicked""" 
    anvil.server.call(get_session_cart_items)
    cart_items = anvil.server.call("add_item_to_session_cart_items")