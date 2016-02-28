from __future__ import unicode_literals

from django.db import models


class Record(models.Model):
    """
    Provides a record model.
    """

    #: Defines the key field of the record.
    key = models.CharField(max_length=64, unique=True, db_index=True)

    #: Defines the key field of the record.
    value = models.CharField(max_length=255, db_index=True)

    def __unicode__(self):
        """
        Provides the unicode representation of the record instance.

        :return: The unicode representation of the record instance.
        """
        return "<Record {} {}>".format(self.key, self.value)

