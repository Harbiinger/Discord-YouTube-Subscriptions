import main
import npyscreen

class MainForm(npyscreen.ActionFormV2):
    def create(self):
        self.addChannel = self.add(npyscreen.ButtonPress, name="Add", when_pressed_function=self.goToAdd)
        self.deleteChannel = self.add(npyscreen.ButtonPress, name="Delete", when_pressed_function=self.goToDel)
        self.webhook = self.add(npyscreen.ButtonPress, name="Edit webhook", when_pressed_function=self.goToWebhook)

    def goToAdd(self):
        self.parentApp.switchForm('ADD')

    def goToDel(self):
        self.parentApp.switchForm('DEL')

    def goToWebhook(self):
        self.parentApp.switchForm('WEBHOOK')

    def on_cancel(self):
        self.parentApp.switchForm(None)
        

class AddForm(npyscreen.ActionForm):
    def create(self):
        self.channelName = self.add(npyscreen.TitleText, name="Name:")
        self.channelId= self.add(npyscreen.TitleText, name="Id:")

    def on_cancel(self):
        self.channelName.value = ""
        self.channelId.value = ""
        self.parentApp.setNextForm('MAIN')

    def on_ok(self):
        main.add(self.channelName.value, self.channelName.value)
        self.on_cancel()

class DelForm(npyscreen.ActionForm):
    def create(self):
        self.channelName = self.add(npyscreen.TitleText, name="Name:")
        for channel in list(main.getDict().keys())[1:]: 
            self.add(npyscreen.ButtonPress, name=channel)

    def on_cancel(self):
        self.channelName.value = ""
        self.parentApp.setNextForm('MAIN')

    def on_ok(self):
        main.remove(self.channelName.value)
        self.on_cancel()

class WebhookForm(npyscreen.ActionForm):
    def create(self):
        self.webhook = self.add(npyscreen.TitleText, name="Webhook url:")

    def on_cancel(self):
        self.webhook.value = ""
        self.parentApp.setNextForm('MAIN')

    def on_ok(self):
        main.changeWebhook(self.webhook.value)
        self.on_cancel()

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm, name="Ungoogled Youtube Subscriptions")
        self.addForm('ADD', AddForm, name="Ungoogled Youtube Subscriptions")
        self.addForm('DEL', DelForm, name="Ungoogled Youtube Subscriptions")
        self.addForm('WEBHOOK', WebhookForm, name="Ungoogled Youtube Subscriptions")

    
if __name__ == '__main__':
    mainApp = App().run()
