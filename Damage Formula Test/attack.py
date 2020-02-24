import random
import math

CRIT = 1.5

class Attack:
    def __init__ (self, name, dmg, acc, dmg_rat):
        self.name = name

        self.dmg = dmg

        self.acc = acc
        self.dmg_rat = dmg_rat

    def calc_damage (self, attacker, defender):
        acc_mod = self.__calc_acc_mod(attacker, defender)
        luck_mod = self.__calc_luck_mod(attacker)
        charisma_mod = self.__calc_charisma_mod(attacker)
        stamina_mod = self.__calc_stamina_mod(attacker)
        bonus_mod = self.__calc_bonus_mod(attacker, defender)
        base_dmg = self.__calc_base_damage(attacker, defender)

        # print('ACC: ' + str(acc_mod))
        # print('LUC: ' + str(luck_mod))
        # print('CHA: ' + str(charisma_mod))
        # print('STA: ' + str(stamina_mod))
        # print('BON: ' + str(bonus_mod))
        # print('BASE: ' + str(base_dmg))

        # total_dmg = acc_mod * round(((stamina_mod * bonus_mod * base_dmg) + charisma_mod) * luck_mod)
        total_dmg = acc_mod * (((stamina_mod * bonus_mod * base_dmg) + charisma_mod) * luck_mod)

        return total_dmg

    def __calc_luck_mod (self, attacker):
        multiplier = CRIT if random.random() <= attacker.l / 100.0 else 1
        
        return multiplier

    def __calc_charisma_mod (self, attacker):
        if self.dmg_rat > 0:
            char_range = attacker.s / 7.5

            min_bound = -char_range + ((attacker.c / 100.0) * char_range)
            max_bound = char_range - ((1 - (attacker.c / 100.0)) * char_range)

            return random.uniform(min_bound, max_bound)

        return 0

    def __calc_acc_mod (self, attacker, defender):
        boost_rat = attacker.acc_boost / defender.ev_boost
        speed_rat = (1.5 * attacker.sp) / defender.sp

        return 1 if random.random() < boost_rat * speed_rat * self.acc else 0

    def __calc_stamina_mod (self, attacker):
        return 0.25 * math.ceil(attacker.stamina / 25.0)

    def __calc_bonus_mod (self, attacker, defender):
        return 1

    def __calc_base_damage (self, attacker, defender):
        att_rat = (attacker.s * self.dmg_rat) + (attacker.ms * (1 - self.dmg_rat))
        def_rat = (defender.d * self.dmg_rat) + (defender.f * (1 - self.dmg_rat))

        full_dmg = self.dmg * (att_rat / def_rat)

        return full_dmg if full_dmg > 0 else 0
