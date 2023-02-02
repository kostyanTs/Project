from django.shortcuts import render


from django.http import (
    HttpRequest,
    HttpResponse
)

from main.models import Pen
from main.forms import PenForm
from django.views.generic import View

class PenView(View):
    """Pen view."""

    form = PenForm

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='main/pen_form.html',
            content_type={
                'ctx_form' : self.form()
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = PenForm(
            request.POST
        )
        if not form.is_valid():
            return HttpResponse("BAD")
        print(form.cleaned_data)
        form.save()
        return HttpResponse("OK")
