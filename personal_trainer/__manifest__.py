{
    'name': 'Personal Trainer',
    'summary': "Demo data and configuration for Personal Trainer.",
    'description': '''
Personal Trainer
================

    Demo data and configuration for Personal Trainer.

    Features:

        - Demo Data: Ships pre-configured demo data for the industry.
    ''',
    'version': '18.0.1.0.0',
    'category': 'Health and Fitness',
    'depends': [
        'appointment_hr',
        'calendar',
        'knowledge',
        'sale_crm',
        'sale_project',
        'sale_timesheet',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/project_task_type.xml',
        'data/project_tags.xml',
        'data/project_project.xml',
        'data/project_task.xml',
        'data/product_product.xml',
        'data/appointment_type.xml',
        'data/crm_stage.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/crm_lead.xml',
        'demo/calendar_event.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/account_analytic_line.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'personal_trainer/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    'website': 'https://vertel.se/apps/odoo-industry/personal_trainer',
    'images': ['images/main.png'],
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
    ],
}
