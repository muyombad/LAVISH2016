from django.shortcuts import redirect


class DashboardAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/addmin/admin_dashboard' and not request.user.is_superuser and not request.user.groups.filter(name='muyombad').exists() :
            return redirect('/Dashboard')  # Replace with your staff dashboard URL
        elif request.path == '/Dashboard' and request.user.is_superuser:
            return redirect('/addmin/admin_dashboard')
       
            
        response = self.get_response(request)
        return response


