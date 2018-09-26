from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import AuthRegistration, AuthConfirmEmail

urlpatterns = [
    # Core Authentication 
    url(r'^api-token-auth/', obtain_jwt_token, name="auth-token-create"),
    url(r'^api-token-refresh/', refresh_jwt_token, name="auth-token-refresh"),
    
    #url(r'^api-token-revoke/', revoke_jwt_token, name="auth-token-revoke")

    # Other Authentication
    url(r'^register/$', AuthRegistration.as_view() , name="auth-register"),
    url(r'^deleteaccount$', AuthRegistration.as_view(, name="auth-delete-account")
    url(r'^confirmemail/$', AuthConfirmEmail.as_view(), name="auth-confirm-email"),
    url(r'^resendconfirmationemail/$', , name="auth-resend-confirm-email"),
    url(r'^forgotpassword/$', , name="auth-forgot-password"),
    url(r'^resetpassword/$', , name="auth-reset-password")
    url(r'^changepassword/$', , name="auth-change-password")
]