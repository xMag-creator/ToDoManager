from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=256)
    finished = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ZeroLevel(Base):
    pass


class FirstLevel(Base):
    zeroLevel = models.ForeignKey(ZeroLevel, on_delete=models.CASCADE)


class SecondLevel(Base):
    firstLevel = models.ForeignKey(FirstLevel, on_delete=models.CASCADE)


class ThirdLevel(Base):
    secondLevel = models.ForeignKey(SecondLevel, on_delete=models.CASCADE)


class FourthLevel(Base):
    thirdLevel = models.ForeignKey(ThirdLevel, on_delete=models.CASCADE)


class FifthLevel(Base):
    fourthLevel = models.ForeignKey(FourthLevel, on_delete=models.CASCADE)
