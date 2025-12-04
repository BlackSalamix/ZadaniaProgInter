from django.shortcuts import render
from .models import Visit
def index(request):
    visit, created = Visit.objects.get_or_create(id=1)
    visit.count += 1
    visit.save()
    return render(request, 'visitcounter/index.html', {'visit_count': visit.count})