from django.shortcuts import render, redirect

from django.db.models import Q

from .forms import ClientForm, ImmobileForm, RegisterLocationForm
from .models import Immobile, ImmobileImage
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,FormView
from django.urls import reverse_lazy



class ImmobileList(ListView):  
    # Define o modelo a ser utilizado para recuperar os dados.
    model = Immobile  

    # Define o nome do contexto a ser passado para o template.
    context_object_name = 'immobiles'  

    # Define o nome do template a ser utilizado para renderizar a página.
    template_name = 'list-location.html' 


class ImmobileCreate(CreateView):

    template_name = 'form-immobile.html'
    success_url = reverse_lazy('list-location')
     # Define a classe do formulário a ser usada para criar o Imóvel.
    form_class = ImmobileForm
    def form_valid(self, form):
        # Salva o objeto Immobile e obtém a instância salva
        immobile_instance = form.save()

        # Obtém a lista de arquivos enviados no formulário
        files = self.request.FILES.getlist('immobile')

        if files:
            # Para cada arquivo na lista, cria uma instância de ImmobileImage
            for f in files:
                # Salva a instância de ImmobileImage associada ao objeto Immobile
                ImmobileImage.objects.create(immobile=immobile_instance, image=f)

                # Esta é uma operação segura. Se "immobile_instance" ainda não estiver salvo no banco de dados,
                # ela será salva automaticamente quando o método "form_valid" for concluído.

        # Chama o método form_valid da superclasse para continuar o processamento do formulário
        return super(ImmobileCreate, self).form_valid(form)



class ClientCreate(CreateView):

    form_class = ClientForm
    template_name = 'form-client.html'
    success_url = reverse_lazy('list-location')

    # Define um método para tratar o formulário quando ele é válido.
    def form_valid(self, form):
        # Chama o método form_valid da superclasse CreateView para realizar as operações padrão de validação.
        return super(ClientCreate, self).form_valid(form)



class LocationCreate(FormView):  

    template_name = 'form-location.html'  
    form_class = RegisterLocationForm  

    # Define um método para obter o contexto da view.
    def get_context_data(self, **kwargs):  
        # Obtém o contexto da superclasse.
        context = super().get_context_data(**kwargs)  

        # Obtém o objeto Immobile com base no ID fornecido na URL.
        get_locate = Immobile.objects.get(id=self.kwargs['id'])  

        # Adiciona o objeto Immobile ao contexto com a chave 'location'.
        context['location'] = get_locate  

        # Retorna o contexto atualizado.
        return context  

    # Define um método para tratar o formulário quando ele é válido.
    def form_valid(self, form):  
        # Obtém o objeto Immobile com base no ID fornecido na URL.
        get_locate = Immobile.objects.get(id=self.kwargs['id'])  

        # Salva o formulário, associando-o ao objeto Immobile.
        location_form = form.save(commit=False)  
        location_form.immobile = get_locate  
        location_form.save()  

        # Atualiza o status de localização do Immobile para True.
        immo = Immobile.objects.get(id=self.kwargs['id'])  
        immo.is_locate = True  
        immo.save()  

        # Redireciona para a página 'list-location'.
        return redirect('list-location')  

    # Define um método para tratar o formulário quando ele é inválido.
    def form_invalid(self, form):  
        # Renderiza a resposta com o contexto atual e o formulário inválido.
        return self.render_to_response(self.get_context_data(form=form))  


class ReportsList(ListView):  
    template_name = 'reports.html'  
    context_object_name = 'immobiles'  
    model = Immobile  

    # Define um método para obter o conjunto de consultas (queryset).
    def get_queryset(self):  
        # Obtém todos os objetos Immobile do banco de dados.
        immobiles = Immobile.objects.all()  

        # Obtém os parâmetros da consulta da solicitação GET.
        get_client = self.request.GET.get('client')  
        get_locate = self.request.GET.get('is_locate')  
        get_type_item = self.request.GET.get('type_item')  
        get_dt_start = self.request.GET.get('dt_start')  
        get_dt_end = self.request.GET.get('dt_end')  

        # Filtra os objetos Immobile com base nos parâmetros da consulta.
        if get_client:  
            immobiles = immobiles.filter(
                Q(reg_location__client__name__icontains=get_client) | 
                Q(reg_location__client__email__icontains=get_client)
            )  

        if get_dt_start and get_dt_end:  
            immobiles = immobiles.filter(
                reg_location__create_at__range=[get_dt_start, get_dt_end]
            )  

        if get_locate is not None:  
            immobiles = immobiles.filter(is_locate=get_locate)  

        if get_type_item:  
            immobiles = immobiles.filter(type_item=get_type_item)  

        # Retorna o queryset filtrado.
        return immobiles  