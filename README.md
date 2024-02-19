<H1 align="center">Estrutura de Crud utilizando Class-based views</H1>
<p align="center">🚀 Projeto de criação de uma estrutura de crud utilizando Class-based views do Django para referências futuras</p>

## Recursos Utilizados

* Django 5.0.2
* Python 3.10

## Views
Onde será criado as classes utilizando um model para recuperar os dados ou utilizando um form para criação dos formulários.


Utilizando model Immobile para recuperar os dados, passando o context object name que será usado parar acessar estes dados na pagina html list-location.
```
class ImmobileList(ListView):  
    model = Immobile  
    context_object_name = 'immobiles'  
    template_name = 'list-location.html'
 ```

Utilizando model Client para criação de um Formulário personalizado que será incorporado em form_class.
```
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
```

```
class ClientCreate(CreateView):

    form_class = ClientForm
    template_name = 'form-client.html'
    success_url = reverse_lazy('list-location')
    def form_valid(self, form):
        return super(ClientCreate, self).form_valid(form)
```



# Resultado

## Lista Imóveis
![image](https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/f13bc223-0a25-4055-a009-3ffecc040ca7)

## Lista Reports
![image](https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/285aa3d7-b7d1-4065-a928-5f1d2fd6d0f6)

## Cadastro de Clientes
![image](https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/fd4dee1f-9738-4406-963c-29cee9e9655c)

## Cadastro de Imóvel
![image](https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/a4722f64-2b6b-4d6b-8568-aa8e2045c1cb)

## Cadastro de Locação
![image](https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/b77195b3-8ee3-430b-8566-e879843a7aa2)






