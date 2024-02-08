from backend_app.models import Owner, Raspy, Sensor, DataEntry
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def testOwner(request):
    owner = Owner.objects.all()
    owner = owner[0]
    html = (
        "<html><body>Erster owner in der Datenbank ist: %s</body></html>" % owner.name
    )
    return HttpResponse(html)


def testRaspy(request):
    raspy = Raspy.objects.all()
    raspy = raspy[0]
    html = (
        "<html><body>Erster raspy in der Datenbank ist: %s</body></html>" % raspy.name
    )
    return HttpResponse(html)


def testDataEntry(request):
    dataEntries = DataEntry.objects.all()
    dataEntryDivs = []
    for dataEntry in dataEntries:
        for attr, value in dataEntry.__dict__.items():
            dataEntryDivs.append("<div>%s: %s</div>" % (attr, value))
    html = "<html><body>%s</body></html>" % "".join(dataEntryDivs)
    return HttpResponse(html)
