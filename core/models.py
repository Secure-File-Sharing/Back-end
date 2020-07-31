from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.


class Account(User):
    CONF_LABEL = (
        (1, "TopSecret"),
        (2, "Secret"),
        (3, "Confidential"),
        (4, "Unclassified")
    )
    INTEGRITY_LABEL = (
        (1, "VeryTrusted"),
        (2, "Trusted"),
        (3, "SlightlyTrusted"),
        (4, "Untrusted")
    )
    confidentiality_label = models.IntegerField(blank=False, choices=CONF_LABEL)
    integrity_label = models.IntegerField(blank=False, choices=INTEGRITY_LABEL)


class TokenAuth(Token):
    """
    Extend last_use parameter for checking expire token.
    """
    last_use = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key

class File(models.Model):
    CONF_LABEL = (
        (1, "TopSecret"),
        (2, "Secret"),
        (3, "Confidential"),
        (4, "Unclassified")
    )
    INTEGRITY_LABEL = (
        (1, "VeryTrusted"),
        (2, "Trusted"),
        (3, "SlightlyTrusted"),
        (4, "Untrusted")
    )
    file_name = models.CharField(max_length=32)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    data_file = models.FileField()
    confidentiality_label = models.IntegerField(blank=False, choices=CONF_LABEL)
    integrity_label = models.IntegerField(blank=False, choices=INTEGRITY_LABEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
