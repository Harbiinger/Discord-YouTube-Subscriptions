import npyscreen

class myForm(npyscreen.ActionForm):
    def create(self):
        self.name = self.add(npyscreen.TitleText, name='Channel name:')
        self.id = self.add(npyscreen.TitleText, name='Channel id:')

def myFunction(*args):
    F = myForm(name = "Ungoogled YouTube subscription")
    F.edit()
    return [F.name.value, F.id.value]

if __name__ == '__main__':
    new_channel = npyscreen.wrapper_basic(myFunction)
    f = open("subscriptions.txt", 'a')
    f.write(new_channel[0] + "€" + new_channel[1] + "\n")
    f.close()

