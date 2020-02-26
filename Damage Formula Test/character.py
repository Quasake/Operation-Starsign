class Character:
    def __init__ (self, name, hp, mp, s, d, ms, f, sp, e, l, c):
        self.name = name

        self.hp = hp
        self.mp = mp
        self.s = s
        self.d = d
        self.ms = ms
        self.f = f
        self.sp = sp
        self.e = e

        self.l = l
        self.c = c

        self.stamina = 100
        self.curr_sp = 100
        self.curr_hp = self.hp

        self.acc_boost = 1
        self.ev_boost = 1

    def regain_speed (self):
        if self.curr_sp == 100:
            return

        self.curr_sp += (10.0 / 11.0) * self.sp
        if self.curr_sp > 100:
            self.curr_sp = 100
