from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', 'common.views.base'),
    url(r'^reset/$', 'common.views.reset_password_instance'),
    url(r'^password/(?P<token>.*)/$', 'common.views.reset_password'),
    url(r'^user/login/', 'account.views.login'),
    url(r'^logout/?$',  'django.contrib.auth.views.logout_then_login'),
    url(r'^user/register/$',  'account.views.register'),
    url(r'^user/change_password/$',  'profile.views.password_change'),
    url(r'^user/change_email/$',  'profile.views.email_change'),
    url(r'^user/change_first_name/$',  'profile.views.first_name_change'),
    url(r'^user/change_last_name/$',  'profile.views.last_name_change'),
    url(r'^user/change_personal_info/$',  'profile.views.personal_info_change'),
    url(r'^user/check/$',  'profile.views.check_user'),
    url(r'^profile/$',  'profile.views.myprofile'),
    url(r'^account/change-password$',  'account.views.change_password'),
    url(r'^stream/clan$',  'alliance.views.get_stream'),
    url(r'^profile/stream/clan$',  'profile.views.stream_clan'),
    url(r'^profile/widget-lvl$',  'profile.views.widget_lvl'),
    url(r'^profile/widget-territory$',  'profile.views.widget_territory'),
    url(r'^profile/dismiss-clan$',  'profile.views.dismiss_clan'),
    url(r'^profile/get_users/$',  'profile.views.get_users'),
    url(r'^profile/sendmessage/$',  'profile.views.send_message'),
    url(r'^profile/friendrequest/$',  'profile.views.friendrequest'),
    url(r'^profile/(?P<profile_id>\d+)$',  'profile.views.profiles'),
    url(r'^profile/(?P<profile_id>\d+)/add_friend/$',  'profile.views.add_friend_request'),
    url(r'^profile/(?P<profile_id>\d+)/un_friend/$',  'profile.views.un_friend'),
    url(r'^notification/seen/(?P<notification_id>\d+)$',  'notification.views.seen_notification'),
    url(r'^ranks/$',  'ranks.views.ranks'),
    url(r'^alliance/create/$',  'alliance.views.create'),
    url(r'^clan$',  'alliance.views.my_clan'),
    url(r'^clan/avatar$',  'alliance.views.upload_avatar'),
    url(r'^clan/del-member$',  'alliance.views.del_member'),
    url(r'^clan/create-news$',  'alliance.views.create_news'),
    url(r'^clan/name-change$',  'alliance.views.name_change'),
    url(r'^clan/vote-news$',  'alliance.views.vote_news'),
    url(r'^clan/check-like-state$',  'alliance.views.check_like_state'),
    url(r'^alliance/request/$',  'alliance.views.request'),
    url(r'^alliance/process_request/$',  'alliance.views.process_request'),
    url(r'^battle/request/war$',  'battle.views.war_request'),
    url(r'^external-api/login/$',  'external-api.views.login'),
    url(r'^external-api/checkin/$',  'external-api.views.checkingin'),
    url(r'^map/$',  direct_to_template, {'template': 'map.html'}),
    url(r'^territory/create$',  'territory.views.create_territory'),
    url(r'^territory/verify$',  'territory.views.verify_territory'),
    url(r'^location/get-locations$',  'location.views.get_locations'),
    url(r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^feedback', include('feedback.urls')),
    url(r'^territory/load', 'territory.views.load_territory'),
    url(r'^territory/upgrade', 'territory.views.upgrade'),
    url(r'^territory/name', 'territory.views.change_name'),
    url(r'^territory/color', 'territory.views.change_color'),
    url(r'^facebook/login$', 'facebook.views.login'),
    url(r'^facebook/authentication_callback$', 'facebook.views.authentication_callback'),
    url(r'^sentry/', include('sentry.web.urls')),
    url(r'^google/login$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^login-complete/google$', 'django_openid_auth.views.login_complete', name='openid-complete'),

)

handler404 = 'common.views.base'

urlpatterns += staticfiles_urlpatterns()