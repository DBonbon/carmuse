from django.shortcuts import render
from django.views.generic import ListView
from about.models import AboutPage
from django.views import generic
from django.views.generic.base import TemplateView


class AboutUs(TemplateView):
    model = AboutPage
    # context_object_name = 'about'
    template_name = 'about/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutpages'] = AboutPage.objects.get(id=1)
        return context


class AboutPageDetailView(generic.DetailView):
    model = AboutPage
    #context_object_name = 'about'
    queryset = AboutPage.objects.filter(id=1)
    template_name = 'about/aboutdetail_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#class AboutPageListView(ListView):
 #   model = AboutPage
  #  context_object_name = 'about'
   # template_name = "about/aboutpage_list.html"