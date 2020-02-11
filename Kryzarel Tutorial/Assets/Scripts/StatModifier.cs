public enum StatModifierType {
	NUMBER = 10,
	PERCENT_ADD = 20,
	PERCENT_MULT = 30
}

// Kryzarel Youtube Channel : https://www.youtube.com/channel/UCOM0GGMEcu-gyf4F1mT7A8Q

public class StatModifier {
	public readonly float Value;
	public readonly StatModifierType Type;
	public readonly int Order;
	public readonly object Source;

	public StatModifier (float value, StatModifierType type, int order, object source) {
		Value = value;
		Type = type;
		Order = order;
		Source = source;
	}

	public StatModifier (float value, StatModifierType type) : this(value, type, (int) type, null) { }

	public StatModifier (float value, StatModifierType type, int order) : this(value, type, order, null) { }

	public StatModifier (float value, StatModifierType type, object source) : this(value, type, (int) type, source) { }
}
