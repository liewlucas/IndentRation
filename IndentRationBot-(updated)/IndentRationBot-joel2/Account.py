class Account:

    def __init__(self, chat_id, username, password, pin):
        self.chat_id = chat_id
        self.username = username
        self.password = password
        self.pin = pin

    def __repr__(self):
        return "Account('{}', '{}', '{}', '{}')".format(self.chat_id, self.username, self.password, self.pin)
class rationoptions:

    def __init__(self, chat_id, MON53L, MON53D, MON200L, MON200D, TUE53L, TUE53D, TUE200L, TUE200D, WED53L, WED53D, WED200L, WED200D, THU53L, THU53D, THU200L, THU200D, FRI53L, FRI53D, FRI200L, FRI200D, SAT53L, SAT53D, SUN53L, SUN53D):
        self.chat_id = chat_id
        self.MON53L = MON53L
        self.MON53D = MON53D
        self.MON200L = MON200L
        self.MON200D = MON200D
        self.TUE53L = TUE53L
        self.TUE53D = TUE53D
        self.TUE200L = TUE200L
        self.TUE200D = TUE200D
        self.WED53L = WED53L
        self.WED53D = WED53D
        self.WED200L = WED200L
        self.WED200D = WED200D
        self.THU53L = THU53L
        self.THU53D = THU53D
        self.THU200L = THU200L
        self.THU200D = THU200D
        self.FRI53L = FRI53L
        self.FRI53D = FRI53D
        self.FRI200L = FRI200L
        self.FRI200D = FRI200D
        self.SAT53L = SAT53L
        self.SAT53D = SAT53D
        self.SUN53L = SUN53L
        self.SUN53D = SUN53D


    def __repr__(self):
        return "rationoptions('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',)".format(self.chat_id, self.MON53L, self.MON53D, self.MON200L, self.MON200D, self.TUE53L, self.TUE53D, self.TUE200L, self.TUE200D, self.WED53L, self.WED53D,
                                                                                                                                                               self.WED200L, self.WED200D, self.THU53L, self.THU53D, self.THU200L, self.THU200D, self.FRI53L, self.FRI53D, self.FRI200L, self.FRI200D,
                                                                                                                                                               self.SAT53L, self.SAT53D, self.SUN53L, self.SUN53D,)