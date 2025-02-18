from django.db import models


class Et(models.Model):

    exp_name = models.CharField(max_length=20, blank=True, null=True)
    exp_category = models.CharField(max_length=20, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'et'
