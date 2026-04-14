"""Fields for Zinnia admin"""
from django import forms
from django.utils.encoding import smart_str


class MPTTModelChoiceIterator(forms.models.ModelChoiceIterator):
    """
    MPTT version of ModelChoiceIterator.
    """

    def choice(self, obj):
        """
        Overloads the choice method to add the position
        of the object in the tree for future sorting.
        """
        tree_id = getattr(obj, self.queryset.model._mptt_meta.tree_id_attr, 0)
        left = getattr(obj, self.queryset.model._mptt_meta.left_attr, 0)
        return super(MPTTModelChoiceIterator,
                     self).choice(obj) + ((tree_id, left),)


class MPTTModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    """
    MPTT version of ModelMultipleChoiceField.
    """

    def __init__(self, level_indicator='|--', *args, **kwargs):
        self.level_indicator = level_indicator
        super(MPTTModelMultipleChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        """
        Create labels which represent the tree level of each node
        when generating option labels.
        """
        label = smart_str(obj)
        prefix = self.level_indicator * getattr(obj, obj._mptt_meta.level_attr)
        if prefix:
            return '%s %s' % (prefix, label)
        return label

    @property
    def choices(self):
        """
        Override choices getter to use MPTTModelChoiceIterator.
        """
        return MPTTModelChoiceIterator(self)

    @choices.setter
    def choices(self, value):
        self._choices = self.widget.choices = list(value)
