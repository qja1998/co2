from django import forms
from .models import Parameters, TrainedData

class ParametersForm(forms.ModelForm):
    class Meta:
        model = Parameters
        fields = ['model_name', 'seq_len', 'hidden_num', 'layer_num', 'epochs', 'lr']

class TrainedForm(forms.ModelForm):
    class Meta:
        model = TrainedData
        fields = ['model_path', 'loss', 'img_path']