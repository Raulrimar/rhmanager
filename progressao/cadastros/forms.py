from django import forms
from .models import Servidor

class ServidorForm(forms.ModelForm):
    inicioferias = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Início Férias"
    )
    terminoferias = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Término Férias"
    )
    origem = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'})
    )
    cancelamentos = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'})
    )

    class Meta:
        model = Servidor
        fields = '__all__'
        widgets = {
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(ServidorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ != 'CheckboxInput' and field_name not in ['observacao', 'origem', 'cancelamentos']:
                field.widget.attrs['class'] = 'form-control'

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        if matricula and Servidor.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError("Esta matrícula já está cadastrada.")
        return matricula
