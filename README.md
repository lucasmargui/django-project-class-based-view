<H1 align="center">Crud structure using Class-based views</H1>
<p align="center">🚀 Project to create a crud structure using Django's Class-based views for future references</p>

# Project
This project uses Django_Projeto_AluguelCarros as a base, modifying the views to use class-based views.

## Resources Used

* Django 5.0.2
* Python 3.10



<div align="center">
  <h2> Property List </h2>
  <img src="https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/f13bc223-0a25-4055-a009-3ffecc040ca7" style="width:100%">
   <h2> Reports List </h2>
  <img src="https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/285aa3d7-b7d1-4065-a928-5f1d2fd6d0f6" style="width:100%">
   <h2> Customer base </h2>
  <img src="https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/fd4dee1f-9738-4406-963c-29cee9e9655c" style="width:100%">
   <h2> Property Registration </h2>
  <img src="https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/a4722f64-2b6b-4d6b-8568-aa8e2045c1cb" style="width:100%">
   <h2>  Rental Registration </h2>
  <img src="https://github.com/lucasmargui/Django_Projeto_AluguelImovel/assets/157809964/b77195b3-8ee3-430b-8566-e879843a7aa2" style="width:100%">


  
</div>




## Views

<details>
 <summary>Click to show content</summary>

Where the classes will be created using a model to retrieve the data or using a form to create the forms.


Using model Immobile to retrieve the data, passing the context object name that will be used to access this data on the list-location html page.
```
class ImmobileList(ListView):
 model = Immobile
 context_object_name = 'immobiles'
 template_name = 'list-location.html'
 ```

Using model Client to create a custom Form that will be incorporated into form_class.
```
class ClientForm(forms.ModelForm):
 class Meta:
 model = Client
 fields = '__all__'
 def __init__(self, *args, **kwargs): # Add
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

</details>


