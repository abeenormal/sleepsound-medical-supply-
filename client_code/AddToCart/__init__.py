from ._anvil_designer import AddToCartTemplate
from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Checkout import Checkout
from ..Products import Products
from ..MyCart import MyCart




class AddToCart(AddToCartTemplate):
  def __init__(self, id_name, description, image, button, **properties):
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_form(id_name)
    # Any code you write here will run before the form opens.
 
  
  def update_form(self, id_name):
    product = anvil.server.call("get_product_details", id_name)
    self.products = product
    self.name_label.content = product["name"]
    self.description_label.content = product["description"]
    self.price_label.text = f"${product['price']} USD"
    self.image_content.source = product["image"]

  def render_cart(self,id_name):
    self.content_panel.clear()  

  def load_cart(self):
    MyCart = anvil.server.call('get_user_products')


  def back_button_click(self, **event_args):
        """This method is called when the button is clicked"""


  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    if user["cart_items"] and self.products["id_name"] in user["cart_items"]:
      #display the items in Cart
      for i, product in enumerate(products):
        c = Products(id_name=product["name"], price=f"Purchase for ${product['price']}", quantity=product['quantity'], description=product["description"], image=product["image"], add_cart_button=['add_cart_button'],)
        products_panel.add_component(c, row=str(i//3), width_xs=4)

      self.content_panel.add_component(cart_panel)  
   
   
  

  

  
  

