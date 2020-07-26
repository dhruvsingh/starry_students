# -*- coding: utf-8 -*-
from dateutil import relativedelta
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


class Teacher(BaseModel):
    """Hold teacher information.

    Should be related to user, as One2One Field, but for now its as is.
    """

    name = models.CharField(
        max_length=64,
    )
    students = models.ManyToManyField(
        Student,
        through="TeacherStudent",
        related_name="teachers",
        blank=True,  # needed in order to make it optional
    )

    class Meta:
        """Meta for Teacher model."""

        ordering = ('-created_at',)

    def __repr__(self):
        """repr() for Teacher."""
        return f'<Teacher: {self.id} - {self.name}>'

    __str__ = __repr__


class TeacherStudent(models.Model):
    """
    Hold information about teachers and students.

    Also holds information about STAR students.
    """

    student = models.ForeignKey(Student, models.CASCADE)
    teacher = models.ForeignKey(Teacher, models.CASCADE)
    # a boolean for now, can be an integer field to store student rating
    starred_student = models.BooleanField(default=False)

    class Meta:
        """Meta for TeacherStudent."""

        unique_together = ("teacher", "student")

    def __repr__(self):
        """repr() for TeacherStudent."""
        return f'<Teacher - Student: {self.teacher.id} - {self.student.id}>'

    __str__ = __repr__
