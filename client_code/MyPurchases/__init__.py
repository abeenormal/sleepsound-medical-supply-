from ._anvil_designer import MyPurchasesTemplate
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
from ..Products import Products



class MyPurchases(MyPurchasesTemplate):
  def __init__(self, **properties):
   
  
      
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.load_products()
  

    # Any code you write here will run before the form opens.

  def render_products(self, id_name):
    self.content_panel.clear()
    

  

  def load_products(self):
    products = anvil.server.call("get_user_products")

    if products is not None and len(products)> 0: 
      self.no_purchases_label.visible = False

      products_panel = GridPanel()
       
      for i, product in enumerate(products):
        c = Products(name=product["name"], button_text="Back", description=product["description"], image=product["image"], button_callback=self.render_products,)
        products_panel.add_component(c, row=str(i//3), width_xs=4)
      
      self.content_panel.add_component(products_panel)
    

   

    
