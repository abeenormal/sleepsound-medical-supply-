from ._anvil_designer import BaseTemplate
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
from ..Home import Home
from ..About import About
from ..MyPurchases import MyPurchases
from .urls import urls
from ..Footer import Footer


class Base(BaseTemplate):
  def __init__(self, **properties):
 
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.change_sign_in_text()
    self.handle_urls()
    

    # Any code you write here will run before the form opens.
    self.background = 'url("_/theme/clouds.png")'
   
    
  def handle_urls(self):
    url = get_url_hash().lower()

    if url in urls:
      self.content_panel.clear()
      self.content_panel.add_component(urls[url]())
    else:
      self.go_to_home()
 
  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.sign_in.text = email
    else:
      self.sign_in.text = "Sign In" 

    self.toggle_my_purchases_link()

  def toggle_my_purchases_link(self):
    self.my_purchases.visible = anvil.users.get_user() is not None

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_home()

  def my_purchases_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MyPurchases())

  def go_to_home(self): 
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def sign_in_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
      logout = confirm ("Would you like to logout?")
      if logout:
        anvil.users.logout()
        self.go_to_home()
    else:
      anvil.users.login_with_form()
    self.change_sign_in_text()
   

  def about_us_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(About())

       self.refresh_data_bindings()