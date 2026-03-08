from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django_ledger.views.feedback import BugReportView, RequestNewFeatureView


urlpatterns = [

    # Django admin panel
    path('admin/', admin.site.urls),

    # Django Ledger main URLs
    path('', include(('django_ledger.urls', 'django_ledger'), namespace='django_ledger')),

    # Feedback endpoints (send issues to GitHub)
    path(
        'feedback/bug/',
        BugReportView.as_view(),
        name='bug-report'
    ),

    path(
        'feedback/feature/',
        RequestNewFeatureView.as_view(),
        name='feature-request'
    ),

]