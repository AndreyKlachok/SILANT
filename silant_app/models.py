from django.db import models
from django.urls import reverse



class VehicleModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'
    

class EngineModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателя'


class TransmissionModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссии'



class DriveAxleModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущего моста'
    

class SteerableAxleModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемого моста'
    

class ServiceCompany(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'


class TypeService(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вид ТО'
    

class NodeRejection(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'
    

class SpareParts(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='Описания нет')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Используемые запчасти'



class Car(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    machine_serial_number = models.CharField(max_length=255, unique=True, verbose_name='Зав. № машины')
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, verbose_name='Модель техники')  
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE, verbose_name='Модель двигателя') 
    engine_serial_number = models.CharField(max_length=255, verbose_name='Зав. № двигателя') 
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmission_serial_number = models.CharField(max_length=255, verbose_name='Зав. № трансмиссии')
    drive_axle_model = models.ForeignKey(DriveAxleModel, on_delete=models.CASCADE, verbose_name='Модель ведущего моста') 
    drive_axle_serial_number = models.CharField(max_length=255, verbose_name='Зав. № ведущего моста')
    steerable_axle_model = models.ForeignKey(SteerableAxleModel, on_delete=models.CASCADE, verbose_name='Модель управляемого моста') 
    steerable_axle_serial_number = models.CharField(max_length=255, verbose_name='Зав. № управляемого моста') 
    delivery_contract = models.CharField(max_length=255, verbose_name='Договор поставки №, дата') 
    shipping_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата отгрузки с завода') 
    consignee = models.CharField(max_length=255, verbose_name='Грузополучатель') 
    delivery_address = models.CharField(max_length=255, verbose_name='Адрес поставки') 
    equipment = models.CharField(max_length=255, verbose_name='Комплектация') 
    client = models.CharField(max_length=255, verbose_name='Клиент') 
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания') 

    def __str__(self):
        return self.machine_serial_number
    
    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})
    
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Service(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE, verbose_name='Вид ТО') 
    date_service = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата проведения ТО')  
    operating_time = models.IntegerField(verbose_name='Наработка, м/час')  
    work_order_number = models.CharField(max_length=255, verbose_name='№ заказ-наряда')  
    work_order_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата заказ-наряда')  
    organization = models.CharField( blank=True,max_length=255) 
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина') 
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания') 

    def __str__(self):
        return self.work_order_number
    
    def get_absolute_url(self):
        return reverse('service', kwargs={'service_slug': self.slug})
    
    class Meta:
        verbose_name = 'Тех. обслуживание'
        verbose_name_plural = 'Технические обслуживания'


class Claims(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    date_rejection = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата отказа') 
    operating_time = models.IntegerField(verbose_name='Наработка, м/час') 
    node_rejection = models.ForeignKey(NodeRejection, on_delete=models.CASCADE, verbose_name='Характер отказа')  
    description_rejection = models.CharField(max_length=255, verbose_name='Описание отказа') 
    recovery_method = models.CharField(max_length=255, verbose_name='Способ восстановления') 
    spare_parts = models.ForeignKey(SpareParts,blank=True, null=True, on_delete=models.CASCADE, verbose_name='Используемые запчасти')
    date_recovery = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата востановления')
    machine_downtime = models.CharField(max_length=255, verbose_name='Время простоя техники')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')  
    service_company = models.ForeignKey(ServiceCompany,blank=True, on_delete=models.CASCADE, verbose_name='Сервисная компания') 

    def __str__(self):
        return self.description_rejection
    
    def get_absolute_url(self):
        return reverse('claims', kwargs={'claims_slug': self.slug})
    
    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'