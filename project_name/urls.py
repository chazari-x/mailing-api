from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # добавляем маршруты, связанные с приложением polls
    path('', include('polls.urls')),

    # добавляем стандартный маршрут административной панели Django
    path('admin/', admin.site.urls),
]
