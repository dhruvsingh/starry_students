# -*- coding: utf-8 -*-
from django.db import models

from django.utils import timezone


class BaseModel(models.Model):
    """Django base model for use as parent model."""

    created_at = models.DateTimeField(
        editable=False,
        help_text='The time this object was created.'
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The time this object was updated.'
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        """Meta for BaseModel."""

        abstract = True

    def clean(self, *args, **kwargs):
        """Override clean method for custom validation/cleaning of fields."""
        super(BaseModel, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        """Override save method for custom validation/cleaning of fields."""
        # if deleting an object (we soft delete, so its essentially a save)
        # do not validate them, just save
        if not kwargs.get('no_validate', False):
            self.full_clean()
        else:
            kwargs.pop('no_validate')

        # update created
        if not self.id:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()

        super(BaseModel, self).save(*args, **kwargs)

    def __repr__(self):
        """repr() for class object."""
        raise NotImplementedError(
            "Necessary to implement __repr__ to improve "
            "readability across the codebase."
        )

    def __str__(self):
        """str() for class object."""
        raise NotImplementedError(
            "Necessary to implement __str__ to improve "
            "readability across the codebase."
        )


class Student(BaseModel):
    """Hold student information.

    Should be related to user, as One2One Field, but for now its as is.
    """

    name = models.CharField(
        max_length=64,
    )

    class Meta:
        """Meta for Student model."""

        ordering = ('-created_at',)

    def __repr__(self):
        """repr() for Student."""
        return f'<Student: {self.id} - {self.name}>'

    __str__ = __repr__
