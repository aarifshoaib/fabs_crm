from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacts
from .models import Deals
from .models import Leads
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from datetime import datetime


##### Contacts Table #####


def post_contact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id') 
        contact_name = request.POST.get('contact_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        social_profile = request.POST.get('social_profile')
        tags = request.POST.get('tags')
        description = request.POST.get('description')
        visibility = request.POST.get('visibility')
        is_active = 'Y' if request.POST.get('status') else 'N'

        if contact_id:
            contact = get_object_or_404(Contacts, contact_id=contact_id)
            contact.contact_name = contact_name
            contact.email = email
            contact.phone = phone
            contact.address = address
            contact.social_profile = social_profile
            contact.tags = tags
            contact.description = description
            contact.visibility = visibility
            contact.status = is_active
            contact.save()
        else:
            Contacts.objects.create(
                comp_code=1000,
                contact_name=contact_name,
                email=email,
                phone=phone,
                address=address,
                social_profile=social_profile,
                tags=tags,
                description=description,
                visibility=visibility,
                status=is_active
            )

        return redirect('contacts')

    fetch_datas = Contacts.objects.all()
    context = {'fetch_datas': fetch_datas}
    return render(request, 'pages/crm/contacts.html', context)


def get_contact(request, contact_id):
    try:
        contact = Contacts.objects.get(contact_id=contact_id)
        data = {
            "contact_name": contact.contact_name,
            "email": contact.email,
            "phone": contact.phone,
            "address": contact.address,
            "social_profile": contact.social_profile,
            "tags": contact.tags,
            "description": contact.description,
            "visibility": contact.visibility,
            "status": contact.status,
        }
        return JsonResponse({"success": True, "data": data})
    except Contacts.DoesNotExist:
        return JsonResponse({"success": False, "error": "Contact not found."})


def delete_contact(request, contact_id):
    try:
        contact = Contacts.objects.get(contact_id=contact_id)
        
        contact.status = 'N'
        contact.save()
        
        return JsonResponse({"success": True, "message": "Contact has been deactivated."})
    except Contacts.DoesNotExist:
        return JsonResponse({"success": False, "error": "Contact not found."})
    



##### Deals Table #####


def post_deals(request):
    
    if request.method == "POST":
        deal_id = request.POST.get('deal_id')
        deal_name = request.POST.get('deal_name')
        pipeline = request.POST.get('pipeline')
        status = 'Y' if request.POST.get('status') else 'N'
        deal_value = request.POST.get('deal_value')
        currency = request.POST.get('currency')
        period = request.POST.get('period')
        period_value = request.POST.get('period_value')
        due_date = request.POST.get('due_date')
        expected_closingdate = request.POST.get('expected_closingdate')
        follow_up_date = request.POST.get('follow_up_date')
        source = request.POST.get('source')
        tags = request.POST.get('tags')
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        
        
        if deal_id:
            deals = get_object_or_404(Deals, deal_id=deal_id)
            deals.deal_name = deal_name
            deals.pipeline = pipeline
            deals.status = status
            deals.deal_value = deal_value
            deals.currency = currency
            deals.period = period
            deals.period_value = period_value
            deals.due_date = due_date
            deals.expected_closingdate = expected_closingdate
            deals.follow_up_date = follow_up_date
            deals.source = source
            deals.tags = tags
            deals.priority = priority
            deals.description = description
            deals.save()
            
        else:
         Deals.objects.create(
             deal_name=deal_name,
             pipeline = pipeline,
             status = status,
             deal_value = deal_value,
             currency = currency,
             period = period,
             period_value = period_value,
             due_date = due_date,
             expected_closingdate = expected_closingdate,
             follow_up_date = follow_up_date,
             source = source,
             tags = tags,
             priority = priority,
             description = description,
         )
         
        return redirect ('deals')
        
    fetch_deals = Deals.objects.all().order_by('deal_name') ##### to change the orderby field is (createdby) date  
    return render(request,'pages/crm/deals.html',{'fetch_deals':fetch_deals})  
    
    
def get_deals(request, deal_id):
    try:
        deals = get_object_or_404(Deals, deal_id=deal_id)
        
        deal_data = {
            "deal_name" : deals.deal_name,
             "pipeline" : deals.pipeline,
             "status" : deals.status,
             "deal_value" : deals.deal_value,
             "currency" : deals.currency,
             "period" : deals.period,
             "period_value" : deals.period_value,
             "due_date": deals.due_date,
             "expected_closingdate" :deals.expected_closingdate,
             "follow_up_date" : deals.follow_up_date,
             "source" : deals.source,
             "tags" : deals.tags,
             "priority" : deals.priority,
             "description" : deals.description,
        }
        
        return JsonResponse ({"success": True , "deal_data":deal_data})
    except Deals.DoesNotExist:
        return JsonResponse ({"success":False, "error": "Deals Not Found"})
    

def delete_deals(request, deal_id):
    try:
        deals = Deals.objects.get(deal_id=deal_id)
        deals.status = 'N'
        deals.save()
        
        return redirect ('deals')
    except Deals.DoesNotExist:
        return JsonResponse({"success": False, "error": "Deal not found."})



##### Leals Table #####


def leads(request):
    try:
        leads = Leads.objects.all()
        return render(request, 'pages/crm/leads.html', {'leads': leads})
    except Exception as e:
        messages.error(request, f'Error fetching leads: {str(e)}')
        return render(request, 'pages/crm/leads.html', {'leads': []})

def post_leads(request):
    if request.method == "POST":
        try:
            lead_id = request.POST.get('lead_id')
            lead_name = request.POST.get('lead_name')
            lead_type = request.POST.get('lead_type')
            value = request.POST.get('value')
            currency = request.POST.get('currency')
            source = request.POST.get('source')
            industry = request.POST.get('industry')
            tags = request.POST.get('tags')
            description = request.POST.get('description')
            visibility = request.POST.get('visibility')
            status = 'Y' if request.POST.get('status') else 'N'
            
            # Validation
            if not lead_name:
                raise ValidationError("Lead Name is required")
            if not lead_type:
                raise ValidationError("Lead Type is required")
            if not value:
                raise ValidationError("Value is required")
            if not currency:
                raise ValidationError("Currency is required")
            
            if lead_id:
                lead = get_object_or_404(Leads, lead_id=lead_id)
                lead.lead_name = lead_name
                lead.lead_type = lead_type
                lead.value = value
                lead.currency = currency
                lead.source = source
                lead.industry = industry
                lead.tags = tags
                lead.description = description
                lead.visibility = visibility
                lead.status = status
                lead.save()
                messages.success(request, 'Lead updated successfully')
            else:
                Leads.objects.create(
                    lead_name=lead_name,
                    lead_type=lead_type,
                    value=value,
                    currency=currency,
                    source=source,
                    industry=industry,
                    tags=tags,
                    description=description,
                    visibility=visibility,
                    status=status
                )
                messages.success(request, 'Lead created successfully')
            
            return redirect('leads')
            
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('leads')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('leads')
    
    return redirect('leads')

def get_lead(request):
    if request.method == "GET":
        lead_id = request.GET.get('lead_id')
       
        try:
            lead = get_object_or_404(Leads, lead_id=lead_id)
           
            lead_data = {
                'lead_id': lead.lead_id,
                'lead_name': lead.lead_name,
                'lead_type': lead.lead_type,
                'value': str(lead.value),
                'currency': lead.currency,
                'source': lead.source,
                'industry': lead.industry,
                'tags': lead.tags,
                'description': lead.description,
                'visibility': lead.visibility,
                'status': lead.status
            }
           
            return JsonResponse({'success': True, 'lead_data': lead_data})
        except Leads.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Lead not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

def delete_lead(request, lead_id):
    try:
        lead = get_object_or_404(Leads, lead_id=lead_id)
        lead.status = 'N'
        lead.save()
        messages.success(request, 'Lead deactivated successfully')
        return redirect('leads')
    except Leads.DoesNotExist:
        messages.error(request, 'Lead not found')
        return redirect('leads')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('leads')









# from django.http import JsonResponse
# from django.views import View
# from django.shortcuts import get_object_or_404
# from .models import Deals


# class DealsCreate(View):
#     def post(self, request):
#         deals_id = request.POST.get('deals_id', '').strip()

#         if not deals_id:
#             return JsonResponse({'status': 'error', 'field': 'deals_id', 'message': 'Deals ID is required.'})

#         if request.POST.get("check_availability") == "true":
#             if Deals.objects.filter(id=deals_id).exists():
#                 return JsonResponse({'status': 'error', 'field': 'deals_id', 'message': 'Deals ID already exists.'})
#             return JsonResponse({'status': 'success', 'message': 'Deals ID is available.'})

#         try:
#             deals = Deals(
#                 dealid=request.POST.get('dealid'),
#                 dealname=request.POST.get('dealname'),
#                 pipeline=request.POST.get('pipeline'),
#                 status=request.POST.get('status'),
#                 dealvalue=request.POST.get('dealvalue'),
#                 currency=request.POST.get('currency'),
#                 period=request.POST.get('period'),
#                 periodvalue=request.POST.get('periodvalue'),
#                 contactid_id=request.POST.get('contactid_id'),
#                 projectid_id=request.POST.get('projectid_id'),
#                 duedate=request.POST.get('duedate'),
#                 expectedclosingdate=request.POST.get('expectedclosingdate'),
#                 assigneeid_id=request.POST.get('assigneeid_id'),
#                 followupdate=request.POST.get('followupdate'),
#                 source=request.POST.get('source'),
#                 tags=request.POST.get('tags'),
#                 priority=request.POST.get('priority'),
#                 description=request.POST.get('description'),
#             )
#             deals.full_clean()
#             deals.save()
#             return JsonResponse({'status': 'success', 'redirect_url': '/deals/list/'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'field': 'general', 'message': str(e)})

# class DealsUpdate(View):
#     def post(self, request, deals_id):
#         try:
#             deals = get_object_or_404(Deals, id=deals_id)
#             deals.dealid = request.POST.get('dealid')
#             deals.dealname = request.POST.get('dealname')
#             deals.pipeline = request.POST.get('pipeline')
#             deals.status = request.POST.get('status')
#             deals.dealvalue = request.POST.get('dealvalue')
#             deals.currency = request.POST.get('currency')
#             deals.period = request.POST.get('period')
#             deals.periodvalue = request.POST.get('periodvalue')
#             deals.contactid = request.POST.get('contactid')
#             deals.projectid = request.POST.get('projectid')
#             deals.duedate = request.POST.get('duedate')
#             deals.expectedclosingdate = request.POST.get('expectedclosingdate')
#             deals.assigneeid = request.POST.get('assigneeid')
#             deals.followupdate = request.POST.get('followupdate')
#             deals.source = request.POST.get('source')
#             deals.tags = request.POST.get('tags')
#             deals.priority = request.POST.get('priority')
#             deals.description = request.POST.get('description')
#             deals.full_clean()
#             deals.save()
#             return JsonResponse({'status': 'success', 'redirect_url': '/deals/list/'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})

# class DealsDelete(View):
#     def post(self, request, deals_id):
#         deals = get_object_or_404(Deals, id=deals_id)
#         deals.delete()
#         return JsonResponse({'status': 'success', 'message': 'Deals deleted successfully'})






# Create your views here.

# UI Module

def ui_alerts(request):
    return render(request, 'pages/uiinterface/baseui/ui-alerts.html')
 
def ui_accordion(request):
    return render(request, 'pages/uiinterface/baseui/ui-accordion.html')
 
def ui_avatar(request):
    return render(request, 'pages/uiinterface/baseui/ui-avatar.html')
 
def ui_badges(request):
    return render(request, 'pages/uiinterface/baseui/ui-badges.html')
 
def ui_borders(request):
    return render(request, 'pages/uiinterface/baseui/ui-borders.html')
 
def ui_buttons(request):
    return render(request, 'pages/uiinterface/baseui/ui-buttons.html')
 
def ui_buttons_group(request):
    return render(request, 'pages/uiinterface/baseui/ui-buttons-group.html')
 
def ui_breadcrumb(request):
    return render(request, 'pages/uiinterface/baseui/ui-breadcrumb.html')
 
def ui_cards(request):
    return render(request, 'pages/uiinterface/baseui/ui-cards.html')
 
def ui_carousel(request):
    return render(request, 'pages/uiinterface/baseui/ui-carousel.html')
 
def ui_colors(request):
    return render(request, 'pages/uiinterface/baseui/ui-colors.html')
 
def ui_dropdowns(request):
    return render(request, 'pages/uiinterface/baseui/ui-dropdowns.html')
 
def ui_grid(request):
    return render(request, 'pages/uiinterface/baseui/ui-grid.html')
 
def ui_images(request):
    return render(request, 'pages/uiinterface/baseui/ui-images.html')
 
def ui_lightbox(request):
    return render(request, 'pages/uiinterface/baseui/ui-lightbox.html')
 
def ui_media(request):
    return render(request, 'pages/uiinterface/baseui/ui-media.html')
 
def ui_modals(request):
    return render(request, 'pages/uiinterface/baseui/ui-modals.html')
 
def ui_offcanvas(request):
    return render(request, 'pages/uiinterface/baseui/ui-offcanvas.html')
 
def ui_pagination(request):
    return render(request, 'pages/uiinterface/baseui/ui-pagination.html')
 
def ui_popovers(request):
    return render(request, 'pages/uiinterface/baseui/ui-popovers.html')
 
def ui_progress(request):
    return render(request, 'pages/uiinterface/baseui/ui-progress.html')
 
def ui_placeholders(request):
    return render(request, 'pages/uiinterface/baseui/ui-placeholders.html')
 
def ui_spinner(request):
    return render(request, 'pages/uiinterface/baseui/ui-spinner.html')
 
def ui_sweetalerts(request):
    return render(request, 'pages/uiinterface/baseui/ui-sweetalerts.html')
 
def ui_nav_tabs(request):
    return render(request, 'pages/uiinterface/baseui/ui-nav-tabs.html')
 
def ui_toasts(request):
    return render(request, 'pages/uiinterface/baseui/ui-toasts.html')
 
def ui_tooltips(request):
    return render(request, 'pages/uiinterface/baseui/ui-tooltips.html')
 
def ui_typography(request):
    return render(request, 'pages/uiinterface/baseui/ui-typography.html')
 
def ui_video(request):
    return render(request, 'pages/uiinterface/baseui/ui-video.html')
 
# AdvancedUI 
 
def ui_ribbon(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-ribbon.html')
 
def ui_clipboard(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-clipboard.html')
 
def ui_drag_drop(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-drag-drop.html')
 
def ui_rangeslider(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-rangeslider.html')
 
def ui_text_editor(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-text-editor.html')
 
def ui_counter(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-counter.html')
 
def ui_scrollbar(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-scrollbar.html')
 
def ui_stickynote(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-stickynote.html')
 
def ui_timeline(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-timeline.html')
 
# Charts

def chart_apex(request):
    return render(request, 'pages/uiinterface/charts/chart-apex.html')
 
def chart_c3(request):
    return render(request, 'pages/uiinterface/charts/chart-c3.html')
 
def chart_js(request):
    return render(request, 'pages/uiinterface/charts/chart-js.html')
 
def chart_morris(request):
    return render(request, 'pages/uiinterface/charts/chart-morris.html')
 
def chart_flot(request):
    return render(request, 'pages/uiinterface/charts/chart-flot.html')
 
def chart_peity(request):
    return render(request, 'pages/uiinterface/charts/chart-peity.html')
 
 
#Icons

def icon_fontawesome(request):
    return render(request, 'pages/uiinterface/icons/icon-fontawesome.html')
 
def icon_feather(request):
    return render(request, 'pages/uiinterface/icons/icon-feather.html')
 
def icon_ionic(request):
    return render(request, 'pages/uiinterface/icons/icon-ionic.html')
 
def icon_material(request):
    return render(request, 'pages/uiinterface/icons/icon-material.html')
 
def icon_pe7(request):
    return render(request, 'pages/uiinterface/icons/icon-pe7.html')
 
def icon_simpleline(request):
    return render(request, 'pages/uiinterface/icons/icon-simpleline.html')
 
def icon_themify(request):
    return render(request, 'pages/uiinterface/icons/icon-themify.html')

def icon_weather(request):
    return render(request, 'pages/uiinterface/icons/icon-weather.html')
 
def icon_typicon(request):
    return render(request, 'pages/uiinterface/icons/icon-typicon.html')
 
def icon_flag(request):
    return render(request, 'pages/uiinterface/icons/icon-flag.html')

# Forms
 
def form_basic_inputs(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-basic-inputs.html')
 
def form_checkbox_radios(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-checkbox-radios.html')
 
def form_input_groups(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-input-groups.html')
 
def form_grid_gutters(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-grid-gutters.html')
 
def form_select(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-select.html')
 
def form_mask(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-mask.html')
 
def form_fileupload(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-fileupload.html')
 
def form_elements(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-elements.html')
 
def form_horizontal(request):
    return render(request, 'pages/uiinterface/forms/layouts/form-horizontal.html')
 
def form_vertical(request):
    return render(request, 'pages/uiinterface/forms/layouts/form-vertical.html')
 
def form_floating_labels(request):
    return render(request, 'pages/uiinterface/forms/layouts/form-floating-labels.html')
 
def form_validation(request):
    return render(request, 'pages/uiinterface/forms/form-validation.html')
 
def form_select2(request):
    return render(request, 'pages/uiinterface/forms/form-select2.html')
 
def form_wizard(request):
    return render(request, 'pages/uiinterface/forms/form-wizard.html')

#Tables

def tables_basic(request):
    return render(request, 'pages/uiinterface/tables/tables-basic.html')
 
def data_tables(request):
    return render(request, 'pages/uiinterface/tables/data-tables.html')