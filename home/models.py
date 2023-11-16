from django.db import models

RATINGS = ((1, "Excellent"), (2, "Good"),
           (3, "Meh"), (4, "Bad"), (5, "Budweiser"))


class Distillery(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "Distilleries"

    def __str__(self):
        return self.name


class Whiskey(models.Model):
    name = models.CharField(max_length=200, unique=True)
    distillery = models.ForeignKey(
        Distillery, on_delete=models.CASCADE, related_name="whiskey_distillery")
    rating = models.IntegerField(choices=RATINGS, default=3)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = "Whiskies"

    def __str__(self):
        return f"Whiskey: {self.name} from {self.distillery}"
