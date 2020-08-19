from django.db import models

# Create your models here.

insurance_type = (('Motor', 'Motor'),
                  ('Health', 'Health'),
                  ('Travel', 'Travel'),)


class data_policy(models.Model):
    policy_auto_id = models.AutoField(primary_key=True)
    policy_no = models.BigIntegerField(verbose_name='Policy No')
    policy_cname = models.CharField(max_length=200, verbose_name='Customer Name')
    policy_type = models.CharField(max_length=20, choices=insurance_type, verbose_name='Policy Type')
    policy_start = models.DateField(verbose_name='Policy Start Date')
    policy_expire = models.DateField(verbose_name='Policy End Date')
    policy_amt = models.FloatField(verbose_name='Policy Amount')
    policy_status = models.BooleanField(default=True, verbose_name='Policy Status')

    def __str__(self):
        return str(self.policy_no)

    class Meta:
        verbose_name = 'Policy List'
