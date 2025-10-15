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
  def __init__(self,id_name,description,image,button_callback,price,quantity, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = id_name
    self.description_label.content = description
    self.image_content.source = image
    self.button_callback = button_callback
    self.price_label.text = price
    self.quantity_label.text = quantity
        # Any code you write here will run before the form opens.

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_produ
    
    self.add_to_cart(self.item())

  def add_to_cart(self, product, quantity):
    #if item is already in cart, just update the quantity
    self.cart_itmes.append({'product': product, 'quantity': quantity - 1 })

    self.content_panel= GridPanel()

  
 