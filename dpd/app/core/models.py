from django.db import models

class Session(models.Model):
    ses_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return '%d' % (self.ses_id)
    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'

class TargetCords(models.Model):
    lapt = models.FloatField()
    long = models.FloatField()
    ses_id = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return '%f %f' % (self.lapt, self.long)
    class Meta:
        verbose_name = 'TargetCord'
        verbose_name_plural = 'TargetCords'

class ZoneCords(models.Model):
    lapt = models.FloatField()
    long = models.FloatField()
    ses_id = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return '%f %f' % (self.lapt, self.long)
    class Meta:
        verbose_name = 'ZoneCord'
        verbose_name_plural = 'ZoneCords'

class UserCords(models.Model):
    lapt = models.FloatField()
    long = models.FloatField()
    ses_id = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return '%f %f' % (self.lapt, self.long)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

