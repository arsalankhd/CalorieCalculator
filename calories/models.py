from django.db import models
from accounts.models import CustomUser

class foodItem(models.Model):
    name = models.CharField(max_length=200 ,null=False)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    person_of = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str('{name} ({c} کالری)'.format(name=self.name, c=self.calorie))

class foodConsumed(models.Model):
    options = (
        ('صبحانه', 'صبحانه'),
        ('نهار', 'نهار'),
        ('شام', 'شام'),
    )

    name = models.ForeignKey(foodItem, on_delete=models.CASCADE)
    person_of = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False,default=1)
    option = models.CharField(max_length=50, choices=options)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str('{name} {op}'.format(name=self.name, op=self.options))