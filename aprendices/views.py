from django.template import loader
from django.http import HttpResponse
from .models import Aprendiz
from .forms import AprendizForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Aprendiz
from instructores.models import Instructor

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')    

    context = {
        'lista_aprendices': lista_aprendices,
    }
    return HttpResponse(template.render(context, request))


def detalle_aprendiz(request, id_aprendiz):
    aprendiz = Aprendiz.objects.get(id=id_aprendiz)
    template = loader.get_template('detalle_aprendiz.html')
    context = {
        'aprendiz': aprendiz,
    }
    return HttpResponse(template.render(context, request))


def inicio(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


# VISTAS BASADAS EN CLASES - CRUD APRENDIZ

# CREATE - APRENDIZ

class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'detalle_aprendices.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el aprendiz"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - APRENDIZ
class AprendizUpdateView(generic.UpdateView):
    """Vista para actualizar un aprendiz existente"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'detalle_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    pk_url_kwarg = 'aprendiz_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - APRENDIZ
class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""
    model = Aprendiz
    template_name = 'eliminar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    pk_url_kwarg = 'aprendiz_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        aprendiz = self.get_object()
        messages.success(
            request,
            f'El aprendiz {aprendiz.nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)