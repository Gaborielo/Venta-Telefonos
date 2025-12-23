from django.db import models

# Create your models here.
class Marca (models.Model):
    nombre = models.CharField(max_length=100)
    especificaciones = models.TextField()
    def __str__(self):
        return self.nombre

class Telefono (models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="imagenes/", null=True, blank=True)
    def __str__(self):
        return f"{self.marca} - {self.modelo}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contacto = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20,choices=[("pagado", "Pagado"),("cancelado", "Cancelado")])

    def __str__(self):
        return f"Pedido #{self.id}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.telefono} x {self.cantidad}"