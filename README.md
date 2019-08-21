# GLPI API PYTHON

## Usage

from glpi_api.glpi import GlpiApi

session_kill = GlpiApi('USER-TOKEN',
                       'APP-TOKEN', 'SERVER-IP')
                       
print(session_kill.ticket_create('TITLE', 'TEST-DESCRIPTION', '6'))
