import wx

class CaesarCipherApp(wx.Frame):
    def __init__(self, parent, title):
        super(CaesarCipherApp, self).__init__(parent, title=title, size=(400, 300))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        shift_sizer = wx.BoxSizer(wx.HORIZONTAL)
        shift_label = wx.StaticText(panel, label="Shift:")
        self.shift_ctrl = wx.TextCtrl(panel)
        shift_sizer.Add(shift_label, 0, wx.ALL, 5)
        shift_sizer.Add(self.shift_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        message_sizer = wx.BoxSizer(wx.HORIZONTAL)
        message_label = wx.StaticText(panel, label="Message:")
        self.message_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        message_sizer.Add(message_label, 0, wx.ALL, 5)
        message_sizer.Add(self.message_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        result_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_label = wx.StaticText(panel, label="Result:")
        self.result_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        result_sizer.Add(result_label, 0, wx.ALL, 5)
        result_sizer.Add(self.result_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        encrypt_button = wx.Button(panel, label="Encrypt")
        decrypt_button = wx.Button(panel, label="Decrypt")
        encrypt_button.Bind(wx.EVT_BUTTON, self.on_encrypt)
        decrypt_button.Bind(wx.EVT_BUTTON, self.on_decrypt)
        button_sizer.Add(encrypt_button, 0, wx.ALL, 5)
        button_sizer.Add(decrypt_button, 0, wx.ALL, 5)

        sizer.Add(shift_sizer, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(message_sizer, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(result_sizer, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(button_sizer, 0, wx.ALL | wx.ALIGN_CENTER, 5)

        panel.SetSizer(sizer)

    def on_encrypt(self, event):
        shift = int(self.shift_ctrl.GetValue())
        message = self.message_ctrl.GetValue()
        encrypted_message = ""

        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char

        self.result_ctrl.SetValue(encrypted_message)

    def on_decrypt(self, event):
        shift = int(self.shift_ctrl.GetValue())
        message = self.message_ctrl.GetValue()
        decrypted_message = ""

        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - shift + 26) % 26 + ascii_offset)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char

        self.result_ctrl.SetValue(decrypted_message)

if __name__ == "__main__":
    app = wx.App()
    CaesarCipherApp(None, title="Caesar Cipher")
    app.MainLoop()
