from django.db import models


class CommonInfo(models.Model):
    class Meta:
        abstract = True


class Owner(models.Model):
    class Meta(CommonInfo.Meta):
        db_table = "Owner"

    name = models.CharField(max_length=50)


class Raspy(models.Model):
    class Meta(CommonInfo.Meta):
        db_table = "Raspy"

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column="ownerId")
    name = models.CharField(max_length=50)


class Sensor(models.Model):
    class Meta(CommonInfo.Meta):
        db_table = "Sensor"

    raspy = models.ForeignKey(Raspy, on_delete=models.CASCADE, db_column="raspyId")
    name = models.CharField(max_length=50)
    isAvailable = models.BooleanField(default=True)
    unit = models.CharField(max_length=20)
    highestPossible = models.FloatField()
    lowestPossible = models.FloatField()


class DataEntry(models.Model):
    class Meta(CommonInfo.Meta):
        db_table = "DataEntry"

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, db_column="sensorId")
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
