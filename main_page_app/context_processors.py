from announcment_app.views import Announcment

def latest_announcement(request):
    latest_ann = Announcment.objects.order_by('-created_at').first()  # Залежить від вашої моделі
    return {'latest_anns': latest_ann}