from django.shortcuts import render, redirect
from django.views import View
from .models import BasicFareModel
from .forms import SearchForm
from .main import main


class TopPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charge_search/top_page.html")


top_page = TopPageView.as_view()


class SearchView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, "charge_search/joban.html", {"form": form})

    def post(self, request, *args, **kwargs):
        line = request.POST["line"]
        form = SearchForm(request.POST)
        try:
            context = main(request, line)
        except:
            return render(
                request,
                "charge_search/" + line + ".html",
                context={"err_msg": "入力内容をご確認ください。", "form": form},
            )
        return render(
            request, "charge_search/" + line + "_result.html", context=context
        )


joban = SearchView.as_view()
