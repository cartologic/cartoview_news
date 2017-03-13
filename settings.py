# this file is excuted from cartoview.app_manager.settings using exec_file
import os
import sys
import cartoview_news
app_folder = os.path.dirname(cartoview_news.__file__)
sys.path.append(os.path.join(app_folder, 'libs'))
INSTALLED_APPS += ('crispy_forms',)
CRISPY_TEMPLATE_PACK = 'bootstrap3'
