from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry

        fields = [
            'full_name',
            'mobile',
            'email',
            'service_number',
            'rank',
            'category',
            'subject',
            'message',
            'document',
        ]

        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_class = """
        w-full rounded-xl border border-slate-300
        bg-white px-4 py-3
        text-slate-700 shadow-sm
        transition-all duration-300
        focus:border-blue-600
        focus:ring-4 focus:ring-blue-100
        focus:outline-none
        """

        file_class = """
        w-full rounded-xl border
        border-dashed border-slate-300
        bg-slate-50 px-4 py-3
        """

        for field in self.fields.values():

            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = file_class
            else:
                field.widget.attrs['class'] = input_class
                field.widget.attrs['placeholder'] = field.label