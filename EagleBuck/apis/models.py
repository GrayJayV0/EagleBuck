from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    eaglebucks = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return [
            f'Username: {self.username}\n',
            f'Password: {self.password}\n',
            f'Eagle Bucks: {self.eaglebucks}\n',
        ]
    
class Game(models.Model):
    name = models.CharField(max_length=20)
    users = models.CharField(max_length=20)

    def __str__(self):
        return [
            f'Game Name: {self.name}\n',
            f'Username: {self.users}\n',
        ]