using System.Collections;
using System.Collections.Generic;
using System.Text;
using UnityEngine;
using UnityEngine.UI;

public class StatToolTip : MonoBehaviour {
	[SerializeField] Text statNameText;
	[SerializeField] Text statModfiersText;

	private StringBuilder stringBuilder = new StringBuilder( );

	public void ShowToolTip (CharacterStat stat, string statName) {
		statNameText.text = GetStatTopText(stat, statName);
		statModfiersText.text = GetStatModifiersText(stat);

		gameObject.SetActive(true);
	}

	public void HideToolTip ( ) {
		gameObject.SetActive(false);
	}

	private string GetStatTopText (CharacterStat stat, string statName) {
		stringBuilder.Length = 0;

		stringBuilder.Append(statName);
		stringBuilder.Append(" ");
		stringBuilder.Append(stat.Value);

		if (stat.Value != stat.BaseValue) {
			stringBuilder.AppendLine( );

			stringBuilder.Append(" (");
			stringBuilder.Append(stat.BaseValue);
			stringBuilder.Append(" ");

			if (stat.Value >= stat.BaseValue) {
				stringBuilder.Append("+");
			} else {
				stringBuilder.Append("-");
			}

			stringBuilder.Append(" ");
			stringBuilder.Append(System.Math.Round(Mathf.Abs(stat.Value - stat.BaseValue), 4));
			stringBuilder.Append(")");
		}

		return stringBuilder.ToString( );
	}

	private string GetStatModifiersText (CharacterStat stat) {
		stringBuilder.Length = 0;

		foreach (StatModifier modifier in stat.StatModifiers) {
			if (stringBuilder.Length > 0) {
				stringBuilder.AppendLine( );
			}

			if (modifier.Value > 0) {
				stringBuilder.Append("+");
			}

			if (modifier.Type == StatModifierType.NUMBER) {
				stringBuilder.Append(modifier.Value);
			} else {
				stringBuilder.Append(modifier.Value * 100);
				stringBuilder.Append("%");
			}

			EquippableItem item = modifier.Source as EquippableItem;

			if (item != null) {
				stringBuilder.Append(" ");
				stringBuilder.Append(item.ItemName);
			} else {
				Debug.LogError("Modifier is not an Equippable Item!");
			}
		}

		return stringBuilder.ToString( );
	}
}
