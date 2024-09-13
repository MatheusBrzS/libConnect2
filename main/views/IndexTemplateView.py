from typing import Any
from django.views.generic import TemplateView

from main.models.Livro import Livro

class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['livros'] = Livro.objects.all()
        return context