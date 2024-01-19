# vrexApp/charts.py
from django.db.models import Count
from django.db.models.functions import TruncMonth
from .models import SchoolForm
from django.http import JsonResponse
from django.utils import timezone


def school_form_statistics(request):
    # 1. Total number of SchoolForm Request
    total_requests = SchoolForm.objects.count()

    # 2. Total number of ongoing request
    ongoing_requests = SchoolForm.objects.filter(status='Ongoing').count()

    # 3. Number of document request per month - bar graph
    document_requests_per_month = SchoolForm.objects.annotate(
        month=TruncMonth('request_date')
    ).values('month').annotate(count=Count('id')).order_by('month')

    labels = [item['month'].strftime('%B %Y') for item in document_requests_per_month]
    data = [item['count'] for item in document_requests_per_month]

    chart_data = {
        'total_requests': total_requests,
        'ongoing_requests': ongoing_requests,
        'document_requests': {
            'labels': labels,
            'data': data,
        },
    }

    # 4. Recent action by the client user
    recent_actions = SchoolForm.objects.filter(
        status__in=['Ongoing', 'Completed'],
    ).order_by('-date_released')[:5]

    recent_actions_data = [
        {
            'unique_id': f'F{item.id:04d}',
            'full_name': f"{item.first_name} {item.last_name}",
            'status': item.status,
            'date_released': item.date_released.strftime('%m-%d-%Y') if item.date_released else "N/A",
        }
        for item in recent_actions
    ]

    chart_data['recent_actions'] = recent_actions_data

    return JsonResponse(chart_data)
