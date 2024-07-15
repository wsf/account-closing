{
    "name": "Skyloom Fiscal year closing",
    "summary": "Generic fiscal year closing wizard",
    "version": "13.0",
    "license": "",
    "category": "Accounting & Finance",
    "installable": True,
    "depends": [
        "account",
    ],
    "data": [
        # "security/account_fiscalyear_closing_security.xml",
        "security/ir.model.access.csv",
        "views/account_fiscalyear_closing_views.xml",
        "views/account_fiscalyear_closing_template_views.xml",
        "views/account_move_views.xml",
        "wizards/account_fiscal_year_closing_unbalanced_move_views.xml",
    ],
}
