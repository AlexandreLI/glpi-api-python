import requests


class GlpiApi:
    def __init__(self, user_token, app_token, server):
        self.user_token = user_token
        self.app_token = app_token
        self.server = server

    def init_session(self):
        header = {'Content-Type': 'application/json',
                  'Authorization': 'user_token %s' % self.user_token,
                  'App-Token': '%s' % self.app_token}
        session = requests.get('https://{}/apirest.php/initSession/'.format(self.server),
                               headers=header, verify=False)
        session_token = session.json()['session_token']
        return session_token

    def kill_session(self):
        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        session = requests.get('https://{}/apirest.php/killSession/'.format(self.server),
                               headers=header, verify=False)
        return session.status_code

    def ticket_create(self, title, desc, priority):

        title = title
        description = desc
        priority = priority

        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        payload = {"input": {"name": "%s" % title,
                             "content": "%s" % description,
                             "priority": "%s" % priority}}
        session = requests.post('https://{}/apirest.php/Ticket'.format(self.server), headers=header,
                                json=payload, verify=False)
        return session




