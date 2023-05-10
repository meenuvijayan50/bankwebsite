from django import forms

from bankapp.models import District, User, Branches


# creating a form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['branches'].queryset = User.objects.none()
        #
            if 'District' in self.data:
                try:
                    District_id = int(self.data.get('District'))
                    self.fields['Branches'].queryset =Branches.objects.filter( District_id=District_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['Branches'].queryset = self.instance.District.branches_set.order_by('name')
