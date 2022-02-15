from django.shortcuts import render
from django.http import HttpResponse
from SaleReportApp.models import SaleData
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.db.models import Sum

# Create your views here.
def index(request):
    sale_list = SaleData.objects.all()
    page = request.GET.get('page', 1)
    top_country = SaleData.objects.order_by('-Total_Revenue')[:10]
    top_region = SaleData.objects.order_by('-Total_Revenue')[:3]
    top_selling = SaleData.objects.order_by('-Units_Sold')[:5]
    offline = SaleData.objects.filter(Sales_Channel = 'Offline')
    online = SaleData.objects.filter(Sales_Channel = 'Online')
    queryset = SaleData.objects.values('Order_Date__year').annotate(total_sum=Sum('Total_Revenue')).order_by('Order_Date__year')

    paginator = Paginator(sale_list, 10)

    try:
        sale_list = paginator.page(page)
    except PageNotAnInteger:
        sale_list = paginator.page(1)
    except EmptyPage:
        sale_list = paginator.page(paginator.num_pages)
    
    return render(request, 'index.html',{'sale_list': sale_list, 'top_country': top_country, 'top_region': top_region, 'top_selling': top_selling, 'offline': offline, 'online': online, 'queryset': queryset })
