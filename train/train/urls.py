from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URLの全体設計
urlpatterns = [
    # 今回作成するアプリ「charge_search」にアクセスするURL
    path('chargesearch/', include('charge_search.urls')),
    # 何もURLを指定しない場合（app_config/views.pyで、自動的に「charge_search」にアクセスするよう設定済み）
    path('', views.index, name='index'),
    # 管理サイトにアクセスするURL
    path('admin/', admin.site.urls),
    #path('api/', include('charge_api.urls')),
]

# メディアファイル公開用のURL設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)