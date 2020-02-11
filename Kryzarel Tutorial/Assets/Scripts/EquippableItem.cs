using UnityEngine;

public enum EquipmentType {
	BODYWEAR,
	FOOTWEAR,
	WEAPON,
	ACCESSORY
}

[CreateAssetMenu]
public class EquippableItem : Item {
	public int HealthBonus;
	public int MysticPowerBonus;
	public int StrengthBonus;
	public int DefenseBonus;
	public int MysticStrengthBonus;
	public int FortitudeBonus;
	[Space]
	public float SpeedPercentBonus;
	public float EndurancePercentBonus;
	public float LuckPercentBonus;
	public float CharismaPercentBonus;
	[Space]
	public EquipmentType EquipmentType;

	public void Equip (Character character) {
		if (HealthBonus != 0) {
			character.Health.AddModifier(new StatModifier(HealthBonus, StatModifierType.NUMBER, this));
		}
		if (MysticPowerBonus != 0) {
			character.MysticPower.AddModifier(new StatModifier(MysticPowerBonus, StatModifierType.NUMBER, this));
		}
		if (StrengthBonus != 0) {
			character.Strength.AddModifier(new StatModifier(StrengthBonus, StatModifierType.NUMBER, this));
		}
		if (DefenseBonus != 0) {
			character.Defense.AddModifier(new StatModifier(DefenseBonus, StatModifierType.NUMBER, this));
		}
		if (MysticStrengthBonus != 0) {
			character.MysticStrength.AddModifier(new StatModifier(MysticStrengthBonus, StatModifierType.NUMBER, this));
		}
		if (FortitudeBonus != 0) {
			character.Fortitude.AddModifier(new StatModifier(FortitudeBonus, StatModifierType.NUMBER, this));
		}

		if (SpeedPercentBonus != 0) {
			character.Speed.AddModifier(new StatModifier(SpeedPercentBonus, StatModifierType.PERCENT_ADD, this));
		}
		if (EndurancePercentBonus != 0) {
			character.Endurance.AddModifier(new StatModifier(EndurancePercentBonus, StatModifierType.PERCENT_ADD, this));
		}
		if (LuckPercentBonus != 0) {
			character.Luck.AddModifier(new StatModifier(LuckPercentBonus, StatModifierType.PERCENT_ADD, this));
		}
		if (CharismaPercentBonus != 0) {
			character.Charisma.AddModifier(new StatModifier(CharismaPercentBonus, StatModifierType.PERCENT_ADD, this));
		}
	}

	public void Unequip (Character character) {
		character.Health.RemoveAllModifiersFromSource(this);
		character.MysticPower.RemoveAllModifiersFromSource(this);
		character.Strength.RemoveAllModifiersFromSource(this);
		character.Defense.RemoveAllModifiersFromSource(this);
		character.MysticStrength.RemoveAllModifiersFromSource(this);
		character.Fortitude.RemoveAllModifiersFromSource(this);
		character.Speed.RemoveAllModifiersFromSource(this);
		character.Endurance.RemoveAllModifiersFromSource(this);
		character.Luck.RemoveAllModifiersFromSource(this);
		character.Charisma.RemoveAllModifiersFromSource(this);
	}
}
