using UnityEngine;

public enum EquipmentType {
	BODYWEAR,
	FOOTWEAR,
	WEAPON,
	ACCESSORY
}

[CreateAssetMenu]
public class Item : ScriptableObject {
	public string ItemName;
	public Sprite Icon;

	[Space]
	public int HealthBonus;
	public int MysticPowerBonus;
	public int StrengthBonus;
	public int DefenseBonus;
	public int MysticStrengthBonus;
	public int FortitudeBonus;
	public int SpeedBonus;
	public int EnduranceBonus;
	public int LuckBonus;
	public int CharismaBonus;
	[Space]
	public float HealthPercentBonus;
	public float MysticPowerPercentBonus;
	public float StrengthPercentBonus;
	public float DefensePercentBonus;
	public float MysticStrengthPercentBonus;
	public float FortitudePercentBonus;
	public float SpeedPercentBonus;
	public float EndurancePercentBonus;
	public float LuckPercentBonus;
	public float CharismaPercentBonus;
	[Space]
	public EquipmentType EquipmentType;
}
