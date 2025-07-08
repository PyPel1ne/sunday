"""

MAIN.PY runs the application starting with login dashboard

"""

from msilib.schema import AdminExecuteSequence
from view.dashboards.system_dashboards import Login_Dashboard


dashboard = Login_Dashboard()
dashboard.login_dashboard()