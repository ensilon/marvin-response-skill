from mycroft import MycroftSkill, intent_file_handler


class MarvinResponse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('response.marvin.intent')
    def handle_response_marvin(self, message):
        self.speak_dialog('response.marvin')


def create_skill():
    return MarvinResponse()

