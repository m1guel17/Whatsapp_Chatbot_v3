import os

welcome_msg = os.environ.get('WELCOME') or "Bienvenido a Lian Accesorios ☺️, Enviamos captura pantalla de los productos que viste en live y quieres adquirir. El monto mínimo para separar tus productos es de 30 soles!!"
payment_msg = os.environ.get('PAYMENT') or "Si desea pagar yapee a este número xxx-xxx-xxx y luego indique su i nformación para el envío \n1️⃣ Dirección\n2️⃣ Referencia\n3️⃣ Consideraciones"