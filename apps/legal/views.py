from django.views.decorators.cache import cache_page
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render
from .models import Document, DocumentInfo, ClientAnswer, DocumentType
from .forms import DocumentForm
from django.views.generic import CreateView, UpdateView
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
import io

from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login')
def document_listing(request):
    if request.user.is_authenticated:
        return render(request, 'legal/document_listing.html', {'document_types': DocumentType.objects.all()})

class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm


    def form_valid(self, form):
        form.instance.client = self.request.user
        form.instance.type = DocumentType.objects.get(name=self.kwargs['type'])
        return super(DocumentCreateView, self).form_valid(form)

            
class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.instance.type = DocumentType.objects.get(name=self.kwargs['type'])
        return super(DocumentCreateView, self).form_valid(form)


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.client = self.request.user
            form.instance.type = DocumentType.objects.get(name=self.kwargs['type'])
            form.instance.save()
            return HttpResponseRedirect(form.instance.get_absolute_url())


    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if form.is_valid():
            form.instance.client = self.request.user
            form.instance.type = DocumentType.objects.get(name=self.kwargs['type'])
            form.instance.save()
            return HttpResponseRedirect(form.instance.get_absolute_url())

@login_required(login_url='/accounts/login')
def document_detail(request, id):
    if request.user.is_authenticated:
        document = Document.objects.get_or_create(id=id, client=request.user)[0]

        if request.POST:
            data = request.POST.dict()
            for k, v in data.items():
                try:
                    document_info = DocumentInfo.objects.get(name=k)
                    item = ClientAnswer.objects.get(document=document, document_info=document_info, client=request.user)
                    item.answer = v
                    item.save()
                except DocumentInfo.DoesNotExist as e:
                    continue
                except ClientAnswer.DoesNotExist as e:
                    continue
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
            buffer = io.BytesIO()
            document.generate_document().write(buffer)
            response.write(buffer.getvalue())
            return response

        return render(request, 'legal/document.html', {'document': document,
        'questions': ClientAnswer.objects.filter(client=request.user, document=document).order_by('document_info__display_order')})
