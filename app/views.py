"""

import os
import subprocess
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CertificateRequest, PersonCertificate

@csrf_exempt
def generate_ovpn_certificate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            device_id = data.get('device_id')
            site_id = data.get('site_id')
            server_ip = data.get('server_ip')
            device_type = data.get('device_type')
            model_name = data.get('model_name')
            customer_name = data.get('customer_name')
            project_type = data.get('project_type')

            customer_name = CertificateRequest.generate_unique_customer_name(customer_name)

            ovpn_certificate = CertificateRequest(
                device_id=device_id,
                site_id=site_id,
                server_ip=server_ip,
                device_type=device_type,
                model_name=model_name,
                customer_name=customer_name,
                project_type=project_type
            )
            ovpn_certificate.save()

            os.environ['TERM'] = 'xterm'

           
            command = f'sshpass -p weLcome2IT ssh root@{server_ip} "TERM=xterm /root/OpenVPN-Setup/new_openvpn-install.sh 1 {customer_name}"'
            
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            print("hiiiiiiiiiiiiiiiiii", result)
            
            if result.returncode == 0:
                remote_certificate_file_path = f'/root/certificate/{customer_name}.ovpn'
                
                scp_command = f'sshpass -p weLcome2IT scp root@{server_ip}:{remote_certificate_file_path} .'
                scp_result = subprocess.run(scp_command, shell=True, stderr=subprocess.PIPE)
                
                if scp_result.returncode == 0:
                    filename = f'{customer_name}.ovpn'
                    
                    with open(filename, 'rb') as ovpn_file:
                        ovpn_content = ovpn_file.read()

                    response = HttpResponse(ovpn_content, content_type='application/octet-stream')
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                else:
                    return JsonResponse({'error': f'SCP command execution failed. Stderr: {scp_result.stderr.decode()}'}, status=500)
            else:
                return JsonResponse({'error': f'Command execution failed. Stdout: {result.stdout.decode()}, Stderr: {result.stderr.decode()}'}, status=500)

        except Exception as e:
            return JsonResponse({'error': f'Internal server error: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)



@csrf_exempt
def generate_person_certificate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            server_ip = data.get('server_ip')
            person_name = data.get('person_name')
            project_name = data.get('project_name')

            person_name = PersonCertificate.generate_unique_person_name(person_name)

            ovpn_certificate1 = PersonCertificate(
                server_ip=server_ip,
                person_name=person_name,
                project_name=project_name
            )
            ovpn_certificate1.save()

            os.environ['TERM'] = 'xterm'

           
            command = f'sshpass -p weLcome2IT ssh root@{server_ip} "TERM=xterm /root/OpenVPN-Setup/new_openvpn-install.sh 1 {person_name}"'
            
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            print("hiiiiiiiiiiiiiiiiii", result)
            
            if result.returncode == 0:
                remote_certificate_file_path = f'/root/certificate/{person_name}.ovpn'
                
                scp_command = f'sshpass -p weLcome2IT scp root@{server_ip}:{remote_certificate_file_path} .'
                scp_result = subprocess.run(scp_command, shell=True, stderr=subprocess.PIPE)
                
                if scp_result.returncode == 0:
                    filename = f'{person_name}.ovpn'
                    
                    with open(filename, 'rb') as ovpn_file:
                        ovpn_content = ovpn_file.read()

                    response = HttpResponse(ovpn_content, content_type='application/octet-stream')
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                else:
                    return JsonResponse({'error': f'SCP command execution failed. Stderr: {scp_result.stderr.decode()}'}, status=500)
            else:
                return JsonResponse({'error': f'Command execution failed. Stdout: {result.stdout.decode()}, Stderr: {result.stderr.decode()}'}, status=500)

        except Exception as e:
            return JsonResponse({'error': f'Internal server error: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
"""



# import os
# import subprocess
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import CertificateRequest, PersonCertificate

# def generate_certificate(request, certificate_type):
#     try:
#         data = json.loads(request.body.decode('utf-8'))
#         server_ip = data.get('server_ip')
#         name = data.get('name')
        
#         if certificate_type == 'device':
#             #customer_name = data.get('customer_name')
#             customer_name = CertificateRequest.generate_unique_customer_name(name)
#             certificate = CertificateRequest(
#                 server_ip=server_ip,
#                 device_id=data.get('device_id'),
#                 site_id=data.get('site_id'),
#                 device_type=data.get('device_type'),
#                 model_name=data.get('model_name'),
#                 customer_name=customer_name,
#                 project_type=data.get('project_type'),
#             )
#         elif certificate_type == 'person':
#             #person_name = data.get('person_name')
#             person_name = PersonCertificate.generate_unique_person_name(name)
#             certificate = PersonCertificate(
#                 server_ip=server_ip,
#                 person_name=person_name,
#                 project_name=data.get('project_name'),
#             )
#         else:
#             return JsonResponse({'error': 'Invalid certificate type.'}, status=400)

