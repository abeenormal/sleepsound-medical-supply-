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
  def __init__(self,id_name,description,image,button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = id_name
    self.description_label.content = description
    self.image_content.source = image
    self.button_callback = button_callback
   
        # Any code you write here will run before the form opens.

  
 