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
  def __init__(self,name,button_text,description,image,button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = name
    self.button.text = button_text
    self.description_label.content = description
    self.image_content.source = image
    self.button_callback = button_callback
   
        # Any code you write here will run before the form opens.

  
  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_callback(self.name_label.content.lower())






