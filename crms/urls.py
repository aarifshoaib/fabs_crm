"""
URL configuration for crms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps import views as app_views 
from components import views as components_views 
from dashboard import views as dashboard_views
from django.urls import path




urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboard
    
    path('index', dashboard_views.index, name='index'),
    path('leads-dashboard', dashboard_views.leads_dashboard, name='leads_dashboard'),
    path('project-dashboard', dashboard_views.project_dashboard, name='project_dashboard'),
    
    # Authentication

    path('', app_views.login, name='login'),
    path('register', app_views.register, name='register'),
    path('forgot-password', app_views.forgot_password, name='forgot_password'),
    path('reset-password', app_views.reset_password, name='reset_password'),
    path('email-verification', app_views.email_verification, name='email_verification'),
    path('two-step-verification', app_views.two_step_verification, name='two_step_verification'),
    path('lock-screen', app_views.lock_screen, name='lock_screen'),
    path('success', app_views.success, name='success'),
    
    # pages
    
    path('error-404', app_views.error_404, name="error_404"),
    path('error-500', app_views.error_500, name="error_500"),
    path('coming-soon', app_views.coming_soon, name="coming_soon"),
    path('blank-page', app_views.blank_page, name="blank_page"),
    path('under-maintenance', app_views.under_maintenance, name="under_maintenance"),
    
    # Reports
    
    path('lead-reports' ,app_views.lead_reports ,name='lead_reports'),
    path('deal-reports' ,app_views.deal_reports ,name='deal_reports'),
    path('contact-reports' ,app_views.contact_reports ,name='contact_reports'),
    path('company-reports' ,app_views.company_reports ,name='company_reports'),
    path('project-reports' ,app_views.project_reports ,name='project_reports'),
    path('task-reports' ,app_views.task_reports ,name='task_reports'),
    
    # Settings
    
    path('profile', app_views.profile, name='profile'),
    path('security', app_views.security, name='security'),
    path('notifications', app_views.notifications, name='notifications'),
    path('connected-apps', app_views.connected_apps, name='connected_apps'),
    
    path('company-settings', app_views.company_settings, name='company_settings'),
    path('localization', app_views.localization, name='localization'),
    path('prefixes', app_views.prefixes, name='prefixes'),
    path('preference', app_views.preference, name='preference'),
    path('appearance', app_views.appearance, name='appearance'),
    path('language', app_views.language, name='language'),
    path('language-web', app_views.language_web, name='language_web'),
    
    path('invoice-settings', app_views.invoice_settings, name='invoice_settings'),
    path('printers', app_views.printers, name='printers'),
    path('custom-fields', app_views.custom_fields, name='custom_fields'),
    
    path('email-settings', app_views.email_settings, name='email_settings'),
    path('sms-gateways', app_views.sms_gateways, name='sms_gateways'),
    path('gdpr-cookies', app_views.gdpr_cookies, name='gdpr_cookies'),
    
    path('payment-gateways', app_views.payment_gateways, name='payment_gateways'),
    path('bank-accounts', app_views.bank_accounts, name='bank_accounts'),
    path('tax-rates', app_views.tax_rates, name='tax_rates'),
    path('currencies', app_views.currencies, name='currencies'),
    
    path('storage', app_views.storage, name='storage'),
    path('ban-ip-address', app_views.ban_ip_address, name='ban_ip_address'),
    
    # Supports
    
    path('tickets' , app_views.tickets, name='tickets'),
    path('contact-messages' , app_views.contact_messages, name='contact_messages'),
    
    # Pages
    
    path('pages' , app_views.pages, name='pages'),
    path('countries' , app_views.countries, name='countries'),
    path('states' , app_views.states, name='states'),
    path('cities' , app_views.cities, name='cities'),
    path('testimonials' , app_views.testimonials, name='testimonials'),
    path('faq' , app_views.faq, name='faq'),
    
    # Membership
    
    path('membership-plans' , app_views.membership_plans, name='membership_plans'),
    path('membership-addons' , app_views.membership_addons, name='membership_addons'),
    path('membership-transactions' , app_views.membership_transactions, name='membership_transactions'),
    
    # User Management
    
    path('manage-users' , app_views.manage_users, name='manage_users'),
    path('roles-permissions' , app_views.roles_permissions, name='roles_permissions'),
    path('permission' , app_views.permission, name='permission'),
    path('delete-request' , app_views.delete_request, name='delete_request'),
    
    # CRM Settings
    path('sources', app_views.sources, name='sources'),
    path('lost-reason', app_views.lost_reason, name='lost_reason'),
    path('contact-stage', app_views.contact_stage, name='contact_stage'),
    path('industry', app_views.industry, name='industry'),
    path('calls', app_views.calls, name='calls'),
    
    # UI Module
    
    path('ui-alerts', components_views.ui_alerts, name='ui_alerts'),
    path('ui-accordion', components_views.ui_accordion, name='ui_accordion'),
    path('ui-avatar', components_views.ui_avatar, name='ui_avatar'),
    path('ui-badges', components_views.ui_badges, name='ui_badges'),
    path('ui-borders', components_views.ui_borders, name='ui_borders'),
    path('ui-buttons', components_views.ui_buttons, name='ui_buttons'),
    path('ui-buttons-group', components_views.ui_buttons_group, name='ui_buttons_group'),
    path('ui-breadcrumb', components_views.ui_breadcrumb, name='ui_breadcrumb'),
    path('ui-cards', components_views.ui_cards, name='ui_cards'),
    path('ui-carousel', components_views.ui_carousel, name='ui_carousel'),
    path('ui-colors', components_views.ui_colors, name='ui_colors'),
    path('ui-dropdowns', components_views.ui_dropdowns, name='ui_dropdowns'),
    path('ui-grid', components_views.ui_grid, name='ui_grid'),
    path('ui-images', components_views.ui_images, name='ui_images'),
    path('ui-lightbox', components_views.ui_lightbox, name='ui_lightbox'),
    path('ui-media', components_views.ui_media, name='ui_media'),
    path('ui-modals', components_views.ui_modals, name='ui_modals'),
    path('ui-offcanvas', components_views.ui_offcanvas, name='ui_offcanvas'),
    path('ui-pagination', components_views.ui_pagination, name='ui_pagination'),
    path('ui-popovers', components_views.ui_popovers, name='ui_popovers'),
    path('ui-progress', components_views.ui_progress, name='ui_progress'),
    path('ui-placeholders', components_views.ui_placeholders, name='ui_placeholders'),
    path('ui-spinner', components_views.ui_spinner, name='ui_spinner'),
    path('ui-sweetalerts', components_views.ui_sweetalerts, name='ui_sweetalerts'),
    path('ui-nav-tabs', components_views.ui_nav_tabs, name='ui_nav_tabs'),
    path('ui-toasts', components_views.ui_toasts, name='ui_toasts'),
    path('ui-tooltips', components_views.ui_tooltips, name='ui_tooltips'),
    path('ui-typography', components_views.ui_typography, name='ui_typography'),
    path('ui-video', components_views.ui_video, name='ui_video'),
        
    # Advanced UI  
    
    path('ui-ribbon', components_views.ui_ribbon, name='ui_ribbon'),
    path('ui-clipboard', components_views.ui_clipboard, name='ui_clipboard'),
    path('ui-drag-drop', components_views.ui_drag_drop, name='ui_drag_drop'),
    path('ui-rangeslider', components_views.ui_rangeslider, name='ui_rangeslider'),
    path('ui-text-editor', components_views.ui_text_editor, name='ui_text_editor'),
    path('ui-counter', components_views.ui_counter, name='ui_counter'),
    path('ui-scrollbar', components_views.ui_scrollbar, name='ui_scrollbar'),
    path('ui-stickynote', components_views.ui_stickynote, name='ui_stickynote'),
    path('ui-timeline', components_views.ui_timeline, name='ui_timeline'),
    
    #Charts
    
    path('chart-apex', components_views.chart_apex, name='chart_apex'),
    path('chart-c3', components_views.chart_c3, name='chart_c3'),
    path('chart-js', components_views.chart_js, name='chart_js'),
    path('chart-morris', components_views.chart_morris, name='chart_morris'),
    path('chart-flot', components_views.chart_flot, name='chart_flot'),
    path('chart-peity', components_views.chart_peity, name='chart_peity'),
    
    #Icons
    
    path('icon-fontawesome', components_views.icon_fontawesome, name='icon_fontawesome'),
    path('icon-feather', components_views.icon_feather, name='icon_feather'),
    path('icon-ionic', components_views.icon_ionic, name='icon_ionic'),
    path('icon-material', components_views.icon_material, name='icon_material'),
    path('icon-pe7', components_views.icon_pe7, name='icon_pe7'),
    path('icon-simpleline', components_views.icon_simpleline, name='icon_simpleline'),
    path('icon-themify', components_views.icon_themify, name='icon_themify'),
    path('icon-weather', components_views.icon_weather, name='icon_weather'),
    path('icon-typicon', components_views.icon_typicon, name='icon_typicon'),
    path('icon-flag', components_views.icon_flag, name='icon_flag'),
    
    #Forms
    
    path('form-basic-inputs', components_views.form_basic_inputs, name='form_basic_inputs'),
    path('form-checkbox-radios', components_views.form_checkbox_radios, name='form_checkbox_radios'),
    path('form-input-groups', components_views.form_input_groups, name='form_input_groups'),
    path('form-grid-gutters', components_views.form_grid_gutters, name='form_grid_gutters'),
    path('form-select', components_views.form_select, name='form_select'),
    path('form-mask', components_views.form_mask, name='form_mask'),
    path('form-fileupload', components_views.form_fileupload, name='form_fileupload'),
    path('form-elements', components_views.form_elements, name='form_elements'),
    path('form-horizontal', components_views.form_horizontal, name='form_horizontal'),
    path('form-vertical', components_views.form_vertical, name='form_vertical'),
    path('form-floating-labels', components_views.form_floating_labels, name='form_floating_labels'),
    path('form-validation', components_views.form_validation, name='form_validation'),
    path('form-select2', components_views.form_select2, name='form_select2'),
    path('form-wizard', components_views.form_wizard, name='form_wizard'),
    
    # Tables
    
    path('tables-basic', components_views.tables_basic, name='tables_basic'),
    path('data-tables', components_views.data_tables, name='data_tables'),

    #   Application

    path('chat', app_views.chat, name='chat'),
    path('video-call', app_views.video_call, name='video_call'),
    path('audio-call', app_views.audio_call, name='audio_call'),
    path('call-history', app_views.call_history, name='call_history'),
    path('calendar', app_views.calendar, name='calendar'),
    path('email', app_views.email, name='email'),
    path('todo', app_views.todo, name='todo'),
    path('notes', app_views.notes, name='notes'),
    path('file-manager', app_views.file_manager, name='file_manager'),

    #   CRM

    ###########   Contacts     ########### 
    path('contacts', components_views.post_contact, name='contacts'),
    path('get_contact/<int:contact_id>/', components_views.get_contact, name='get_contact'),
    path('delete_contact/<int:contact_id>/', components_views.delete_contact, name='delete_contact'),
    
    
    path('contact-grid', app_views.contact_grid, name='contact_grid'),
    path('contact-details', app_views.contact_details, name='contact_details'),
    path('companies', app_views.companies, name='companies'),
    path('companies-grid', app_views.companies_grid, name='companies_grid'),
    path('company-details', app_views.company_details, name='company_details'),
    
    ###########   Deals     ########### 
    path('deals', components_views.post_deals,name='deals'),
    path('get_deals/<int:deal_id>/', components_views.get_deals, name='get_deals'),
    path('delete_deals/<int:deal_id>/', components_views.delete_deals, name='delete_deals'),
    
    
    path('deals-kanban', app_views.deals_kanban, name='deals_kanban'),
    path('deals-details', app_views.deals_details, name='deals_details'),
    
    
    ###########   Leals     ########### 
   path('leads/', components_views.leads, name='leads'),
    path('leads/post/', components_views.post_leads, name='post_leads'),
    path('get_lead', components_views.get_lead, name='get_lead'),
    path('leads/delete/<int:lead_id>/', components_views.delete_lead, name='delete_lead'),
    
    path('leads-kanban', app_views.leads_kanban, name='leads_kanban'),
    path('leads-details', app_views.leads_details, name='leads_details'),
    path('pipeline', app_views.pipeline, name='pipeline'),
    path('campaign', app_views.campaign, name='campaign'),
    path('campaign-complete', app_views.campaign_complete, name='campaign_complete'),
    path('campaign-archieve', app_views.campaign_archieve, name='campaign_archieve'),
    path('projects', app_views.projects, name='projects'),
    path('project-grid', app_views.project_grid, name='project_grid'),
    path('project-details', app_views.project_details, name='project_details'),
    path('tasks', app_views.tasks, name='tasks'),
    path('tasks-important', app_views.tasks_important, name='tasks_important'),
    path('tasks-completed', app_views.tasks_completed, name='tasks_completed'),
    path('proposals', app_views.proposals, name='proposals'),
    path('proposals-grid', app_views.proposals_grid, name='proposals_grid'),
    path('contracts', app_views.contracts, name='contracts'),
    path('contracts-grid', app_views.contracts_grid, name='contracts_grid'),
    path('estimations', app_views.estimations, name='estimations'),
    path('estimations-kanban', app_views.estimations_kanban, name='estimations_kanban'),
    path('invoices', app_views.invoices, name='invoices'),
    path('invoice-grid', app_views.invoice_grid, name='invoice_grid'),
    path('payments', app_views.payments, name='payments'),
    path('analytics', app_views.analytics, name='analytics'),
    path('activities', app_views.activities, name='activities'),
    path('activity-calls', app_views.activity_calls, name='activity_calls'),
    path('activity-mail', app_views.activity_mail, name='activity_mail'),
    path('activity-task', app_views.activity_task, name='activity_task'),
    path('activity-meeting', app_views.activity_meeting, name='activity_meeting'),

]
