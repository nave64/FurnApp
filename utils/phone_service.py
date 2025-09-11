# import random
# from django import forms
# from django.http import request
# from django.shortcuts import redirect, render
# from django.urls import reverse
#
# # from account_module import views
# # from account_module.views import RegisterView
# from kavenegar import *
#
# from account_module.forms import RegisterForm
# import random
#
# from account_module.models import User
# register_form = RegisterForm()
#
# token = random.randint(1, 1000000)
# def send_code():
#     user_phone = register_form.cleaned_data.get('phone')
#     try:
#         api = KavenegarAPI(
#             '4371333969556E6D3966736D65586E39703737485739697675696B644E30332B74586C784E4C68586133593D')
#         params = {
#             'receptor': user_phone,
#             'template': 'verifyuserabzaresf',
#             'token': token,
#             # 'token2': '',
#             # 'token3': '',
#             'type': 'sms',  # sms vs call
#         }
#         response = api.verify_lookup(params)
#         # print(response)
#     except APIException as e:
#         pass
#     except HTTPException as e:
#         pass
#
#
#
#
#
#
#
#
#
#
