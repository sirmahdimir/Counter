from django.db import models


class Digit(models.Model):
    num = models.IntegerField(default=0)

    def decreasment(self):
        self.num -= 1
        self.save()

    def reset(self):
        self.num = 0
        self.save()

    def increasment(self):
        self.num += 1
        self.save()

    def __str__(self):
        return f'Digit Is : {self.num}'
        
