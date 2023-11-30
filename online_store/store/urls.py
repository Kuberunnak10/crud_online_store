from django.urls import path


from store.views import create_wear, success_page, show, edit, update, delete

urlpatterns = [
    path('create/', create_wear, name='create_wear'),
    path('success_page/', success_page, name='success_page'),
    path('', show, name='show'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