#         certificate.save()
#         os.environ['TERM'] = 'xterm'
        
#         remote_certificate_file_path = f'/root/certificate/{name}.ovpn'
#         command = f'sshpass -p weLcome2IT ssh root@{server_ip} "TERM=xterm /root/OpenVPN-Setup/new_openvpn-install.sh 1 {name}"'
        
#         result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
#         if result.returncode == 0:
#             scp_command = f'sshpass -p weLcome2IT scp root@{server_ip}:{remote_certificate_file_path} .'
#             scp_result = subprocess.run(scp_command, shell=True, stderr=subprocess.PIPE)
            
#             if scp_result.returncode == 0:
#                 filename = f'{name}.ovpn'
                
#                 with open(filename, 'rb') as ovpn_file:
#                     ovpn_content = ovpn_file.read()
                
#                 response = HttpResponse(ovpn_content, content_type='application/octet-stream')
#                 response['Content-Disposition'] = f'attachment; filename="{filename}"'
#                 return response
#             else:
#                 return JsonResponse({'error': f'SCP command execution failed. Stderr: {scp_result.stderr.decode()}'}, status=500)
#         else:
#             return JsonResponse({'error': f'Command execution failed. Stdout: {result.stdout.decode()}, Stderr: {result.stderr.decode()}'}, status=500)
    
#     except Exception as e:
#         return JsonResponse({'error': f'Internal server error: {str(e)}'}, status=500)

# @csrf_exempt
# def generate_ovpn_certificate(request):
#     if request.method == 'POST':
#         return generate_certificate(request, 'device')
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=405)

# @csrf_exempt
# def generate_person_certificate(request):
#     if request.method == 'POST':
#         return generate_certificate(request, 'person')
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=405)



import os
import subprocess
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CertificateRequest, PersonCertificate

@csrf_exempt
def generate_certificate(request, certificate_type):
    try:
        data = json.loads(request.body.decode('utf-8'))
        server_ip = data.get('server_ip')
        
        if certificate_type == 'device':
            customer_name = f"{data.get('device_type')}_{data.get('site_id')}_{data.get('customer_name')}"
            certificate = CertificateRequest(
                server_ip=server_ip,
                device_id=data.get('device_id'),
                site_id=data.get('site_id'),
                device_type=data.get('device_type'),
                model_name=data.get('model_name'),
                customer_name=customer_name,
                project_type=data.get('project_type'),
            )
        elif certificate_type == 'person':
            person_name = f"{data.get('project_name')}_{data.get('person_name')}"
            certificate = PersonCertificate(
                server_ip=server_ip,
                person_name=person_name,
                project_name=data.get('project_name'),
            )
        else:
            return JsonResponse({'error': 'Invalid certificate type.'}, status=400)

        certificate.save()
        os.environ['TERM'] = 'xterm'
        
        remote_certificate_file_path = f'/root/certificate/{customer_name if certificate_type == "device" else person_name}.ovpn'
        command = f'sshpass -p weLcome2IT ssh root@{server_ip} "TERM=xterm /root/OpenVPN-Setup/new_openvpn-install.sh 1 {customer_name if certificate_type == "device" else person_name}"'
        
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            scp_command = f'sshpass -p weLcome2IT scp root@{server_ip}:{remote_certificate_file_path} .'
            scp_result = subprocess.run(scp_command, shell=True, stderr=subprocess.PIPE)
            
            if scp_result.returncode == 0:
                filename = f'{customer_name if certificate_type == "device" else person_name}.ovpn'
                
                with open(filename, 'rb') as ovpn_file:
                    ovpn_content = ovpn_file.read()
                
                response = HttpResponse(ovpn_content, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            else:
                return JsonResponse({'error': f'SCP command execution failed. Stderr: {scp_result.stderr.decode()}'}, status=500)
        else:
            return JsonResponse({'error': f'Command execution failed. Stdout: {result.stdout.decode()}, Stderr: {result.stderr.decode()}'}, status=500)
    
    except Exception as e:
        return JsonResponse({'error': f'Internal server error: {str(e)}'}, status=500)



@csrf_exempt
def generate_device_certificate(request):
    return generate_certificate(request, 'device')

@csrf_exempt
def generate_person_certificate(request):
    return generate_certificate(request, 'person')
