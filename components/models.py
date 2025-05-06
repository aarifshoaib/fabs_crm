from django.db import models

class Contacts(models.Model):
    comp_code = models.CharField(max_length=10)
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    social_profile = models.CharField(max_length=500, null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    visibility = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.contact_name
     
    class Meta:
        db_table = "crm_contacts"


class Deals(models.Model):
    deal_id = models.AutoField(primary_key=True)
    deal_name = models.CharField(max_length=255, null=False, blank=False)
    pipeline = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)
    deal_value = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    currency = models.CharField(max_length=50, null=False, blank=False)
    period = models.CharField(max_length=50, null=False, blank=False)
    period_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # contactid = models.ForeignKey('Contacts', on_delete=models.SET_NULL, null=True, blank=True)
    # projectid = models.ForeignKey('Projects', on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    expected_closingdate = models.DateField(null=True, blank=True)
    # assigneeid = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True)
    follow_up_date = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)
    priority = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)



    def __str__(self):
        return self.deal_name
    
    class Meta:
        db_table = "crm_deals"

    
    

class Leads(models.Model):
    lead_id = models.AutoField(primary_key=True)
    lead_name = models.CharField(max_length=255, null=False, blank=False)
    lead_type = models.CharField(max_length=50, null=False, blank=False)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_image = models.CharField(max_length=255, null=True, blank=True)
    company_address = models.CharField(max_length=255, null=True, blank=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    currency = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    visibility = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=False, blank=False, default='Active')
    owner = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lead_name
    
    class Meta:
        db_table = "crm_leads"
        ordering = ['-created_date'] 
