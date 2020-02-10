using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;

[Serializable]
public class CharacterStat {
	public float BaseValue;

	public virtual float Value {
		get {
			if (isDirty || BaseValue != _baseValue) {
				_baseValue = BaseValue;
				_value = CalculateFinalValue( );

				isDirty = false;
			}
			return _value;
		}
	}

	protected bool isDirty = true;
	protected float _value;
	protected float _baseValue = float.MinValue;

	protected readonly List<StatModifier> statModifiers;
	public readonly ReadOnlyCollection<StatModifier> StatModifiers;

	public CharacterStat ( ) {
		statModifiers = new List<StatModifier>( );
		StatModifiers = statModifiers.AsReadOnly( );
	}

	public CharacterStat (float baseValue) : this( ) {
		BaseValue = baseValue;
	}

	public virtual void AddModifier (StatModifier statMod) {
		isDirty = true;

		statModifiers.Add(statMod);
		statModifiers.Sort(CompareModifierOrder);
	}

	public virtual bool RemoveModifier (StatModifier statMod) {
		if (statModifiers.Remove(statMod)) {
			return isDirty = true;
		}

		return false;
	}

	public virtual bool RemoveAllModifiersFromSource (object source) {
		bool didRemove = false;

		for (int i = statModifiers.Count - 1; i >= 0; i--) {
			if (statModifiers[i].Source == source) {
				RemoveModifier(statModifiers[i]);

				didRemove = true;
			}
		}

		return didRemove;
	}

	protected virtual int CompareModifierOrder (StatModifier statMod1, StatModifier statMod2) {
		if (statMod1.Order < statMod2.Order) {
			return -1;
		} else if (statMod1.Order > statMod2.Order) {
			return 1;
		}

		return 0;
	}

	protected virtual float CalculateFinalValue ( ) {
		float finalValue = BaseValue;
		float sumPercentAdd = 0;

		for (int i = 0; i < statModifiers.Count; i++) {
			StatModifier statMod = statModifiers[i];

			if (statMod.Type == StatModifierType.NUMBER) {
				finalValue += statMod.Value;
			} else if (statMod.Type == StatModifierType.PERCENT_ADD) {
				sumPercentAdd += statMod.Value;

				if (i + 1 >= statModifiers.Count || statModifiers[i + 1].Type != StatModifierType.PERCENT_ADD) {
					finalValue *= 1 + sumPercentAdd;
					sumPercentAdd = 0;
				}
			} else if (statMod.Type == StatModifierType.PERCENT_MULT) {
				finalValue *= 1 + statMod.Value;
			}
		}

		return (float) Math.Round(finalValue, 4);
	}
}
