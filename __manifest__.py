# -*- coding: utf-8 -*-
{
    'name': "lol_esports",

    'summary': """
        Module to manage League of Legends esports""",

    'description': """
        Module to manage information about the League of Legends esports scene, leagues, teams, players, etc.
    """,

    'author': "Roger Roque",
    'website': "https://lolesports.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Deportes electronicos',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
	'reports/report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
