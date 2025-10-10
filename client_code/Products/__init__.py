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
from ..Checkout import Checkout



class Products(ProductsTemplate):
  def __init__(self,name,button_text,description,image, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = name
    self.add_button.text = button_text
    self.description_label.content = description
    self.image_content.source = image
   
    

    # Any code you write here will run before the form opens.

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(content=AddToCart(item=self.item))

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.add_component(ProductsTemplate)
    





