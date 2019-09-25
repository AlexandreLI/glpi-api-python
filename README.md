# GLPI API PYTHON

## Usage

from glpi_api.glpi import GlpiApi

ticket = GlpiApi('USER-TOKEN',
                       'APP-TOKEN', 'SERVER-IP')
                       
ticket.ticket_create('TITLE', 'TEST-DESCRIPTION', '6')
