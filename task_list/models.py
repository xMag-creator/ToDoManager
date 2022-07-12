from django.db import models

# Create your models here.


class BaseLevel(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    finished = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ZeroLevel(BaseLevel):
    pass


class FirstLevel(BaseLevel):
    zeroLevel = models.ForeignKey(ZeroLevel, on_delete=models.CASCADE)


class SecondLevel(BaseLevel):
    zeroLevel = models.ForeignKey(FirstLevel, on_delete=models.CASCADE)


class ThirdLevel(BaseLevel):
    zeroLevel = models.ForeignKey(SecondLevel, on_delete=models.CASCADE)


class FourthLevel(BaseLevel):
    zeroLevel = models.ForeignKey(ThirdLevel, on_delete=models.CASCADE)


class FifthLevel(BaseLevel):
    zeroLevel = models.ForeignKey(FourthLevel, on_delete=models.CASCADE)
