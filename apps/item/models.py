from __future__ import unicode_literals

from ..login_reg.models import User
from django.db import models

class ItemManager(models.Manager):
    def creator(self, postdata, user_id):
        item = self.create(
            title=postdata,
            users=User.objects.get(id=user_id)
            )
        
        userObject = User.objects.get(id=user_id)
        item.wished_by.add(userObject)
        return item

    def validate(self, postdata):
        result={'status':True, 'errors':[]}
        if len(postdata['item'])<3:
            result['errors'].append('Item name is too short')
            result['status']=False
    
    def add_to_wishlist(self, user_id, item_id):
        item = Item.objects.get(id=item_id)
        user = User.objects.get(id=user_id)
        
        item.wished_by.add(user)

    def remove_from_wishlist(self, user_id, item_id):
        item = Item.objects.get(id=item_id)
        user = User.objects.get(id=user_id)
        
        item.wished_by.remove(user)
    def show_item(self,user_id,item_id):
        pass

    def delete(self,item_id):
        pass

class Item(models.Model):
    title = models.CharField(max_length=255)
    users=models.ForeignKey(User, related_name="added_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wished_by = models.ManyToManyField(User, related_name="wishing_for")
    objects = ItemManager()
    


