from django import forms
from .models import Client, Immobile, RegisterLocation


## Cadastra Cliente    
class ClientForm(forms.ModelForm):
    # Define as configurações do modelo e dos campos do formulário.
    class Meta:
        # Especifica o modelo com o qual o formulário está associado.
        model = Client
        # Define que todos os campos do modelo devem ser incluídos no formulário.
        fields = '__all__'
        
    # Define um método de inicialização para o formulário.
    def __init__(self, *args, **kwargs): # Adiciona 
        # Chama o método de inicialização da superclasse para inicializar o formulário.
        super().__init__(*args, **kwargs)  
        
        # Itera sobre os campos do formulário.
        for field_name, field in self.fields.items():   
            # Adiciona a classe CSS 'form-control' a todos os widgets de campo.
            field.widget.attrs['class'] = 'form-control'




##Permite que seja feito upload de multiplos arquivos para ImmobileForm
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


## Cadastra um Imovel
class ImmobileForm(forms.ModelForm):
    # Define um campo de arquivo múltiplo para permitir que vários arquivos sejam selecionados.
    immobile = MultipleFileField(label='Select files', required=False)

    # Define as configurações do modelo e dos campos do formulário.
    class Meta:
        # Especifica o modelo com o qual o formulário está associado.
        model = Immobile
        # Define que todos os campos do modelo devem ser incluídos no formulário.
        fields = '__all__'
        # Exclui o campo 'is_locate' do formulário.
        exclude = ('is_locate',)

    # Define um método de inicialização para o formulário.
    def __init__(self, *args, **kwargs): # Adiciona 
        # Chama o método de inicialização da superclasse para inicializar o formulário.
        super().__init__(*args, **kwargs)  
        
        # Itera sobre os campos do formulário.
        for field_name, field in self.fields.items():   
            # Verifica se o widget do campo é uma caixa de seleção ou uma seleção de rádio.
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                # Adiciona a classe CSS 'form-check-input' se o widget for uma caixa de seleção ou uma seleção de rádio.
                field.widget.attrs['class'] = 'form-check-input'
            else:
                # Adiciona a classe CSS 'form-control' para outros tipos de widgets de campo.
                field.widget.attrs['class'] = 'form-control'


## Registra Locação do Imovel    
class RegisterLocationForm(forms.ModelForm):
    # Define um campo de data/hora para a data de início da locação.
    dt_start = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date',}))
    # Define um campo de data/hora para a data de término da locação.
    dt_end = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date',}))

    # Define as configurações do modelo e dos campos do formulário.
    class Meta:
        # Especifica o modelo com o qual o formulário está associado.
        model = RegisterLocation
        # Define que todos os campos do modelo devem ser incluídos no formulário.
        fields = '__all__'
        # Exclui os campos 'immobile' e 'create_at' do formulário.
        exclude = ('immobile', 'create_at',)

    # Define um método de inicialização para o formulário.
    def __init__(self, *args, **kwargs): # Adiciona 
        # Chama o método de inicialização da superclasse para inicializar o formulário.
        super().__init__(*args, **kwargs)  
        
        # Itera sobre os campos do formulário.
        for field_name, field in self.fields.items():   
            # Adiciona a classe CSS 'form-control' a todos os widgets de campo.
            field.widget.attrs['class'] = 'form-control'
