using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Text;

public class ItemToolTip : MonoBehaviour {
	[SerializeField] Text itemNameText;
	[SerializeField] Text itemTypeText;
	[SerializeField] Text itemStatsText;

	private StringBuilder stringBuilder = new StringBuilder( );

	public void ShowToolTip (EquippableItem item) {
		itemNameText.text = item.ItemName;
		itemTypeText.text = item.EquipmentType.ToString( );

		stringBuilder.Length = 0;

		AddStat(item.HealthBonus, "Health");
		AddStat(item.MysticPowerBonus, "Mystic Power");
		AddStat(item.StrengthBonus, "Strength");
		AddStat(item.DefenseBonus, "Defense");
		AddStat(item.MysticStrengthBonus, "Mystic Strength");
		AddStat(item.FortitudeBonus, "Fortitude");

		AddStat(item.SpeedPercentBonus, "Speed", isPercent: true);
		AddStat(item.EndurancePercentBonus, "Endurance", isPercent: true);
		AddStat(item.LuckPercentBonus, "Luck", isPercent: true);
		AddStat(item.CharismaPercentBonus, "Charisma", isPercent: true);

		itemStatsText.text = stringBuilder.ToString( );

		gameObject.SetActive(true);
	}

	public void HideToolTip ( ) {
		gameObject.SetActive(false);
	}

	private void AddStat (float value, string statName, bool isPercent = false) {
		if (value != 0) {
			if (stringBuilder.Length > 0) {
				stringBuilder.AppendLine( );
			}

			if (value > 0) {
				stringBuilder.Append("+");
			}

			if (isPercent) {
				stringBuilder.Append(value * 100);
				stringBuilder.Append("% ");
			} else {
				stringBuilder.Append(value);
				stringBuilder.Append(" ");
			}

			stringBuilder.Append(statName);
		}
	}
}
