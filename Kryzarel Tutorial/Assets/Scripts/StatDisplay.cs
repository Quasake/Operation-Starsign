using UnityEngine.UI;
using UnityEngine;
using UnityEngine.EventSystems;

public class StatDisplay : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler {
	private CharacterStat _stat;
	public CharacterStat Stat {
		get {
			return _stat;
		}
		set {
			_stat = value;

			UpdateStatValue( );
		}
	}

	private string _name;
	public string Name {
		get {
			return _name;
		}
		set {
			_name = value;

			nameText.text = _name;
		}
	}

	[SerializeField] Text nameText;
	[SerializeField] Text valueText;
	[Space]
	[SerializeField] StatToolTip statToolTip;

	private void OnValidate ( ) {
		Text[ ] texts = GetComponentsInChildren<Text>( );
		nameText = texts[0];
		valueText = texts[1];

		if (statToolTip == null) {
			statToolTip = FindObjectOfType<StatToolTip>( );
		}
	}

	public void UpdateStatValue ( ) {
		valueText.text = _stat.Value.ToString( );
	}

	public void OnPointerEnter (PointerEventData eventData) {
		statToolTip.ShowToolTip(Stat, Name);
	}

	public void OnPointerExit (PointerEventData eventData) {
		statToolTip.HideToolTip( );
	}
}
