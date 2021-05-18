from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "596bdc4fc7mshd7e8d7357ec2827p1b32eajsnb78e76c9d770",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloworldview(request):
    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):
    	
        mylist.append(response['response'][x]['country'])
    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry':selectedcountry,'mylist':mylist, 'new':new, 'active':active, 'critical':critical, 'recovered':recovered, 'total':total, 'deaths':deaths}
        return render(request, 'helloworld.html',context)

    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):

        mylist.append(response['response'][x]['country'])
    context = {'mylist':mylist}
    return render(request,'helloworld.html',context)