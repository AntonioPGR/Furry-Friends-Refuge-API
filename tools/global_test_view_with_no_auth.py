from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from django.urls import reverse
from usuarios.models import Usuario


class GlobalViewSemAuthTestCase(APITestCase):
  
  
  def setUp(self, url:str):
    self.url = reverse(f'{url}-list')
    
  def fazer_requisicao_get(self):
    return self.client.get(self.url)
  
  def fazer_requisicao_post(self, data):
    return self.client.post(self.url, data)
  
  def fazer_requisicao_put(self, data):
    return self.client.put(self.url, data)
  
  def fazer_requisicao_patch(self, data):
    return self.client.patch(self.url, data)
  
  def fazer_requisicao_delete(self, data):
    return self.client.delete(self.url, data)
  
  def espera_resposta_ser_ok(self, request):
    return self.assertEqual(request.status_code, 200)
  
  def espera_resposta_ser_created(self, request):
    return self.assertEqual(request.status_code, 201)
  
  def espera_resposta_ser_forbidden(self, request):
    return self.assertEqual(request.status_code, 403)

  def espera_resposta_ser_unauthorized(self, request):
    return self.assertEqual(request.status_code, 401)
  
  def autenticar_usuario(self, usuario:Usuario):
    return force_authenticate(user=usuario)