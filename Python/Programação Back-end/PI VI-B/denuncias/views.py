from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import Denuncia
from .forms import DenunciaForm


class DenunciarView(LoginRequiredMixin, CreateView):
    model = Denuncia
    form_class = DenunciaForm
    template_name = 'denuncias/pages/denunciar.html'
    success_url = reverse_lazy('denuncias:todos_os_casos')

    def form_valid(self, form):
        denuncia = form.save(commit=False)
        denuncia.denunciante = self.request.user if not form.cleaned_data['anonimo'] else None
        denuncia.save()
        return super().form_valid(form)

class CasosDetailView(LoginRequiredMixin, DetailView):
    model = Denuncia
    template_name = 'denuncias/pages/casos_detail.html'

    def post(self, request, *args, **kwargs):
        caso = self.get_object()
        user_groups = request.user.groups.values_list('name', flat=True)

        if "comentario" in request.POST:
            conteudo = request.POST.get("comentario")
            if conteudo:
                autor = "Anônimo" if caso.anonimo and caso.denunciante == request.user else request.user.username
                caso.adicionar_comentario(autor, conteudo)

        if "status" in request.POST and "Agentes" in user_groups:
            novo_status = request.POST.get("status")
            if novo_status in ["Aberto", "Em Tratamento", "Fechado"]:
                caso.status = novo_status
                caso.save()

        if "grupo" in request.POST and "Coordenadores" in user_groups:
            novo_grupo = request.POST.get("grupo")
            caso.grupo = novo_grupo
            caso.save()

        if "agente_si" in request.POST and "Coordenadores" in user_groups:
            agente_si_id = request.POST.get("agente_si")
            if agente_si_id:
                try:
                    agente_si = User.objects.get(id=agente_si_id, groups__name="Agentes")
                    caso.agente_si = agente_si
                    caso.save()
                except User.DoesNotExist:
                    pass

        return redirect('denuncias:denuncia_detail', pk=caso.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_groups = self.request.user.groups.values_list('name', flat=True)
        context['is_coordinator'] = "Coordenadores" in user_groups
        context['is_agent'] = "Agentes" in user_groups
        context['is_user'] = "Agentes" in user_groups
        
        if "Coordenadores" in user_groups:
            from django.contrib.auth.models import User
            context['agentes_si'] = User.objects.filter(groups__name="Agentes")
        
        return context

class TodosOsCasosView(LoginRequiredMixin, ListView):
    model = Denuncia
    template_name = 'denuncias/pages/todos_os_casos.html'

    def get_queryset(self):
        return Denuncia.objects.filter(denunciante_id=self.request.user.id, status__in=["Aberto", "Em Tratamento"])

class CasosEmAbertoView(LoginRequiredMixin, ListView):
    model = Denuncia
    template_name = 'denuncias/pages/casos_em_aberto.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name="Coordenadores").exists():
            return Denuncia.objects.filter(status__in=["Aberto", "Em Tratamento"])
        elif self.request.user.groups.filter(name="Agentes").exists():
            return Denuncia.objects.filter(status__in=["Aberto", "Em Tratamento"], agente_si=self.request.user)

        return Denuncia.objects.none()

class CasosFechadosView(LoginRequiredMixin, ListView):
    model = Denuncia
    template_name = 'denuncias/pages/casos_fechados.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name__in=["Coordenadores", "Agentes"]).exists():
            return Denuncia.objects.filter(status="Fechado")
        if self.request.user.groups.filter(name="Clientes").exists():
            return Denuncia.objects.filter(status="Fechado", denunciante_id=self.request.user.id)


        return Denuncia.objects.none()
