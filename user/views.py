from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
import json

User = get_user_model()

# Create your views here.

def user_profile(request):
    return JsonResponse({"message": "User profile endpoint"})

@csrf_exempt
@require_POST
def github_oauth_login(request):
    data = json.loads(request.body.decode())
    token = data.get('token')
    if not token:
        return JsonResponse({'error': 'Token required'}, status=400)

    # Get user info from GitHub
    headers = {'Authorization': f'token {token}'}
    github_response = requests.get('https://api.github.com/user', headers=headers)
    if github_response.status_code != 200:
        return JsonResponse({'error': 'Invalid GitHub token'}, status=401)
    github_data = github_response.json()
    username = github_data.get('login')
    email = github_data.get('email')
    if not email:
        # Try to get emails if not public
        emails_resp = requests.get('https://api.github.com/user/emails', headers=headers)
        if emails_resp.status_code == 200:
            emails = emails_resp.json()
            primary_emails = [e['email'] for e in emails if e.get('primary') and e.get('verified')]
            if primary_emails:
                email = primary_emails[0]
    if not username or not email:
        return JsonResponse({'error': 'Could not fetch username or email from GitHub'}, status=400)

    user, created = User.objects.get_or_create(username=username, defaults={
        'email': email,
        'password': token  # Store token as password (not recommended for production)
    })
    if not created:
        # Update password to latest token
        user.password = token
        user.save()
    return JsonResponse({'username': user.username, 'email': user.email, 'created': created})
