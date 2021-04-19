from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404 
from django.core.paginator import Paginator

from django.db.models import Q

from django.shortcuts import redirect
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework.views import APIView

from .models import Transcript, Mother

def index(request):
    submitbutton= request.GET.get('button') 
    if (submitbutton):
        if 'query_name' in request.GET:
            srh_name = request.GET['query_name']
        else:
            srh_name = ""
        if "query_corpus" in request.GET:
            srh_corpus = request.GET['query_corpus']
        else:
            srh_corpus = ""
        srh_gender = request.GET['query_gender']
        srh_ses = request.GET['query_ses']
        if srh_gender != "any" and srh_ses != "any": 
            transcripts = Transcript.objects.filter(
                Q(name__icontains=srh_name),
                Q(corpus__icontains=srh_corpus),
                Q(child_gender=srh_gender),
                Q(ses=srh_ses),
            )
        elif srh_gender != "any": 
            transcripts = Transcript.objects.filter(
                Q(name__icontains=srh_name),
                Q(corpus__icontains=srh_corpus),
                Q(child_gender=srh_gender),
            )
        elif srh_ses != "any": 
            transcripts = Transcript.objects.filter(
                Q(name__icontains=srh_name),
                Q(corpus__icontains=srh_corpus),
                Q(ses=srh_ses),
            )
        else: 
            transcripts = Transcript.objects.filter(
                Q(name__icontains=srh_name),
                Q(corpus__icontains=srh_corpus)
            )
        transcripts.order_by("corpus")
        paginator = Paginator(transcripts, 30) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        params = {'page_obj': page_obj, 'query_name':srh_name, 'query_corpus':srh_corpus, 'query_gender': srh_gender, 'query_ses': srh_ses}
        return render(request, 'childes/index.html', params)
    else:
        transcript_list = Transcript.objects.order_by('corpus')
        paginator = Paginator(transcript_list, 30) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        params = {'page_obj': page_obj}
        return render(request, 'childes/index.html', params)


def detail(request, transcript_id):
    transcript = get_object_or_404(Transcript, pk=transcript_id)
    mother = Mother.objects.filter(
                Q(name=transcript.name),
            )
    if len(mother) == 1:
        return render(request, 'childes/detail.html', {'transcript': transcript, 'mother':mother[0]})
    else:
        return render(request, 'childes/detail.html', {'transcript': transcript, 'mother': None})

def SearchPage(request):
    srh_name = request.GET['query_name']
    srh_corpus = request.GET['query_corpus']
    srh_gender = request.GET['query_gender']
    if srh_gender != "any": 
        transcripts = Transcript.objects.filter(
            Q(name__icontains=srh_name),
            Q(corpus__icontains=srh_corpus),
            Q(gender=srh_gender),
        )
    else: 
        transcripts = Transcript.objects.filter(
            Q(name__icontains=srh_name),
            Q(corpus__icontains=srh_corpus)
        )
    params = {'transcripts': transcripts, 'query_name':srh_name, 'query_corpus':srh_corpus}
    return render(request, 'childes/searchpage.html', params)

def parse(request):
    return render(request, 'childes/upload.html')    

class ParseExcel(APIView):
    def post(self, request, format=None):
        ts = Transcript.objects.filter(corpus = "Gleason")
        starting_url = "https://sla.talkbank.org/TBB/childes/Eng-NA/"
        for t in ts:
            if t.corpus == "Hall":
                if t.ses == "WORK": 
                    if t.race == "White": 
                        t.url = starting_url + 'Hall/WhiteWork/' + t.name
                    else:
                        t.url = starting_url + 'Hall/BlackWork/' + t.name
                if t.ses == "PRO": 
                    if t.race == "White":
                        t.url = starting_url + 'Hall/WhitePro/' + t.name
                    else:
                        t.url = starting_url + 'Hall/BlackPro/' + t.name
            if t.corpus == "Gleason":
                t.url = starting_url + 'Gleason/Mother/' + t.name
            if t.corpus == "Morisset":
                t.url = starting_url + 'Morisset/Seattle/' + t.name 
            if t.corpus == "Warren":
                t.url = starting_url + 'Warren/' + t.name
            t.save() 

        # try:
        #     excel_file = request.FILES['files']
        # except MultiValueDictKeyError:
        #     return None 
        # if (str(excel_file).split('.')[-1] == "xls"):
        #     data = xls_get(excel_file, column_limit=38)
        # elif (str(excel_file).split('.')[-1] == "xlsx"):
        #     data = xlsx_get(excel_file, column_limit=38)
        # else:
        #     return None 
        # child_data = data['child']
        # mother_data = data['mother']
        # for i, cd in enumerate(child_data):
        #     if (i != 0):
        #         Transcript.objects.create(
        #             name = cd[0],
        #             corpus = cd[2],
        #             child_age = cd[4], 
        #             child_gender = cd[5], 
        #             race = cd[7], 
        #             ses = cd[8], 
        #             tot_utts = cd[13], 
        #             mlu_utts = cd[14],
        #             mlu_words = cd[15],
        #             mlu_morphs = cd[16],
        #             freq_ttr = cd[19],
        #             percent_nouns = cd[25],
        #             percent_verbs = cd[27], 
        #             percent_adjs = cd[36],
        #             percent_adv = cd[37],
        #             percent_prep = cd[35],
        #         )

        # for i, md in enumerate(mother_data):
        #     if (i != 0):
        #         Mother.objects.create(
        #             name = md[0],
        #             corpus = md[2],
        #             tot_utts = md[13], 
        #             mlu_utts = md[14],
        #             mlu_words = md[15],
        #             mlu_morphs = md[16],
        #             freq_ttr = md[19],
        #             percent_nouns = md[25],
        #             percent_verbs = md[27], 
        #             percent_adjs = md[36],
        #             percent_adv = md[37],
        #             percent_prep = md[35],
        #         )