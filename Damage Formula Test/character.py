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

        self.acc_boost = 1
        self.ev_boost = 1
