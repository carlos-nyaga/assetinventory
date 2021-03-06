from django.urls import include, path
from .views import asset_create, asset_delete, asset_detail, asset_list, asset_update, \
                    category_create, category_delete, category_detail, category_list, \
                    category_update, checkout_create, checkout_delete, checkout_detail, \
                    checkout_list, checkout_update

app_name = 'inventory'
urlpatterns = [
    path('assets/', include([
        path('', asset_create, name='asset-add'),
        path('', asset_list, name='asset-list'),
        path('<uuid:pk>', asset_update, name='asset-edit'),
        path('<uuid:pk>', asset_delete, name='asset-delete'),
        path('<uuid:pk>', asset_detail, name='asset-detail'),
    ])),

    path('categories/', include([
        path('', category_create, name='category-add'),
        path('', category_list, name='category-list'),
        path('<uuid:pk>', category_update, name='category-edit'),
        path('<uuid:pk>', category_delete, name='category-delete'),
        path('<uuid:pk>', category_detail, name='category-detail'),
    ])),

    path('events/', include([
        path('', checkout_create, name='checkout-add'),
        path('', checkout_list, name='checkout-list'),
        path('<uuid:pk>', checkout_update, name='checkout-edit'),
        path('<uuid:pk>', checkout_delete, name='checkout-delete'),
        path('<uuid:pk>', checkout_detail, name='checkout-detail'),
    ])),
]