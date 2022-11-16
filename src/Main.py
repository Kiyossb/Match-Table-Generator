import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import challongeAPI
import Setting

class App(tk.Tk) :
    def __init__(self) :
        super().__init__()

        self.title('Match Table Generator')
        self.geometry('800x500')
        

        self.MainFrameWindow = tk.Frame(
            self,
            relief = tk.GROOVE,
            bd = 2,
            )
        self.MainFrameWindow.pack(
            anchor = tk.NW
            )

        
        self.FrameWindow_1 = tk.Frame(
            self.MainFrameWindow,
            relief = tk.RIDGE,
            bd = 2,
            pady = 10,
            padx = 10,
            width = 150,
            height = 496
            )
        self.FrameWindow_1.pack(
            side = tk.LEFT,
            anchor = tk.NW
            )
        self.FrameWindow_1.pack_propagate(0)

        self.labelUserName = tk.Label(
            self.FrameWindow_1,
            text = 'ユーザー名入力'
            )
        self.labelUserName.pack(
            anchor = tk.W
            )
        self.entryUserName = tk.Entry(
            self.FrameWindow_1
            )
        self.entryUserName.pack(
            anchor = tk.W,
            pady = 1
            )

        self.labelAPIKey = tk.Label(
            self.FrameWindow_1,
            text = 'APIキー入力'
            )
        self.labelAPIKey.pack(
            anchor = tk.W
            )
        self.entryAPIKey = tk.Entry(
            self.FrameWindow_1,
            show = '*'
            )
        self.entryAPIKey.pack(
            anchor = tk.W,
            pady = 1
            )

        self.labelTournamentID = tk.Label(
            self.FrameWindow_1,
            text = 'トーナメントID入力'
            )
        self.labelTournamentID.pack(
            anchor = tk.W
            )
        self.entryTournamentID = tk.Entry(
            self.FrameWindow_1
            )
        self.entryTournamentID.pack(
            anchor = tk.W,
            pady = 1
            )

        self.get_challongeButton = tk.Button(
            self.FrameWindow_1,
            text = "対戦カードを取得"
            )
        self.get_challongeButton.pack(
            anchor = tk.E,
            pady = 5
            )
        self.get_challongeButton.bind(
            "<ButtonRelease>",
            self.clickGetChallongeButton
            )

        self.settingButton = tk.Button(
            self.FrameWindow_1,
            text = "設定"
            )
        self.settingButton.pack(
            anchor = tk.SW,
            pady = 5,
            side = tk.BOTTOM
            )
        self.settingButton.bind(
            "<ButtonRelease>",
            self.clickSettingButton
            )


        self.FrameWindow2 = tk.Frame(
            self.MainFrameWindow,
            relief = tk.RIDGE,
            bd = 2,
            pady = 10,
            padx = 10,
            width = 195,
            height = 496
            )
        self.FrameWindow2.pack(
            side = tk.LEFT,
            anchor = tk.NW
            )
        self.FrameWindow2.pack_propagate(0)

        self.FrameWindow2_1 = tk.Frame(
            self.FrameWindow2
            )
        self.FrameWindow2_1.pack(
            anchor = tk.NW
            )

        self.matchCardCanvas = tk.Canvas(
            self.FrameWindow2_1,
            highlightthickness = 0,
            width = 150,
            height = 420
            )
        self.matchCardCanvas.pack(
            anchor = tk.NW,
            side = tk.LEFT
            )

        self.matchCardCanvasScrollbar = tk.Scrollbar(
            self.FrameWindow2_1,
            orient = tk.VERTICAL,
            command = self.matchCardCanvas.yview
            )
        self.matchCardCanvasScrollbar.pack(
            anchor = tk.NW,
            fill = tk.Y,
            side = tk.RIGHT
        )
        self.matchCardCanvas["yscrollcommand"] = self.matchCardCanvasScrollbar.set
        self.matchCardCanvas.yview_moveto(0)
        self.matchNum = 10
        self.matchArrayNum = 9
        self.FrameWindow2_1Height = 42 * self.matchNum
        self.matchCardCanvas.config(scrollregion = (0, 0, 0, self.FrameWindow2_1Height))

        self.FrameWindow2_1_1 = tk.Frame(
            self.matchCardCanvas
            )
        self.FrameWindow2_1_1.pack(
            anchor = tk.NW
            )
        self.matchCardCanvas.create_window(
            0,
            0,
            window = self.FrameWindow2_1_1,
            anchor = tk.NW
            )
        
        self.labelMatchCardComboboxes = []
        self.matchCardComboboxes = []
        self.matchCard = []
        self.matchCard.append("フリー")
        for i in range(self.matchNum):
            self.labelMatchCardComboboxes.insert(
                i,
                tk.Label(
                    self.FrameWindow2_1_1,
                    text = str(i+1) + '番台'
                    )
                )
            self.labelMatchCardComboboxes[i].pack(
                anchor = tk.N
                )
            self.labelMatchCardComboboxes[i].lift()
                
            self.matchCardComboboxes.insert(
                i,
                ttk.Combobox(
                    self.FrameWindow2_1_1,
                    values = self.matchCard
                    )
                )
            self.matchCardComboboxes[i].pack(
                anchor = tk.N
                )
            self.matchCardComboboxes[i].lift()
        
        self.FrameWindow2_2 = tk.Frame(
            self.FrameWindow2,
            pady = 10,
            bd = 2,
            width = 215,
            height = 76
            )

        self.FrameWindow2_2.pack(
            anchor = tk.NW
            )
        self.FrameWindow2_2.pack_propagate(0)

        self.FrameWindow2_2.pack(
            anchor = tk.NW
            )
        self.FrameWindow2_2.pack_propagate(0)

        self.removeMatchCardComboboxesButton = tk.Button(
            self.FrameWindow2_2,
            text = " - "
            )
        self.removeMatchCardComboboxesButton.pack(
            side = tk.LEFT,
            anchor = tk.W
            )
        self.removeMatchCardComboboxesButton.bind(
            "<ButtonRelease>",
            self.removeMatchCardComboboxesClick
            )

        self.insertMatchCardComboboxesButton = tk.Button(
            self.FrameWindow2_2,
            text = " + "
            )
        self.insertMatchCardComboboxesButton.pack(
            side = tk.LEFT,
            anchor = tk.W
            )
        self.insertMatchCardComboboxesButton.bind(
            "<ButtonRelease>",
            self.insertMatchCardComboboxesClick
            )

        self.GetEntryTextButton = tk.Button(
            self.FrameWindow2_2,
            text = 'テキストを出力',
            command = self.GetEntryTextButtonClick
        )
        self.GetEntryTextButton.pack(
            side = tk.BOTTOM,
            anchor = tk.E
            )


        self.FrameWindow3 = tk.Frame(
            self.MainFrameWindow,
            relief = tk.RIDGE,
            bd = 2,
            pady = 10,
            padx = 10,
            width = 451,
            height = 496
            )
        self.FrameWindow3.pack(
            side = tk.LEFT,
            anchor = tk.NW
            )
        self.FrameWindow3.pack_propagate(0)

        i = 1
        j = 1
        self.outputTextBox = tk.Text(
            self.FrameWindow3,
            width = 56,
            height = 35
            )
        for k in range(self.matchNum):

            self.outputTextBox.insert(
                str(i) + '.0',
                str(j) + '番台\n'
                )
            i = i + 1
            self.outputTextBox.insert(
                str(i)+'.0',
                'フリー\n'
                )
            i = i + 1
            j = j + 1
        self.outputTextBox.pack(
            anchor = tk.W,
            side = tk.LEFT
            )
        self.outputTextBoxScrollbar = tk.Scrollbar(
            self.FrameWindow3,
            orient = tk.VERTICAL,
            command = self.outputTextBox.yview
            )
        self.outputTextBoxScrollbar.pack(
            anchor = tk.NW,
            fill = tk.Y,
            side = tk.RIGHT
            )
        self.outputTextBox["yscrollcommand"] = self.outputTextBoxScrollbar.set
        self.outputTextBox.yview_moveto(0)


    def clickGetChallongeButton(self, event):
        self.userName = self.entryUserName.get()
        self.APIKey = self.entryAPIKey.get()
        self.tournamentID = self.entryTournamentID.get()
        self.matchCardName = challongeAPI.API(self.userName, self.APIKey, self.tournamentID)
        self.matchCard = self.matchCardNameConvert(self.matchCardName)
        self.displayMatchCardComboboxesFlg = 0
        self.createMatchCardComboboxes(self.matchNum, self.matchCard)
        return self.matchCard
    
    def matchCardNameConvert(self, matchCardName):
        self.matchCard = []
        self.matchCard.append("フリー")
        for card in self.matchCardName.values():
            self.matchCard.append(card["player1_name"] + "vs" + card["player2_nema"])
        return self.matchCard

    def createMatchCardComboboxes(self, matchNum, matchCard):
        if self.displayMatchCardComboboxesFlg == 0:
            for i in range(self.matchNum):
                self.matchCardComboboxes[i].destroy()
                self.labelMatchCardComboboxes[i].destroy()

            self.matchCardComboboxes = []
            self.labelMatchCardComboboxes = []

            for i in range(self.matchNum):
                self.labelMatchCardComboboxes.insert(
                    i,
                    tk.Label(
                        self.FrameWindow2_1_1,
                        text = str(i+1) + '番台'
                        )
                    )
                self.labelMatchCardComboboxes[i].pack(
                    anchor = tk.N
                    )
                self.labelMatchCardComboboxes[i].lift()
                
                self.matchCardComboboxes.insert(
                    i,
                    ttk.Combobox(
                        self.FrameWindow2_1_1,
                        values=self.matchCard
                        )
                    )
                self.matchCardComboboxes[i].pack(
                    anchor = tk.N
                    )
                self.matchCardComboboxes[i].lift()
                
        elif self.displayMatchCardComboboxesFlg == 1:
            self.FrameWindow2_1Height = 42 * self.matchNum
            self.matchCardCanvas.config(scrollregion = (0, 0, 0, self.FrameWindow2_1Height))

            self.labelMatchCardComboboxes.insert(
                self.matchArrayNum,
                tk.Label(
                    self.FrameWindow2_1_1,
                    text = str(self.matchNum) + '番台'
                    )
                )
            self.labelMatchCardComboboxes[self.matchArrayNum].pack(
                anchor = tk.N
                )
            self.labelMatchCardComboboxes[self.matchArrayNum].lift()
            
            self.matchCardComboboxes.insert(
                self.matchArrayNum,
                ttk.Combobox(
                    self.FrameWindow2_1_1,
                    values = self.matchCard
                    )
                )
            self.matchCardComboboxes[self.matchArrayNum].pack(
                anchor = tk.N
                )
            self.matchCardComboboxes[self.matchArrayNum].lift()

        elif self.displayMatchCardComboboxesFlg == 2:
            if self.matchNum == 0:
                self.matchNum = 1
                self.matchArrayNum = 0
            else:
                self.FrameWindow2_1Height = 42 * self.matchNum
                self.matchCardCanvas.config(scrollregion = (0, 0, 0, self.FrameWindow2_1Height))
                
                self.labelMatchCardComboboxes[self.matchNum].destroy()
                self.labelMatchCardComboboxes.pop(
                    self.matchNum
                    )

                self.matchCardComboboxes[self.matchNum].destroy()
                self.matchCardComboboxes.pop(
                    self.matchNum
                    )

    def clickSettingButton(self, event):
        Setting.SettingWindow()
    
    def removeMatchCardComboboxesClick(self, event) :
        self.matchNum = self.matchNum -1
        self.matchArrayNum = self.matchArrayNum - 1
        self.displayMatchCardComboboxesFlg = 2

        self.createMatchCardComboboxes(self.matchNum, self.matchCard)
                
    def insertMatchCardComboboxesClick(self, event) :
        self.matchNum = self.matchNum + 1
        self.matchArrayNum = self.matchArrayNum + 1
        self.displayMatchCardComboboxesFlg = 1

        self.createMatchCardComboboxes(self.matchNum, self.matchCard)

    def GetEntryTextButtonClick(self) :
        self.GetComboboxes = []

        for i in range(len(self.matchCardComboboxes)) :
            self.GetComboboxes.append(self.matchCardComboboxes[i].get())

        self.displayOutputTextBox(self.GetComboboxes)

    def displayOutputTextBox(self, GetComboboxes):
        self.outputTextBox.delete(
            0.,
            tk.END
            )
        self.outputTextBox.destroy()
        i = 1
        j = 1
        self.outputTextBox = tk.Text(
            self.FrameWindow3,
            width = 56,
            height = 35
            )
        for card in self.GetComboboxes:
            self.outputTextBox.insert(
                str(i)+'.0',
                str(j) + '番台\n'
                )
            i = i + 1
            self.outputTextBox.insert(
                str(i)+'.0',
                card + '\n'
                )
            i = i + 1
            j = j + 1
        self.outputTextBox.pack(
            anchor = tk.W,
            side = tk.LEFT
            )

        self.outputTextBoxScrollbar.destroy()
        self.outputTextBoxScrollbar = tk.Scrollbar(
            self.FrameWindow3,
            orient = tk.VERTICAL,
            command = self.outputTextBox.yview
            )
        self.outputTextBoxScrollbar.pack(
            anchor = tk.NW,
            fill = tk.Y,
            side = tk.RIGHT
            )
        self.outputTextBox["yscrollcommand"] = self.outputTextBoxScrollbar.set
        self.outputTextBox.yview_moveto(0)

        self.copyText()

    def copyText(self):
        outputText = self.outputTextBox.get(
            0.,
            tk.END
            )
        self.clipboard_clear()
        self.clipboard_append(outputText)



if __name__ == '__main__' :
    app = App()
    app.mainloop()