from django.urls import reverse
from rest_framework.test import APITestCase

class GlobalViewSemAuthTestCase(APITestCase):
  
  
  def setUp(self, url:str):
    self.url_name = url
    self.url = reverse(f'{url}-list')
    
  def gerar_url_com_id(self, id:int):
    return reverse(self.url_name, args=[id])
    
  def fazer_requisicao_get(self):
    return self.client.get(self.url)
  
  def fazer_requisicao_post(self, data):
    return self.client.post(self.url, data)
  
  def fazer_requisicao_put(self, id:int, data):
    return self.client.put(f'/{self.url_name}/{str(id)}/', data)
  
  def fazer_requisicao_patch(self, id:int, data):
    return self.client.patch(f'/{self.url_name}/{str(id)}/', data)
  
  def fazer_requisicao_delete(self, id:int):
    return self.client.delete(f'/{self.url_name}/{str(id)}/')
  
  def espera_resposta_ser_ok(self, request):
    return self.assertEqual(request.status_code, 200)
  
  def espera_resposta_ser_created(self, request):
    return self.assertEqual(request.status_code, 201)
  
  def espera_resposta_ser_no_content(self, request):
    return self.assertEqual(request.status_code, 204)
  
  def espera_resposta_ser_forbidden(self, request):
    return self.assertEqual(request.status_code, 403)