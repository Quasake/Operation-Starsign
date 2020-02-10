using UnityEngine.UI;
using UnityEngine;

public class StatDisplay : MonoBehaviour {
	public Text NameText;
	public Text ValueText;

	private void OnValidate ( ) {
		Text[ ] texts = GetComponentsInChildren<Text>( );
		NameText = texts[0];
		ValueText = texts[1];
	}
}
