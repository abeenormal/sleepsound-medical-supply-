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
from .Cart import Cart





class Products(ProductsTemplate):
  def __init__(self,id_name,description,image,add_cart_button,price, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = id_name
    self.description_label.content = description
    self.image_content.source = image
    self.add_cart_button
    self.price_label.text = price
    # Any code you write here will run before the form opens.
   
   


  def add_cart_button_click(self, id_name='id_name', **event_args):
    anvil.server.call('add_item_to_session_cart', 'id_name',)
  

    








